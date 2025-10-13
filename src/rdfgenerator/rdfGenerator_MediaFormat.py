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
    MediaFormat = ET.SubElement(RDF,'rcgs:MediaFormat',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(MediaFormat,'dcterms:title',row['ラベル'])
    rg.setData(MediaFormat,'rdfs:label',row['ラベル'])
    rg.setData(MediaFormat,'rdf:type',attrib={'rdf:resource':row['種別']})
    rg.setData(MediaFormat,'skos:prefLabel',row['名称@ja'],attrib={'xml:lang':'ja'})
    rg.setData(MediaFormat,'skos:prefLabel',row['名称@en'],attrib={'xml:lang':'en'})
    rg.setData(MediaFormat,'skos:prefLabel',row['名称@ko'],attrib={'xml:lang':'ko'})
    rg.setData(MediaFormat,'skos:prefLabel',row['名称@zh'],attrib={'xml:lang':'zh'})
    rg.setData(MediaFormat,'skos:altLabel',row['その他の名称A'])
    rg.setData(MediaFormat,'skos:altLabel',row['その他の名称B'])
    rg.setData(MediaFormat,'skos:altLabel',row['その他の名称C'])
    rg.setData(MediaFormat,'rcgs:dimension',row['大きさ'])
    rg.setData(MediaFormat,'schema:fileSize',row['データ容量'])
    rg.setData(MediaFormat,'schema:disambiguatingDescription',row['その他の識別的特徴'])
    rg.setData(MediaFormat,'dcterms:description',row['説明'])
    rg.setData(MediaFormat,'skos:note',row['カタロガー注記'])
    rg.setData(MediaFormat,'dcterms:source',row['出典A'])
    rg.setData(MediaFormat,'dcterms:source',row['出典B'])
    rg.setData(MediaFormat,'dcterms:source',row['出典C'])
    rg.setData(MediaFormat,'dcterms:source',row['出典D'])
    rg.setData(MediaFormat,'dcterms:source',row['出典E'])

    # if index==15:
    #     break
    # print(rg.prettify(RDF))
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName) ##バリデーションチェック
