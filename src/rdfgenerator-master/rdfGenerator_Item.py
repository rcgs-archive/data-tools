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
    Item = ET.SubElement(RDF,'rcgs:Item',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(Item,'dcterms:title',row['Manifestation::ラベル'])
    rg.setData(Item,'rdfs:label',row['Manifestation::ラベル'])
    rg.setData(Item,'dcndl:holdlingAgent',attrib={'rdf:resource':row['管理者']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Item,'schema:owns',attrib={'rdf:resource':row['所有者']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Item,'rcgs:exemplarOf',attrib={'rdf:resource':row['例示されたパッケージ']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Item,'rcgs:donor',attrib={'rdf:resource':row['寄贈者']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Item,'dcterms:identifier',row['識別子A'])
    rg.setData(Item,'dcterms:identifier',row['識別子B'])
    rg.setData(Item,'dcterms:identifier',row['ma:identifier'])
    rg.setData(Item,'dcterms:spatial',row['保管場所'])
    rg.setData(Item,'schema:itemCondition',row['現物の状態報告'])
    rg.setData(Item,'dcterms:description',row['キャリア特性注記'])
    rg.setData(Item,'dcterms:description',row['数量に関する注記'])
    rg.setData(Item,'dcterms:description',row['大きさに関する注記'])
    rg.setData(Item,'dcterms:provinance',row['出所'])
    # if index==100:
        # break
    # print(rg.prettify(RDF))
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName)
