#pip install sparqlwrapper
#https://rdflib.github.io/sparqlwrapper/

#SPARQLWrapper部分
from SPARQLWrapper import SPARQLWrapper, JSON
import csv
sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setQuery("""#Cats
SELECT ?item ?itemLabel ?JapanCorporateNumber ?VIAF ?NDL ?ISNI WHERE {
  ?item wdt:P31 wd:Q210167.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  OPTIONAL { ?item wdt:P3225 ?JapanCorporateNumber. }
  OPTIONAL { ?item wdt:P214 ?VIAF. }
  OPTIONAL { ?item wdt:P349 ?NDL. }
  OPTIONAL { ?item wdt:P213 ?ISNI. }
}
LIMIT 100""")

#指定した目的の値を取得
#propertyの値
def get_value(results, property):
    lst=[]
    for result in results["results"]["bindings"]:
        if property in result:
            lst.append(result[property]["value"])
        else:
            lst.append(None)
    return lst

def write_csv(file_name, lst):
    with open(file_name,"w",encoding="utf_8") as f:
        writer = csv.writer(f,lineterminator="\n")
        writer.writerows(lst)

sparql.setReturnFormat(JSON)
results = sparql.query().convert()

label_lst=get_value(results,"itemLabel")
item_lst=get_value(results,"item")

all_lst=[]
all_lst.append(label_lst)
all_lst.append(item_lst)

print(all_lst)

write_csv("test.csv",all_lst)
