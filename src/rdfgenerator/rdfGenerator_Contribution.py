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
    if row['rcgs:recordID']=='':#空データのスキップ
        continue
    Contribution = ET.SubElement(RDF,'rcgs:Contribution',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['rcgs:recordID']})
    rg.setData(Contribution,'rdf:value',attrib={'rdf:resource':row['Agent Contributor MobyGamesAuth::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Contribution,'schema:roleName',row['Role'])
    rg.setData(Contribution,'rcgs:nameStatement',row['NameStatement'])
    rg.setData(Contribution,'rcgs:actedCharacterName',row['actedCharacterName'])
    rg.setData(Contribution,'schema:character',attrib={'rdf:resource':row['CharacterID (TopicAuthority)']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Contribution,'dcterms:description',row['Description'])
    rg.setData(Contribution,'dcterms:source',rg.percentEncode(row['Source A']))
    rg.setData(Contribution,'dcterms:source',rg.percentEncode(row['Source B']))
    rg.setData(Contribution,'dcterms:source',rg.percentEncode(row['Source C']))
    # if index==100:
    #     break
    # rg.prettify(RDF)
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName)
