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
    if row['レコードID']=='':
        continue
    Variation = ET.SubElement(RDF,'rcgs:Variation',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(Variation,'dcterms:title',row['ラベル'])
    rg.setData(Variation,'rdfs:label',row['ラベル'])
    """
    chars = ['A','B','C','D','E']
    for char in chars:
        if not rg.isNullData([row['関連指示子'+char],row['貢献者'+char]]):
            contributor = ET.SubElement(Variation,'dcterms:contributor')
            Contribution = ET.SubElement(contributor,'rcgs:Contribution')
            rg.setData(Contribution,'rcgs:role',row['関連指示子'+char],attrib={'rdf:datatype':'schema:roleName'})
            rg.setData(Contribution,'rdf:value',attrib={'rdf:resource':'https://collection.rcgs.jp/s/rcgs/resource/'+row['貢献者'+char]})
    """
    rg.setData(Variation,'dcterms:date',row['日付'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
    rg.setData(Variation,'schema:award',row['賞'])
    rg.setData(Variation,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンA'])
    rg.setData(Variation,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンB'])
    rg.setData(Variation,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンC'])
    rg.setData(Variation,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンD'])
    rg.setData(Variation,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンE'])
    rg.setData(Variation,'schema:gamePlatform',attrib={'rdf:resource':row['Platform 6::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Variation,'schema:gamePlatform',attrib={'rdf:resource':row['Platform 7::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Variation,'schema:gamePlatform',attrib={'rdf:resource':row['Platform 8::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Variation,'schema:disambiguatingDescription',row['その他の識別的特徴'])
    rg.setData(Variation,'dcterms:abstract',row['概要'])
    chars = ['A','B','C','D','E']
    for char in chars:
        rg.setData(Variation,'rcgs:contentType',attrib={'rdfs:label':row['内容種別'+char],'rdf:resource':row['内容種別統制語彙 '+char+'::URI']})
    rg.setData(Variation,'schema:audio',attrib={'rdfs:label':row['音声'],'rdf:resource':row['音声統制語彙::URI']})
    rg.setData(Variation,'schema:color',attrib={'rdfs:label':row['色彩'],'rdf:resource':row['色彩統制語彙::URI']})
    rg.setData(Variation,'rcgs:aspectRatio',attrib={'rdfs:label':row['アスペクト比'],'rdf:resource':row['アスペクト比統制語彙::URI']})
    rg.setData(Variation,'dcterms:language',attrib={'rdf:resource':row['言語URI']})
    rg.setData(Variation,'rcgs:variationOf',attrib={'rdf:resource':row['表現された著作']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Variation,'rcgs:embodiment',attrib={'rdf:resource':row['Manifestation::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Variation,'dcterms:source',row['出典A'])
    rg.setData(Variation,'dcterms:source',row['出典B'])
    rg.setData(Variation,'dcterms:source',row['出典C'])
    rg.setData(Variation,'dcterms:source',row['出典D'])
    rg.setData(Variation,'dcterms:source',row['出典E'])
    rg.setData(Variation,'dcterms:source',row['出典F'])
    rg.setData(Variation,'dcterms:source',row['出典G'])
    rg.setData(Variation,'dcterms:source',row['出典H'])
    rg.setData(Variation,'dcterms:source',row['出典I'])
    rg.setData(Variation,'dcterms:source',row['出典J'])
    #print(rg.prettify(RDF))
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName)
