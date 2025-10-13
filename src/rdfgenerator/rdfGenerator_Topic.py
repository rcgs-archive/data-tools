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
    if row['レコードID']=='':#空データのスキップ
        continue
    Topic = ET.SubElement(RDF,'rcgs:Topic',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(Topic,'dcterms:title',row['rdfs:label'])
    rg.setData(Topic,'rdfs:label',row['rdfs:label'])
    rg.setData(Topic,'rdfs:label',row['rdfs:label'])
    rg.setData(Topic,'skos:prefLabel',row['タイトル@en'],attrib={'xml:lang':'en'})
    rg.setData(Topic,'skos:prefLabel',row['タイトル@zh'],attrib={'xml:lang':'zh'})
    rg.setData(Topic,'skos:prefLabel',row['タイトル@ja'],attrib={'xml:lang':'ja'})
    rg.setData(Topic,'skos:prefLabel',row['タイトル@ko'],attrib={'xml:lang':'ko'})
    rg.setData(Topic,'skos:altLabel',row['その他のタイトル@en'],attrib={'xml:lang':'en'})
    rg.setData(Topic,'skos:altLabel',row['その他のタイトル@zh'],attrib={'xml:lang':'zh'})
    rg.setData(Topic,'skos:altLabel',row['その他のタイトル@ja'],attrib={'xml:lang':'ja'})
    rg.setData(Topic,'skos:altLabel',row['その他のタイトル@ko'],attrib={'xml:lang':'ko'})
    chars = ['A','B','C','D','E','F','G','H','I','J','K','L']
    for char in chars:
        rg.setData(Topic,'rcgs:category',row['Topic Category '+char+'::rdfs:label'])
    rg.setData(Topic,'skos:inScheme',row['skos:inScheme'])
    rg.setData(Topic,'dctems:spatial',row['地理的範囲'])
    rg.setData(Topic,'dcterms:isPartOf',row['dcterms:isPartOf A'])
    rg.setData(Topic,'dcterms:isPartOf',row['dcterms:isPartOf B'])
    rg.setData(Topic,'dcterms:isPartOf',row['dcterms:isPartOf C'])
    rg.setData(Topic,'owl:sameAs',row['owl:sameAs'])
    rg.setData(Topic,'rdfs:seeAlso',row['dcterms:source'])
    rg.setData(Topic,'rdfs:seeAlso',row['Wikipedia URL'])
    rg.setData(Topic,'skos:note',row['注記'])
    # if index==90:
    #     break
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName)
