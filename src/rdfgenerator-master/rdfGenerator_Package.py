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

lst_nm = []
for index,row in df_DB.iterrows():
    if row['レコードID']=='':#空データのスキップ
        continue
    Package = ET.SubElement(RDF,row['クラス種別'],attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(Package,'dcterms:title',row['ラベル'])
    rg.setData(Package,'rdfs:label',row['ラベル'])
    rg.setData(Package,'dc:title',row['タイトル'])
    rg.setData(Package,'dcndl:titleTranscription',row['翻字タイトル @ja-Hrkt'],attrib={'xml:lang':'ja-Hrkt'})
    rg.setData(Package,'dcndl:titleTranscription',row['翻字タイトル @ja-Latn'],attrib={'xml:lang':'ja-Latn'})
    rg.setData(Package,'rcgs:parallelTitle',row['並列タイトルA'])
    rg.setData(Package,'rcgs:parallelTitle',row['並列タイトルB'])
    rg.setData(Package,'rcgs:parallelTitle',row['並列タイトルC'])
    rg.setData(Package,'rcgs:parallelTitle',row['並列タイトルD'])
    rg.setData(Package,'rcgs:variantTitle',row['異形タイトル A'])
    rg.setData(Package,'rcgs:variantTitle',row['異形タイトル B'])
    rg.setData(Package,'rcgs:abbreviatedTitle',row['省略タイトル'])
    rg.setData(Package,'dcndl:edition',row['エディションA'])
    rg.setData(Package,'dcndl:edition',row['エディションB'])
    rg.setData(Package,'dcndl:edition',row['エディションC'])
    rg.setData(Package,'rcgs:responsibilityStatement',row['責任表示'])
    rg.setData(Package,'rcgs:publisher',attrib={'rdf:resource':row['出版者']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Package,'rcgs:distributor',attrib={'rdf:resource':row['頒布者']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Package,'schema:brand',row['ブランド'])
    if not rg.isNullData([row['出版者名'],row['出版日正規化'],row['出版日取得元'],row['出版地']]):
        ProvisionActivity = ET.SubElement(Package,'rcgs:provisionActivity')
        Publication = ET.SubElement(ProvisionActivity,'rcgs:Publication')
        rg.setData(Publication,'dc:publisher',row['出版者名'])
        rg.setData(Publication,'dcterms:date',row['出版日正規化'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
        rg.setData(Publication,'dcterms:source',row['出版日取得元'],pretxt='Data from ')
        rg.setData(Publication,'dcterms:spatial',row['出版地'])
    if not rg.isNullData([row['頒布者名'],row['頒布日正規化'],row['頒布日取得元'],row['頒布地']]):
        ProvisionActivity = ET.SubElement(Package,'rcgs:provisionActivity')
        Distribution = ET.SubElement(ProvisionActivity,'rcgs:Distribution')
        rg.setData(Distribution,'dc:publisher',row['頒布者名'])
        rg.setData(Distribution,'dcterms:date',row['頒布日正規化'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
        rg.setData(Distribution,'dcterms:source',row['頒布日取得元'],pretxt='Data from ')
        rg.setData(Distribution,'dcterms:spatial',row['頒布地'])
    rg.setData(Package,'schema:copyrightYear',row['著作権年'])
    chars = ['A','B','C']
    for char in chars:
        if not rg.isNullData([row['シリーズ本タイトル '+char]]):
            if not rg.isNullData([row['シリーズ内ナンバー '+char]]):
                rg.setData(Package,'rcgs:seriesStatement',row['シリーズ本タイトル '+char]+' ; '+row['シリーズ内ナンバー '+char])
            else:
                rg.setData(Package,'rcgs:seriesStatement',row['シリーズ本タイトル '+char])
    for char in chars:
        if not rg.isNullData([row['サブシリーズ本タイトル '+char]]):
            if not rg.isNullData([row['サブシリーズ内ナンバー '+char]]):
                rg.setData(Package,'rcgs:subseriesStatement',row['サブシリーズ本タイトル '+char]+' ; '+row['サブシリーズ内ナンバー '+char])
            else:
                rg.setData(Package,'rcgs:subseriesStatement',row['サブシリーズ本タイトル '+char])
    rg.setData(Package,'rcgs:modeOfIssuance',attrib={'rdf:resource':row['刊行方式統制語彙::URI']})
    rg.setData(Package,'dcndl:publicationPeriodicity',attrib={'rdf:resource':row['刊行頻度統制語彙::URI']})
    rg.setData(Package,'schema:serialNumber',row['シリアルナンバー'])
    rg.setData(Package,'dcterms:identifier',row['ma:identifier'])
    rg.setData(Package,'schema:gtin13',row['GTIN A'])
    rg.setData(Package,'schema:gtin13',row['GTIN B'])
    rg.setData(Package,'schema:gtin13',row['GTIN C'])
    rg.setData(Package,'rcgs:modelNumber',row['型番 A'])
    rg.setData(Package,'rcgs:modelNumber',row['型番 B'])
    rg.setData(Package,'rcgs:jpNumber',row['全国書誌番号'])
    rg.setData(Package,'rcgs:ndlBiBID',row['国立国会図書館書誌ID'])
    if not rg.isNullData([row['キャリア種別 メインユニット'],row['数量 メインユニット'],row['エンコーディング形式'],row['大きさ メインユニット']]):
        Format=ET.SubElement(Package,'dcterms:format')
        MediaTypeOrExtent_Format = ET.SubElement(Format,'dcterms:MediaTypeOrExtent')
        rg.setData(MediaTypeOrExtent_Format,'dc:type',attrib={'rdf:resource':row['キャリア種別メインユニット統制語彙::URI']})
        rg.setData(MediaTypeOrExtent_Format,'dc:extent',row['数量 メインユニット'])
        rg.setData(MediaTypeOrExtent_Format,'schema:encodingFormat',attrib={'rdf:resource':row['エンコーディング形式パッケージ::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
        rg.setData(MediaTypeOrExtent_Format,'rcgs:dimension',row['大きさ メインユニット'])
    if not rg.isNullData([row['キャリア種別 サブユニット'],row['数量 サブユニット'],row['大きさ サブユニット']]):
        FormatOfSubunit=ET.SubElement(Package,'rcgs:formatOfSubunit')
        MediaTypeOrExtent_FormatOfSubunit = ET.SubElement(FormatOfSubunit,'dcterms:MediaTypeOrExtent')
        rg.setData(MediaTypeOrExtent_FormatOfSubunit,'dc:type',attrib={'rdf:resource':row['キャリア種別サブユニット統制語彙 2::URI']})
        rg.setData(MediaTypeOrExtent_FormatOfSubunit,'dcterms:extent',row['数量 サブユニット'])
        rg.setData(MediaTypeOrExtent_FormatOfSubunit,'rcgs:dimension',row['大きさ サブユニット'])
    rg.setData(Package,'schema:videoFormat',row['放送標準'])
    rg.setData(Package,'rcgs:digitalFileType',attrib={'rdf:resource':row['デジタルファイル種別統制語彙 2::URI']})
    rg.setData(Package,'schema:videoFrameSize',row['解像度'])
    rg.setData(Package,'schema:regionsAllowed',row['リージョンコード'])
    chars = ['A','B','C','D','E','F','G','H','I','J']
    for char in chars:
        rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジン'+char])
    chars = ['A','B','C','D']
    for char in chars:
        rg.setData(Package,'schema:gamePlatform',attrib={'rdf:resource':row['Packageプラットフォーム'+char+'::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Package,'schema:price',row['入手条件 価格'])
    chars = ['A','B','C']
    for char in chars:
        rg.setData(Package,'schema:contentRating',attrib={'rdf:resource':row['Packageレーティング'+char+'::レコードID']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    for n in range(1,7,1):
        rg.setData(Package,'rcgs:ratingContentDescriptor',row['レーティング内容記述子A'+str(n)])
    for n in range(1,7,1):
        rg.setData(Package,'rcgs:ratingContentDescriptor',row['レーティング内容記述子B'+str(n)])
    for n in range(1,7,1):
        rg.setData(Package,'rcgs:ratingContentDescriptor',row['レーティング内容記述子C'+str(n)])
    rg.setData(Package,'dcterms:accessRights',row['アクセス制限'])
    rg.setData(Package,'schema:numberOfPlayers',row['プレイヤ数 A'])
    rg.setData(Package,'schema:numberOfPlayers',row['プレイヤ数 B'])
    rg.setData(Package,'schema:numberOfPlayers',row['プレイヤ数 C'])
    chars = ['A','B','C','D','E','F']
    for char in chars:
        rg.setData(Package,'schema:requirement',row['装置システム要件'+char].replace('\n',' '))
    rg.setData(Package,'rcgs:embodimentOf',attrib={'rdf:resource':row['具体化されたバリエーション']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Package,'dcterms:hasPart',attrib={'rdf:resource':row['関連(hasPart) A']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Package,'dcterms:hasPart',attrib={'rdf:resource':row['関連(hasPart) B']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Package,'dcterms:hasPart',attrib={'rdf:resource':row['関連(hasPart) C']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(Package,'dcterms:isPartOf',attrib={'rdf:resource':row['関連(isPartOf)']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    chars = ['A','B','C','D','E','F','G','H']
    for char in chars:
        rg.setData(Package,'schema:servicePhone',row['コンタクト情報'+char])
    rg.setData(Package,'schema:url',row['オフィシャルウェブサイト'])
    rg.setData(Package,'dcterms:rights',row['著作権表記'])
    rg.setData(Package,'dcterms:tableOfContent',row['サブユニットリスト'])
    rg.setData(Package,'dcterms:source',row['出典：入手条件'])
    rg.setData(Package,'dcterms:source',row['出典：タイトル'])
    rg.setData(Package,'dcterms:description',row['説明(description)'])
    rg.setData(Package,'rcgs:dimension',row['大きさ コンテナ'])
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName)
