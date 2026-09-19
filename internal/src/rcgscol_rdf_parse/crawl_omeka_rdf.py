#!/usr/bin/env python3
"""Crawl the Omeka S REST API and write Turtle RDF.

Default target is the public site ``gc`` (ゲーム目録作成システム)
https://collection.rcgs.jp/s/gc — REST root is /api.

JSON-LD from /api/items is converted locally. Native ``format=turtle``
is not used, because some Omeka values are not valid IRIs.

Authentication (optional, for private resources):
  export OMEKA_KEY_IDENTITY=...
  export OMEKA_KEY_CREDENTIAL=...

Example:
  python crawl_omeka_rdf.py --site gc --out output/gc.ttl
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from typing import Any
from urllib.parse import urljoin

import requests
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DC, DCTERMS, FOAF, OWL, RDF, RDFS, SKOS, XSD

DEFAULT_BASE = "https://collection.rcgs.jp"
DEFAULT_SITE = "gc"

PREFIXES = {
    "o": "http://omeka.org/s/vocabs/o#",
    "dcterms": str(DCTERMS),
    "dc": str(DC),
    "dctype": "http://purl.org/dc/dcmitype/",
    "foaf": str(FOAF),
    "skos": str(SKOS),
    "rdfs": str(RDFS),
    "rdf": str(RDF),
    "owl": str(OWL),
    "xsd": str(XSD),
    "schema": "https://schema.org/",
    "dcndl": "http://ndl.go.jp/dcndl/terms/",
    "bibo": "http://purl.org/ontology/bibo/",
    "gc": "https://collection.rcgs.jp/gc/",
    "rcgs": "https://collection.rcgs.jp/terms/",
}

SKIP_KEYS = {
    "@context",
    "thumbnail_display_urls",
}

# o: metadata kept as triples (API URIs / literals).
OMEKA_LINK_KEYS = {
    "o:owner",
    "o:resource_class",
    "o:resource_template",
    "o:thumbnail",
    "o:primary_media",
    "o:media",
    "o:item_set",
    "o:site",
}


class OmekaClient:
    def __init__(
        self,
        base_url: str,
        key_identity: str | None = None,
        key_credential: str | None = None,
        timeout: int = 60,
        sleep: float = 0.2,
    ) -> None:
        self.base_url = base_url.rstrip("/") + "/"
        self.timeout = timeout
        self.sleep = sleep
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "rcgscol-rdf-parse/1.0",
                "Accept": "application/ld+json, application/json",
            }
        )
        self.auth: dict[str, str] = {}
        if key_identity and key_credential:
            self.auth = {
                "key_identity": key_identity,
                "key_credential": key_credential,
            }
        self._context: dict[str, str] | None = None

    def url(self, path: str) -> str:
        return urljoin(self.base_url, path.lstrip("/"))

    def get(self, path: str, params: dict[str, Any] | None = None) -> requests.Response:
        query = dict(self.auth)
        if params:
            query.update({k: v for k, v in params.items() if v is not None})
        response = self.session.get(self.url(path), params=query, timeout=self.timeout)
        response.raise_for_status()
        if self.sleep:
            time.sleep(self.sleep)
        return response

    def get_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        return self.get(path, params).json()

    def context(self) -> dict[str, str]:
        if self._context is None:
            payload = self.get_json("api-context")
            raw = payload.get("@context", payload)
            ctx: dict[str, str] = dict(PREFIXES)
            if isinstance(raw, dict):
                for key, value in raw.items():
                    if isinstance(value, str):
                        ctx[key] = value
            self._context = ctx
        return self._context

    def expand(self, term: str) -> str | None:
        if not term or not isinstance(term, str):
            return None
        if term.startswith(("http://", "https://", "urn:")):
            return term if _is_iri(term) else None
        if ":" not in term:
            return None
        prefix, local = term.split(":", 1)
        base = self.context().get(prefix)
        if not base:
            return None
        iri = f"{base}{local}"
        return iri if _is_iri(iri) else None

    def resolve_site_id(self, slug: str) -> int:
        sites = self.get_json("api/sites", {"per_page": 100})
        if not isinstance(sites, list):
            raise RuntimeError("unexpected /api/sites response")
        for site in sites:
            if site.get("o:slug") == slug:
                return int(site["o:id"])
        available = ", ".join(f"{s.get('o:slug')}({s.get('o:id')})" for s in sites)
        raise SystemExit(f"site slug {slug!r} not found. available: {available}")


def _is_iri(value: str) -> bool:
    if not value or any(ord(ch) > 127 for ch in value):
        return False
    if any(ch.isspace() for ch in value):
        return False
    if value.startswith(("http://", "https://")):
        return "/" in value[8:]
    return value.startswith(("urn:", "http://", "https://"))


def bind_prefixes(graph: Graph, context: dict[str, str]) -> None:
    for prefix, uri in {**PREFIXES, **context}.items():
        if isinstance(uri, str) and _is_iri(uri):
            graph.bind(prefix, Namespace(uri))


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def literal_from(value: dict[str, Any]) -> Literal:
    text = value.get("@value")
    datatype = value.get("@type") or value.get("type")
    lang = value.get("@language") or value.get("lang")
    if isinstance(datatype, str) and datatype.startswith("http") and not lang:
        return Literal(text, datatype=URIRef(datatype))
    if lang:
        return Literal(text, lang=lang)
    return Literal(text)


def add_value(
    graph: Graph,
    client: OmekaClient,
    subject: URIRef,
    predicate: URIRef,
    raw: Any,
) -> None:
    if raw is None or raw is False:
        return
    if isinstance(raw, bool):
        graph.add((subject, predicate, Literal(raw)))
        return
    if isinstance(raw, (int, float)) and not isinstance(raw, bool):
        graph.add((subject, predicate, Literal(raw)))
        return
    if isinstance(raw, str):
        iri = client.expand(raw)
        if iri:
            graph.add((subject, predicate, URIRef(iri)))
        else:
            graph.add((subject, predicate, Literal(raw)))
        return
    if not isinstance(raw, dict):
        return

    kind = raw.get("type")
    if kind in {"uri", "url"}:
        href = raw.get("@id") or raw.get("@value")
        if isinstance(href, str) and _is_iri(href):
            graph.add((subject, predicate, URIRef(href)))
        elif isinstance(href, str):
            graph.add((subject, predicate, Literal(href)))
        return

    if "@value" in raw:
        graph.add((subject, predicate, literal_from(raw)))
        return

    href = raw.get("@id")
    if isinstance(href, str) and _is_iri(href):
        graph.add((subject, predicate, URIRef(href)))
        return
    if isinstance(href, str):
        graph.add((subject, predicate, Literal(href)))


def resource_to_graph(client: OmekaClient, item: dict[str, Any], graph: Graph) -> None:
    subject_raw = item.get("@id")
    if not isinstance(subject_raw, str) or not _is_iri(subject_raw):
        return
    subject = URIRef(subject_raw)

    for type_term in as_list(item.get("@type")):
        iri = client.expand(type_term) if isinstance(type_term, str) else None
        if iri:
            graph.add((subject, RDF.type, URIRef(iri)))
        elif isinstance(type_term, str):
            graph.add((subject, RDF.type, Literal(type_term)))

    for key, raw in item.items():
        if key in SKIP_KEYS or key in {"@id", "@type"}:
            continue
        if key.startswith("o:") and key not in OMEKA_LINK_KEYS and key not in {
            "o:id",
            "o:is_public",
            "o:title",
            "o:created",
            "o:modified",
        }:
            continue
        pred_iri = client.expand(key)
        if not pred_iri:
            continue
        predicate = URIRef(pred_iri)
        for value in as_list(raw):
            add_value(graph, client, subject, predicate, value)


def crawl_items(
    client: OmekaClient,
    graph: Graph,
    *,
    site_id: int | None,
    per_page: int,
    max_pages: int | None,
    resource: str,
) -> int:
    page = 1
    count = 0
    while True:
        params: dict[str, Any] = {
            "page": page,
            "per_page": per_page,
            "sort_by": "id",
            "sort_order": "asc",
        }
        if site_id is not None:
            params["site_id"] = site_id
        response = client.get(f"api/{resource}", params)
        payload = response.json()
        if not isinstance(payload, list) or not payload:
            break
        for item in payload:
            if isinstance(item, dict):
                resource_to_graph(client, item, graph)
                count += 1
        total = response.headers.get("Omeka-S-Total-Results", "?")
        print(
            f"  {resource} page {page}  items={len(payload)}  "
            f"harvested={count}  triples={len(graph)}  total={total}",
            flush=True,
        )
        if max_pages is not None and page >= max_pages:
            break
        link = response.headers.get("Link", "")
        if 'rel="next"' not in link and "rel=next" not in link:
            if total.isdigit() and page * per_page >= int(total):
                break
            if not total.isdigit():
                break
        page += 1
    return count


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crawl Omeka S REST API and write Turtle RDF."
    )
    parser.add_argument(
        "--base",
        default=os.environ.get("OMEKA_BASE_URL", DEFAULT_BASE),
        help=f"Omeka S installation root (default: {DEFAULT_BASE})",
    )
    parser.add_argument("--site", default=DEFAULT_SITE, help="Site slug (default: gc)")
    parser.add_argument("--site-id", type=int, default=None, help="Overrides --site")
    parser.add_argument(
        "--all-sites",
        action="store_true",
        help="Do not filter by site_id (entire installation).",
    )
    parser.add_argument(
        "--resources",
        default="items",
        help="Comma-separated API resources (default: items)",
    )
    parser.add_argument("--per-page", type=int, default=100)
    parser.add_argument("--max-pages", type=int, default=None)
    parser.add_argument("--out", default="output/gc.ttl")
    parser.add_argument("--key-identity", default=os.environ.get("OMEKA_KEY_IDENTITY"))
    parser.add_argument(
        "--key-credential", default=os.environ.get("OMEKA_KEY_CREDENTIAL")
    )
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--sleep", type=float, default=0.15)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    client = OmekaClient(
        args.base,
        key_identity=args.key_identity,
        key_credential=args.key_credential,
        timeout=args.timeout,
        sleep=args.sleep,
    )

    site_id = args.site_id
    if not args.all_sites and site_id is None:
        site_id = client.resolve_site_id(args.site)
        print(f"site {args.site!r} -> id {site_id}", flush=True)

    graph = Graph()
    bind_prefixes(graph, client.context())

    resources = [r.strip() for r in args.resources.split(",") if r.strip()]
    for resource in resources:
        print(f"crawling api/{resource} ...", flush=True)
        try:
            crawl_items(
                client,
                graph,
                site_id=None if args.all_sites else site_id,
                per_page=args.per_page,
                max_pages=args.max_pages,
                resource=resource,
            )
        except requests.HTTPError as exc:
            print(f"skip {resource}: {exc}", file=sys.stderr)

    out_path = args.out
    parent = os.path.dirname(os.path.abspath(out_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    graph.serialize(destination=out_path, format="turtle")
    print(f"wrote {out_path}  triples={len(graph)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
