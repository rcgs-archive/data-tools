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
    Platform = ET.SubElement(RDF,'rcgs:Platform',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    # rg.setData(Platform,'rdf:type',attrib={'rdf:resource':row['種別']})
    rg.setData(Platform,'dcterms:title',row['ラベル'])
    rg.setData(Platform,'rdfs:label',row['ラベル'])
    rg.setData(Platform,'skos:prefLabel',row['名称@ja'],attrib={'xml:lang':'ja'})
    rg.setData(Platform,'skos:prefLabel',row['名称@en'],attrib={'xml:lang':'en'})
    rg.setData(Platform,'skos:prefLabel',row['名称@ko'],attrib={'xml:lang':'ko'})
    rg.setData(Platform,'skos:prefLabel',row['名称@zh'],attrib={'xml:lang':'zh'})
    rg.setData(Platform,'skos:altLabel',row['その他の名称A'])
    rg.setData(Platform,'skos:altLabel',row['その他の名称B'])
    rg.setData(Platform,'skos:altLabel',row['その他の名称C'])
    rg.setData(Platform,'dcterms:publisher',attrib={'rdf:resource':row['公開者']})
    rg.setData(Platform,'dcndl:location',row['公開地'])
    rg.setData(Platform,'dcterms:issued',row['公開日'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
    rg.setData(Platform,'schema:disambiguatingDescription',row['その他の識別的特徴'])
    rg.setData(Platform,'dcterms:identifier',row['識別子'])
    rg.setData(Platform,'rcgs:deviceImplimented',attrib={'rdf:resource':row['実装される装置A']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Platform,'rcgs:deviceImplimented',attrib={'rdf:resource':row['実装される装置B']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Platform,'rcgs:deviceImplimented',attrib={'rdf:resource':row['実装される装置C']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Platform,'rcgs:deviceImplimented',attrib={'rdf:resource':row['実装される装置D']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Platform,'rcgs:deviceImplimented',attrib={'rdf:resource':row['実装される装置E']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Platform,'rdfs:seeAlso',row['外部の関連リソース (Wikipedia)'])
    rg.setData(Platform,'schema:url',row['url'])
    rg.setData(Platform,'skos:note',row['カタロガー注記'])
    rg.setData(Platform,'dcterms:source',row['出典A'])
    rg.setData(Platform,'dcterms:source',row['出典B'])
    rg.setData(Platform,'dcterms:source',row['出典C'])
    rg.setData(Platform,'dcterms:source',row['出典D'])
    rg.setData(Platform,'dcterms:source',row['出典E'])
    # if index==15:
    #     break
    # print(rg.prettify(RDF))
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName) ##バリデーションチェック
