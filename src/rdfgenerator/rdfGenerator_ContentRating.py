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
    ContentRating = ET.SubElement(RDF,'rcgs:ContentRating',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(ContentRating,'dcterms:title',row['ラベル'])
    rg.setData(ContentRating,'rdfs:label',row['ラベル'])
    rg.setData(ContentRating,'skos:prefLabel',row['名称@ja'],attrib={'xml:lang':'ja'})
    rg.setData(ContentRating,'skos:prefLabel',row['名称@en'],attrib={'xml:lang':'en'})
    rg.setData(ContentRating,'skos:prefLabel',row['名称@ko'],attrib={'xml:lang':'ko'})
    rg.setData(ContentRating,'skos:prefLabel',row['名称@zh'],attrib={'xml:lang':'zh'})
    rg.setData(ContentRating,'skos:altLabel',row['その他の名称A'])
    rg.setData(ContentRating,'skos:altLabel',row['その他の名称B'])
    rg.setData(ContentRating,'skos:altLabel',row['その他の名称C'])
    rg.setData(ContentRating,'dcterms:spatial',row['地理的範囲'])
    rg.setData(ContentRating,'rcgs:wikidataID',row['Wikidata Link'])
    rg.setData(ContentRating,'rdfs:seeAlso',row['URL'])
    rg.setData(ContentRating,'dcterms:date',row['日付'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
    rg.setData(ContentRating,'dcndl:location',row['発行地'])
    rg.setData(ContentRating,'dcterms:publisher',attrib={'rdf:resource':row['発行者']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(ContentRating,'dc:publisher',row['発行者名'])
    rg.setData(ContentRating,'dcterms:description',row['説明'])
    rg.setData(ContentRating,'schema:logo',row['ロゴ'])
    rg.setData(ContentRating,'skos:note',row['カタロガー注記'])
    rg.setData(ContentRating,'dcterms:source',row['出典A'])
    rg.setData(ContentRating,'dcterms:source',row['出典B'])
    rg.setData(ContentRating,'dcterms:source',row['出典C'])
    rg.setData(ContentRating,'dcterms:source',row['出典D'])
    rg.setData(ContentRating,'dcterms:source',row['出典E'])

    # if index==15:
        # break
    # print(rg.prettify(RDF))
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName) ##バリデーションチェック
