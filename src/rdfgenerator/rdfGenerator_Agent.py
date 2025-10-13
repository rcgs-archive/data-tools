import xml.etree.ElementTree as ET #xml操作
import pandas as pd
import library_rdfGen as rg #yagi自作 #rdf生成用関数ライブラリ
import sys

args = sys.argv
inputFileName = args[1]
outputFileName = args[2]

df_DB = pd.read_csv(inputFileName,dtype=str,na_filter=False)

RDF = ET.Element('rdf:RDF')
rg.makePrefix(RDF)

for index,row in df_DB.iterrows():
    if row['主体種別']=='':#空データのスキップ
        continue
    if row['主体種別']=='http://xmlns.com/foaf/0.1/Organization':
        agentType = 'foaf:Organization'
    elif row['主体種別']=='http://xmlns.com/foaf/0.1/Person':
        agentType = 'foaf:Person'
    Agent = ET.SubElement(RDF,agentType,attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(Agent,'dcterms:title',row['主体ラベル'])
    rg.setData(Agent,'rdfs:label',row['主体ラベル'])
    rg.setData(Agent,'skos:prefLabel',row['skos:prefLabel @en'],attrib={'xml:lang':'en'})
    rg.setData(Agent,'skos:prefLabel',row['skos:prefLabel @jp'],attrib={'xml:lang':'ja'})
    rg.setData(Agent,'skos:prefLabel',row['skos:prefLabel @ko'],attrib={'xml:lang':'ko'})
    rg.setData(Agent,'skos:prefLabel',row['skos:prefLabel @zh'],attrib={'xml:lang':'zh'})
    rg.setData(Agent,'skos:altLabel',row['skos:altLabel @en'],attrib={'xml:lang':'en'})
    rg.setData(Agent,'skos:altLabel',row['skos:altLabel @jp'],attrib={'xml:lang':'ja'})
    rg.setData(Agent,'skos:altLabel',row['skos:altLabel @ko'],attrib={'xml:lang':'ko'})
    rg.setData(Agent,'skos:altLabel',row['skos:altLabel @zh'],attrib={'xml:lang':'zh'})
    rg.setData(Agent,'skos:altLabel',row['ブランドA'])
    rg.setData(Agent,'skos:altLabel',row['ブランドB'])
    rg.setData(Agent,'skos:altLabel',row['ブランドC'])
    rg.setData(Agent,'skos:altLabel',row['ブランドD'])
    rg.setData(Agent,'skos:altLabel',row['ブランドE'])
    rg.setData(Agent,'skos:altLabel',row['ブランドF'])
    rg.setData(Agent,'foaf:homepage',attrib={'rdf:resource':rg.percentEncode(row['ウェブサイト'])})
    rg.setData(Agent,'dcterms:description',row['略歴'].replace('\n',''))
    rg.setData(Agent,'dcterms:identifier',row['ma:identifier'])
    rg.setData(Agent,'rcgs:ndlAuthoritiesID',row['国立国会図書館典拠ID'].replace('-',''))
    rg.setData(Agent,'rcgs:viafID',row['バーチャル国際典拠ファイル Link'].replace('https://viaf.org/viaf/','').replace('-','')) #何故か数字認識されるのでLinkを使用
    rg.setData(Agent,'rcgs:wikidataID',row['Wikidata ID'].replace('-',''))
    rg.setData(Agent,'rcgs:twitterID',row['TwitterID'])
    rg.setData(Agent,'rdfs:seeAlso',attrib={'rdf:resource':rg.percentEncode(row['wikipedia'])})
    rg.setData(Agent,'dcterms:source',row['参照したウェブサイトA'])
    rg.setData(Agent,'dcterms:source',row['参照したウェブサイトB'])
    rg.setData(Agent,'dcterms:source',row['参照したウェブサイトC'])
    rg.setData(Agent,'dcterms:source',row['参照したウェブサイトD'])
    rg.setData(Agent,'dcterms:source',row['参照したウェブサイトE'])
    rg.setData(Agent,'dcterms:language',attrib={'rdf:resource':row['言語URI']})
    rg.setData(Agent,'skos:note',row['カタロガー注記'].replace('\n',''))
    rg.setData(Agent,'skos:note',row['注記'].replace('\n',''))
    rg.setData(Agent,'dcterms:source',row['出典A'])
    rg.setData(Agent,'dcterms:source',row['出典B'])
    rg.setData(Agent,'dcterms:source',row['出典C'])
    rg.setData(Agent,'dcterms:source',row['出典D'])
    rg.setData(Agent,'dcterms:source',row['出典E'])
    if row['主体種別']=='http://xmlns.com/foaf/0.1/Organization':
        rg.setData(Agent,'dc:type',row['団体種別'])
        rg.setData(Agent,'schema:startDate',row['始期'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
        rg.setData(Agent,'schema:endDate',row['終期'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
        rg.setData(Agent,'schema:address',row['アドレス'])
        rg.setData(Agent,'rcgs:relatedOrganization',attrib={'rdf:resource':row['関連する団体A']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
        rg.setData(Agent,'rcgs:relatedOrganization',attrib={'rdf:resource':row['関連する団体B']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
        rg.setData(Agent,'rcgs:relatedOrganization',attrib={'rdf:resource':row['関連する団体C']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    elif row['主体種別']=='http://xmlns.com/foaf/0.1/Person':
        rg.setData(Agent,'schema:hasOccupation',row['職業'])
        rg.setData(Agent,'schema:birthDate',row['生年'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
        rg.setData(Agent,'schema:deathDate',row['没年'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
        rg.setData(Agent,'schema:birthPlace',row['出生地'])
        rg.setData(Agent,'schema:deathPlace',row['死没地'])
        rg.setData(Agent,'schema:homeLocation',row['居住地等'])
        rg.setData(Agent,'schema:addressCountry',row['国'])
    # if index==1000:
    #     break
    # rg.prettify(RDF)
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName)
