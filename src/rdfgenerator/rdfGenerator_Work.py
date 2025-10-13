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
    Work = ET.SubElement(RDF,'rcgs:Work',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(Work,'dc:type',row['形式'])
    rg.setData(Work,'dcterms:title',row['ラベル'])
    rg.setData(Work,'skos:prefLabel',row['タイトル@en'],attrib={'xml:lang':'en'})
    rg.setData(Work,'skos:prefLabel',row['タイトル@zh'],attrib={'xml:lang':'zh'})
    rg.setData(Work,'skos:prefLabel',row['タイトル@ja'],attrib={'xml:lang':'ja'})
    rg.setData(Work,'skos:prefLabel',row['タイトル@ko'],attrib={'xml:lang':'ko'})
    rg.setData(Work,'skos:altLabel',row['その他のタイトル@en'],attrib={'xml:lang':'en'})
    rg.setData(Work,'skos:altLabel',row['その他のタイトル@zh'],attrib={'xml:lang':'zh'})
    rg.setData(Work,'skos:altLabel',row['その他のタイトル@ja'],attrib={'xml:lang':'ja'})
    rg.setData(Work,'skos:altLabel',row['その他のタイトル@ko'],attrib={'xml:lang':'ko'})
    rg.setData(Work,'dcterms:spatial',row['地理的範囲'])
    rg.setData(Work,'dcterms:date',row['日付'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
    rg.setData(Work,'skos:closeMatch',attrib = {'rdf:resource':row['Wikidata ID']},pretxt='https://www.wikidata.org/wiki/')
    rg.setData(Work,'rcgs:twitch',attrib = {'rdf:resource':rg.percentEncode(row['twitch Link'])})
    rg.setData(Work,'rcgs:freebase',row['Freebase ID'])
    rg.setData(Work,'rcgs:mobyGames',attrib = {'rdf:resource':row['Mobygames Link']})
    rg.setData(Work,'rcgs:metacritic',attrib = {'rdf:resource':row['Metacritics Link']})
    rg.setData(Work,'rdfs:seeAlso',attrib = {'rdf:resource':rg.percentEncode(row['外部の関連リソース (wikipedia)'])})
    rg.setData(Work,'rcgs:imdb',attrib = {'rdf:resource':row['Imdb Link']})
    rg.setData(Work,'dcterms:audience',row['対象者'])
    rg.setData(Work,'rcgs:natureOfContent',row['内容の性質'])
    rg.setData(Work,'schema:serialNumber',row['ナンバー指示子'])
    rg.setData(Work,'schema:disambiguatingDescription',row['その他の識別的特徴'])
    rg.setData(Work,'schema:locationCreated',row['出所'])
    rg.setData(Work,'dcterms:isPartOf',attrib={'rdf:resource':row['Work Series A::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'dcterms:isPartOf',attrib={'rdf:resource':row['Work Series B::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'dcterms:isPartOf',attrib={'rdf:resource':row['Work Series C::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    chars = ['A','B','C','D','E','F','G','H','I']
    for char in chars:
        rg.setData(Work,'schema:genre',row['Work Genre '+char+'::rdfs:label'])
    chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW']
    for char in chars:
        rg.setData(Work,'schema:character',row['Topic Character '+char+'::rdfs:label'])
    chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    for char in chars:
        rg.setData(Work,'schema:gameLocation',row['Work Place '+char+'::rdfs:label'])
    # wikiData情報が怪しいため、creater情報は一旦消す.後日、確認作業が必要
    # chars = ['A','B','C','D','E','F','G','H','I','J','K','L']
    # for char in chars:
    #     rg.setData(Work,'dcterms:creator',attrib={'rdf:resource':row['創作者'+char+' ID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
    for char in chars:
        rg.setData(Work,'schema:productionCompany',attrib={'rdf:resource':row['制作企業'+char+' ID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'rcgs:Variation',attrib={'rdf:resource':row['ItemDBExpression::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'rcgs:precedes',attrib={'rdf:resource':row['Work Proceeds A::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'rcgs:precedes',attrib={'rdf:resource':row['Work Proceeds B::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'rcgs:precedes',attrib={'rdf:resource':row['Work Proceeds C::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'rcgs:succeeds',attrib={'rdf:resource':row['Work Succeeds A::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'rcgs:succeeds',attrib={'rdf:resource':row['Work Succeeds B::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'rcgs:succeeds',attrib={'rdf:resource':row['Work Succeeds C::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Work,'dcterms:source',row['出典A'])
    rg.setData(Work,'dcterms:source',row['出典B'])
    rg.setData(Work,'dcterms:source',row['出典C'])
    rg.setData(Work,'dcterms:source',row['出典D'])
    rg.setData(Work,'dcterms:source',row['出典E'])
    #if index==100:
    #    break
    #print(rg.prettify(RDF))
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName) ##バリデーションチェック
