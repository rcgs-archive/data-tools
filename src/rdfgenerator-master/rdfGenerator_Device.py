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
    Device = ET.SubElement(RDF,'rcgs:Device',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(Device,'dcterms:title',row['ラベル'])
    rg.setData(Device,'rdfs:label',row['ラベル'])
    rg.setData(Device,'rcgs:deviceType',attrib={'rdf:resource':row['種別']})
    rg.setData(Device,'skos:prefLabel',row['名称'])
    rg.setData(Device,'skos:altLabel',row['その他の名称A'])
    rg.setData(Device,'skos:altLabel',row['その他の名称B'])
    rg.setData(Device,'skos:altLabel',row['その他の名称C'])
    rg.setData(Device,'dcndl:edition',row['エディションA'])
    rg.setData(Device,'dcndl:edition',row['エディションB'])
    rg.setData(Device,'dcndl:edition',row['エディションC'])
    rg.setData(Device,'schema:videoFormat',row['放送標準'])
    rg.setData(Device,'dcterms:spatial',row['地理的範囲'])
    rg.setData(Device,'schema:gtin13',row['GTIN'])
    rg.setData(Device,'schema:material',attrib={'rdf:resource':row['装置素材A::URI']})
    rg.setData(Device,'schema:material',attrib={'rdf:resource':row['装置素材B::URI']})
    rg.setData(Device,'schema:material',attrib={'rdf:resource':row['装置素材C::URI']})
    rg.setData(Device,'schema:material',attrib={'rdf:resource':row['装置素材D::URI']})
    rg.setData(Device,'schema:material',attrib={'rdf:resource':row['装置素材E::URI']})
    rg.setData(Device,'schema:material',attrib={'rdf:resource':row['装置素材F::URI']})
    rg.setData(Device,'schema:material',attrib={'rdf:resource':row['装置素材G::URI']})
    rg.setData(Device,'schema:material',attrib={'rdf:resource':row['装置素材H::URI']})
    rg.setData(Device,'rcgs:modelNumber',row['型番A'])
    rg.setData(Device,'rcgs:modelNumber',row['型番B'])
    rg.setData(Device,'dcterms:creator',attrib={'rdf:resource':row['頒布者']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'dcterms:issued',row['頒布日'])
    rg.setData(Device,'dcndl:location',row['頒布地'])
    rg.setData(Device,'rcgs:inserts',attrib={'rdf:resource':row['挿入されたパッケージ']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:gamePlatform',attrib={'rdf:resource':row['装置プラットフォームA::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:gamePlatform',attrib={'rdf:resource':row['装置プラットフォームB::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:gamePlatform',attrib={'rdf:resource':row['装置プラットフォームC::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:gamePlatform',attrib={'rdf:resource':row['装置プラットフォームD::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:gamePlatform',attrib={'rdf:resource':row['装置プラットフォームE::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:brand',row['ブランド'])
    rg.setData(Device,'rcgs:specConnection',row['接続仕様'])
    rg.setData(Device,'rcgs:controller',row['操作入力'])
    rg.setData(Device,'rcgs:dimension',row['大きさ'])
    rg.setData(Device,'rcgs:dimension',row['容器の大きさ'])
    rg.setData(Device,'schema:weight',row['重量'])
    rg.setData(Device,'dcterms:tableOfContent',row['サブユニットリスト'])
    rg.setData(Device,'schema:disambiguatingDescription',row['その他の識別的特徴'])
    rg.setData(Device,'schema:videoFrameSize',row['映像出力の解像度'])
    rg.setData(Device,'schema:sound',row['音声出力'])
    rg.setData(Device,'rcgs:powerConsumption',row['消費電力'])
    rg.setData(Device,'dcterms:description',row['システム仕様'])
    rg.setData(Device,'dcterms:description',row['映像出力の仕様'])
    rg.setData(Device,'dcterms:description',row['生産地表示'])
    rg.setData(Device,'skos:note',row['カタロガー注記'])
    rg.setData(Device,'dcterms:source',row['出典A'])
    rg.setData(Device,'dcterms:source',row['出典B'])
    rg.setData(Device,'dcterms:source',row['出典C'])
    rg.setData(Device,'dcterms:source',row['出典D'])
    rg.setData(Device,'dcterms:source',row['出典E'])
    rg.setData(Device,'schema:encodingFormat',attrib={'rdf:resource':row['装置エンコーディング形式A::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:encodingFormat',attrib={'rdf:resource':row['装置エンコーディング形式B::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:encodingFormat',attrib={'rdf:resource':row['装置エンコーディング形式C::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:encodingFormat',attrib={'rdf:resource':row['装置エンコーディング形式D::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'schema:encodingFormat',attrib={'rdf:resource':row['装置エンコーディング形式E::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Device,'dcterms:identifier',row['外部ID'])
    # if index==20:
    #     break
    # print(rg.prettify(RDF))
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName) ##バリデーションチェック
