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

skip_uri = ["https://collection.rcgs.jp/s/rcgs/resource/PACKAGE0000932","https://collection.rcgs.jp/s/rcgs/resource/PACKAGE0004277",
"https://collection.rcgs.jp/s/rcgs/resource/PACKAGE0004447","https://collection.rcgs.jp/s/rcgs/resource/PACKAGE0003965",
"https://collection.rcgs.jp/s/rcgs/resource/PACKAGE0008187","https://collection.rcgs.jp/s/rcgs/resource/PACKAGE0010016",
"https://collection.rcgs.jp/s/rcgs/resource/PACKAGE0015407"]

for index,row in df_DB.iterrows():
    if row['URI'] in skip_uri:
        continue
    Package=ET.SubElement(RDF,'rcgs:PhysicalPackage',attrib={'rdf:about':row['URI']})
    rg.setData(Package,'rdfs:label',row['ラベル'])
    rg.setData(Package,'dc:title',row['タイトル'])
    rg.setData(Package,'dcndl:titleTranscription',row['翻字タイトル @ja-Hrkt'],attrib={'xml:lang':'ja-Hrkt'})
    rg.setData(Package,'dcndl:titleTranscription',row['翻字タイトル @ja-Latn'],attrib={'xml:lang':'ja-Latn'})
    rg.setData(Package,'rcgs:abbreviatedTitle',row['省略タイトル'])
    rg.setData(Package,'rcgs:parallelTitle',row['並列タイトルA'])
    rg.setData(Package,'rcgs:parallelTitle',row['並列タイトルB'])
    rg.setData(Package,'rcgs:parallelTitle',row['並列タイトルC'])
    rg.setData(Package,'rcgs:parallelTitle',row['並列タイトルD'])
    rg.setData(Package,'rcgs:variantTitle',row['異形タイトル A'])
    rg.setData(Package,'rcgs:variantTitle',row['異形タイトル B'])
    rg.setData(Package,'dcndl:edition',row['エディションA'])
    rg.setData(Package,'dcndl:edition',row['エディションB'])
    rg.setData(Package,'dcndl:edition',row['エディションC'])
    rg.setData(Package,'dcterms:rights',row['著作権年'])
    rg.setData(Package,'dcterms:source',row['出典：タイトル'])
    rg.setData(Package,'dcterms:source',row['出典：入手条件'])
    rg.setData(Package,'dcterms:tableOfContents',row['サブユニットリスト'])
    rg.setData(Package,'schema:contentRating',row['レーティング A'])
    rg.setData(Package,'schema:contentRating',row['レーティング B'])
    rg.setData(Package,'schema:contentRating',row['レーティング C'])
    rg.setData(Package,'schema:copyrightYear',row['著作権年'])
    rg.setData(Package,'schema:gamePlatform',row['プラットフォーム A'])
    rg.setData(Package,'schema:gamePlatform',row['プラットフォーム B'])
    rg.setData(Package,'schema:gamePlatform',row['プラットフォーム C'])
    rg.setData(Package,'schema:gamePlatform',row['プラットフォーム D'])
    rg.setData(Package,'schema:gtin13',row['GTIN A'])
    rg.setData(Package,'schema:gtin13',row['GTIN B'])
    rg.setData(Package,'schema:gtin13',row['GTIN C'])
    rg.setData(Package,'schema:numberOfPlayers',row['プレイヤ数 A'])
    rg.setData(Package,'schema:numberOfPlayers',row['プレイヤ数 B'])
    rg.setData(Package,'schema:numberOfPlayers',row['プレイヤ数 C'])
    rg.setData(Package,'schema:price',row['入手条件 価格'])
    rg.setData(Package,'schema:requirement',row['装置システム要件A'].replace('\n',' ')) #改行を空白に置換
    rg.setData(Package,'schema:requirement',row['装置システム要件B'].replace('\n',' '))
    rg.setData(Package,'schema:requirement',row['装置システム要件C'].replace('\n',' '))
    rg.setData(Package,'schema:requirement',row['装置システム要件D'].replace('\n',' '))
    rg.setData(Package,'schema:requirement',row['装置システム要件E'].replace('\n',' '))
    rg.setData(Package,'schema:requirement',row['装置システム要件F'].replace('\n',' '))
    rg.setData(Package,'rcgs:jpNumber',row['全国書誌番号'])
    rg.setData(Package,'schema:brand',row['ブランド'])
    rg.setData(Package,'rcgs:ndlBiBID',row['国立国会図書館書誌ID'])
    rg.setData(Package,'schema:servicePhone',row['コンタクト情報A'])
    rg.setData(Package,'schema:servicePhone',row['コンタクト情報B'])
    rg.setData(Package,'schema:servicePhone',row['コンタクト情報C'])
    rg.setData(Package,'schema:servicePhone',row['コンタクト情報D'])
    rg.setData(Package,'schema:servicePhone',row['コンタクト情報E'])
    rg.setData(Package,'schema:servicePhone',row['コンタクト情報F'])
    rg.setData(Package,'schema:servicePhone',row['コンタクト情報G'])
    rg.setData(Package,'schema:servicePhone',row['コンタクト情報H'])
    rg.setData(Package,'schema:url',attrib={'rdf:resource':rg.percentEncode(row['オフィシャルウェブサイト'])})
    rg.setData(Package,'schema:videoFormat',row['放送標準'])
    rg.setData(Package,'schema:videoFrameSize',row['解像度'])
    rg.setData(Package,'rcgs:digitalFileType',attrib={'rdfs:label':row['デジタルファイルタイプ'],'rdf:resource':row['デジタルファイル種別統制語彙 2::URI']})
    rg.setData(Package,'rcgs:dimension',row['大きさ コンテナ'])
    rg.setData(Package,'dcterms:medium',attrib={'rdfs:label':row['基礎素材 A'],'rdf:resource':row['素材統制語彙 A::URI']})
    rg.setData(Package,'dcterms:medium',attrib={'rdfs:label':row['基礎素材 B'],'rdf:resource':row['素材統制語彙 B::URI']})
    rg.setData(Package,'dcterms:medium',attrib={'rdfs:label':row['基礎素材 C'],'rdf:resource':row['素材統制語彙 C::URI']})
    rg.setData(Package,'dcterms:medium',attrib={'rdfs:label':row['基礎素材 D'],'rdf:resource':row['素材統制語彙 D::URI']})
    rg.setData(Package,'dcterms:medium',attrib={'rdfs:label':row['基礎素材 E'],'rdf:resource':row['素材統制語彙 E::URI']})
    rg.setData(Package,'dcterms:medium',attrib={'rdfs:label':row['基礎素材 F'],'rdf:resource':row['素材統制語彙 F::URI']})
    rg.setData(Package,'dcterms:medium',attrib={'rdfs:label':row['応用素材'],'rdf:resource':row['素材統制語彙 G::URI']})
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンA'])
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンB'])
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンC'])
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンD'])
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンE'])
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンF'])
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンG'])
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンH'])
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンI'])
    rg.setData(Package,'rcgs:middlewareOrGameEngine',row['ミドルウェア・ゲームエンジンJ'])
    rg.setData(Package,'rcgs:modeOfIssuance',attrib={'rdfs:label':row['刊行方式'],'rdf:resource':row['刊行方式統制語彙::URI']})
    rg.setData(Package,'dcndl:publicationPeriodicity',attrib={'rdfs:label':row['刊行頻度'],'rdf:resource':row['刊行頻度統制語彙::URI']})
    rg.setData(Package,'rcgs:modelNumber',row['型番 A'])
    rg.setData(Package,'rcgs:modelNumber',row['型番 B'])
    rg.setData(Package,'rcgs:ratingContentDescriptor',row['レーティング内容記述子A1'])
    rg.setData(Package,'rcgs:ratingContentDescriptor',row['レーティング内容記述子A6'])
    rg.setData(Package,'rcgs:ratingContentDescriptor',row['レーティング内容記述子B1'])
    rg.setData(Package,'rcgs:ratingContentDescriptor',row['レーティング内容記述子B6'])
    rg.setData(Package,'rcgs:ratingContentDescriptor',row['レーティング内容記述子C1'])
    rg.setData(Package,'rcgs:ratingContentDescriptor',row['レーティング内容記述子C6'])
    rg.setData(Package,'rcgs:seriesStatement',row['シリーズ表示A'])
    rg.setData(Package,'rcgs:seriesStatement',row['シリーズ表示B'])
    rg.setData(Package,'rcgs:seriesStatement',row['シリーズ表示C'])
    rg.setData(Package,'rcgs:subseriesStatement',row['サブシリーズ表示A'])
    rg.setData(Package,'rcgs:subseriesStatement',row['サブシリーズ表示B'])
    rg.setData(Package,'rcgs:subseriesStatement',row['サブシリーズ表示C'])
    rg.setData(Package,'rcgs:responsibilityStatement',row['責任表示'])
    rg.setData(Package,'schema:serialNumber',row['シリアルナンバー'])
    rg.setData(Package,'schema:regionsAllowed',row['リージョンコード'])

    if not rg.isNullData([row['キャリア種別 メインユニット'],row['数量 メインユニット'],row['エンコーディング形式'],row['大きさ メインユニット']]):
        Format=ET.SubElement(Package,'dcterms:format')
        MediaTypeOrExtent_Format = ET.SubElement(Format,'dcterms:MediaTypeOrExtent')
        rg.setData(MediaTypeOrExtent_Format,'dc:type',attrib={'rdfs:label':row['キャリア種別 メインユニット'],'rdf:resource':row['キャリア種別メインユニット統制語彙::URI']})
        rg.setData(MediaTypeOrExtent_Format,'dc:extent',row['数量 メインユニット'])
        rg.setData(MediaTypeOrExtent_Format,'schema:encodingFormat',row['エンコーディング形式'])
        rg.setData(MediaTypeOrExtent_Format,'rcgs:dimension',row['大きさ メインユニット'])

    if not rg.isNullData([row['キャリア種別 サブユニット'],row['数量 サブユニット'],row['大きさ サブユニット']]):
        FormatOfSubunit=ET.SubElement(Package,'rcgs:formatOfSubunit')
        MediaTypeOrExtent_FormatOfSubunit = ET.SubElement(FormatOfSubunit,'dcterms:MediaTypeOrExtent')
        rg.setData(MediaTypeOrExtent_FormatOfSubunit,'dc:type',attrib={'rdfs:label':row['キャリア種別 サブユニット'],'rdf:resource':row['キャリア種別サブユニット統制語彙 2::URI']})
        rg.setData(MediaTypeOrExtent_FormatOfSubunit,'dcterms:extent',row['数量 サブユニット'])
        rg.setData(MediaTypeOrExtent_FormatOfSubunit,'rcgs:dimension',row['大きさ サブユニット'])

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

    if not rg.isNullData([row['Agent Publisher::主体種別'],row['Agent Publisher::名前A']]):
        Publisher = ET.SubElement(Package,'rcgs:publisher')
        type = ''
        if row['Agent Publisher::主体種別']=='http://xmlns.com/foaf/0.1/Organization':
            type = 'foaf:Organization'
        elif row['Agent Publisher::主体種別']=='http://xmlns.com/foaf/0.1/Person':
            type = 'foaf:Person'
        Agent_Publisher = ET.SubElement(Publisher,type)
        rg.setData(Agent_Publisher,'rdfs:label',row['Agent Publisher::主体ラベル'])
        rg.setData(Agent_Publisher,'skos:prefLabel',row['Agent Publisher::名前A'])

    if not rg.isNullData([row['Agent Distributor::主体種別'],row['Agent Distributor::名前A']]):
        Distributor = ET.SubElement(Package,'rcgs:distributor')
        type = ''
        if row['Agent Distributor::主体種別']=='http://xmlns.com/foaf/0.1/Organization':
            type = 'foaf:Organization'
        elif row['Agent Distributor::主体種別']=='http://xmlns.com/foaf/0.1/Person':
            type = 'foaf:Person'
        Agent_Distributor = ET.SubElement(Distributor,type)
        rg.setData(Agent_Distributor,'rdfs:label',row['Agent Distributor::主体ラベル'])
        rg.setData(Agent_Distributor,'skos:prefLabel',row['Agent Distributor::名前A'])

    rg.setData(Package,'dcterms:hasPart',attrib={'rdf:resource':row['hasPartA URI']})
    rg.setData(Package,'dcterms:hasPart',attrib={'rdf:resource':row['hasPartB URI']})
    rg.setData(Package,'dcterms:hasPart',attrib={'rdf:resource':row['hasPartC URI']})
    rg.setData(Package,'dcterms:isPartOf',attrib={'rdf:resource':row['isPart URI']})

    if not rg.isNullData([row['ItemDBExpression::内容種別A'],row['ItemDBExpression::日付'],row['ItemDBExpression::言語URI']]):
        EmbodimentOf = ET.SubElement(Package,'rcgs:embodimentOf')
        Variation = ET.SubElement(EmbodimentOf,'rcgs:Variation')
        rg.setData(Variation,'dcterms:language',attrib={'rdf:resource':row['ItemDBExpression::言語URI']})
        rg.setData(Variation,'dcterms:date',row['ItemDBExpression::日付'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})

        rg.setData(Variation,'schema:audio',attrib={'rdfs:label':row['ItemDBExpression::音声'],'rdf:resource':row['音声統制語彙::URI']})
        rg.setData(Variation,'schema:color',attrib={'rdfs:label':row['ItemDBExpression::色彩'],'rdf:resource':row['色彩統制語彙::URI']})
        rg.setData(Variation,'rcgs:aspectRatio',attrib={'rdfs:label':row['ItemDBExpression::アスペクト比'],'rdf:resource':row['アスペクト比統制語彙::URI']})
        rg.setData(Variation,'rcgs:contentType',attrib={'rdfs:label':row['ItemDBExpression::内容種別A'],'rdf:resource':row['内容種別統制語彙 A::URI']})
        rg.setData(Variation,'rcgs:contentType',attrib={'rdfs:label':row['ItemDBExpression::内容種別B'],'rdf:resource':row['内容種別統制語彙 B::URI']})
        rg.setData(Variation,'rcgs:contentType',attrib={'rdfs:label':row['ItemDBExpression::内容種別C'],'rdf:resource':row['内容種別統制語彙 C::URI']})
        rg.setData(Variation,'rcgs:contentType',attrib={'rdfs:label':row['ItemDBExpression::内容種別D'],'rdf:resource':row['内容種別統制語彙 D::URI']})
        rg.setData(Variation,'rcgs:contentType',attrib={'rdfs:label':row['ItemDBExpression::内容種別E'],'rdf:resource':row['内容種別統制語彙 E::URI']})
        rg.setData(Variation,'rcgs:contentType',attrib={'rdfs:label':row['ItemDBExpression::内容種別F'],'rdf:resource':row['内容種別統制語彙 F::URI']})

        if not rg.isNullData(row['ItemDBWork::Wikidata ID']):
            VariationOf = ET.SubElement(Variation,'rcgs:variationOf')
            Work = ET.SubElement(VariationOf,'rcgs:Work')

            # wikiData情報が怪しいため、creater情報は一旦消す.後日、確認作業が必要
            # chars = ['A','B','C','D','E','F','G','H','I','J','K','L']
            # for char in chars:
            #     if not rg.isNullData([row['Work Creator '+char+'::団体統制形アクセスポイント'],row['Work Creator '+char+'::主体種別'],row['ItemDBWork::創作者'+char]]):
            #         Creator = ET.SubElement(Work,'dcterms:creator')
            #         # type = ''
            #         # if row['Work Creator '+char+'::主体種別']=='http://xmlns.com/foaf/0.1/Organization':
            #         #     type = 'foaf:Organization'
            #         # elif row['Work Creator '+char+'::主体種別']=='http://xmlns.com/foaf/0.1/Person':
            #         #     type = 'foaf:Person'
            #         # Agent = ET.SubElement(Creator,type)
            #         Agent = ET.SubElement(Creator,'foaf:Agent')
            #         rg.setData(Agent,'rdfs:label',row['Work Creator '+char+'::団体統制形アクセスポイント'])
            #         # rg.setData(Agent,'rdf:type',attrib={'rdf:resource':row['Work Creator '+char+'::主体種別']})
            #         rg.setData(Agent,'skos:prefLabel',row['ItemDBWork::創作者'+char])

            # 主体種別を持たないAgentデータがあるので一時的にコメントアウト
            chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
            for char in chars:
                if not rg.isNullData([row['Agent WorkProductionCompany '+char+'::主体ラベル'],row['Agent WorkProductionCompany '+char+'::主体種別'],row['ItemDBWork::制作企業'+char]]):
                    productionCompany = ET.SubElement(Work,'schema:productionCompany')
                    type = ''
                    if row['Agent WorkProductionCompany '+char+'::主体種別']=='http://xmlns.com/foaf/0.1/Organization':
                        type = 'foaf:Organization'
                    elif row['Agent WorkProductionCompany '+char+'::主体種別']=='http://xmlns.com/foaf/0.1/Person':
                        type = 'foaf:Person'
                    Agent = ET.SubElement(productionCompany,type)
                    rg.setData(Agent,'rdfs:label',row['Agent WorkProductionCompany '+char+'::主体ラベル'])
                    rg.setData(Agent,'skos:prefLabel',row['ItemDBWork::制作企業'+char])

            rg.setData(Work,'dc:type',row['ItemDBWork::形式'])
            rg.setData(Work,'dcterms:date',row['ItemDBWork::日付'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
            rg.setData(Work,'dcterms:subject',row['Work Series A::ラベル'])
            rg.setData(Work,'dcterms:subject',row['Work Series B::ラベル'])
            rg.setData(Work,'dcterms:subject',row['Work Series C::ラベル'])
            rg.setData(Work,'schema:locationCreated',row['ItemDBWork::出所'])

            chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL','AM','AN','AO','AP','AQ','AR','AS','AT','AU','AV','AW']
            for char in chars:
                rg.setData(Work,'schema:character',row['Topic Character '+char+'::rdfs:label'])

            chars = ['A','B','C','D','E','F','G','H','I']
            for char in chars:
                rg.setData(Work,'schema:genre',row['Work Genre '+char+'::rdfs:label'])

            chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
            for char in chars:
                rg.setData(Work,'schema:gameLocation',row['Work Place '+char+'::rdfs:label'])

            rg.setData(Work,'rcgs:metacritic',attrib = {'rdf:resource':row['ItemDBWork::Metacritics Link']})
            rg.setData(Work,'rcgs:freebase',row['ItemDBWork::Freebase ID'])
            rg.setData(Work,'rcgs:mobyGames',attrib = {'rdf:resource':row['ItemDBWork::Mobygames Link']})
            rg.setData(Work,'rcgs:imdb',attrib = {'rdf:resource':row['ItemDBWork::Imdb Link']})
            rg.setData(Work,'rcgs:twitch',attrib = {'rdf:resource':rg.percentEncode(row['ItemDBWork::twitch Link'])})
            rg.setData(Work,'rdfs:seeAlso',attrib = {'rdf:resource':rg.percentEncode(row['ItemDBWork::外部の関連リソース (wikipedia)'])})
            rg.setData(Work,'schema:serialNumber',row['ItemDBWork::ナンバー指示子'])
            rg.setData(Work,'skos:prefLabel',row['ItemDBWork::タイトル@en'],attrib={'xml:lang':'en'})
            rg.setData(Work,'skos:prefLabel',row['ItemDBWork::タイトル@zh'],attrib={'xml:lang':'zh'})
            rg.setData(Work,'skos:prefLabel',row['ItemDBWork::タイトル@ja'],attrib={'xml:lang':'ja'})
            rg.setData(Work,'skos:prefLabel',row['ItemDBWork::タイトル@ko'],attrib={'xml:lang':'ko'})
            rg.setData(Work,'skos:altLabel',row['ItemDBWork::その他のタイトル@en'],attrib={'xml:lang':'en'})
            rg.setData(Work,'skos:altLabel',row['ItemDBWork::その他のタイトル@zh'],attrib={'xml:lang':'zh'})
            rg.setData(Work,'skos:altLabel',row['ItemDBWork::その他のタイトル@ja'],attrib={'xml:lang':'ja'})
            rg.setData(Work,'skos:altLabel',row['ItemDBWork::その他のタイトル@ko'],attrib={'xml:lang':'ko'})
            rg.setData(Work,'rcgs:precedes',attrib={'rdf:resource':row['先行の著作A']})
            rg.setData(Work,'rcgs:precedes',attrib={'rdf:resource':row['先行の著作B']})
            rg.setData(Work,'rcgs:precedes',attrib={'rdf:resource':row['先行の著作C']})
            rg.setData(Work,'rcgs:succeeds',attrib={'rdf:resource':row['後続の著作A']})
            rg.setData(Work,'rcgs:succeeds',attrib={'rdf:resource':row['後続の著作B']})
            rg.setData(Work,'rcgs:succeeds',attrib={'rdf:resource':row['後続の著作C']})
            rg.setData(Work,'skos:closeMatch',attrib = {'rdf:resource':row['ItemDBWork::Wikidata ID']},pretxt='https://www.wikidata.org/wiki/')
    # DEBUG:
    # try:
    #     rg.prettify(RDF)
    # except:
    #     print(row['URI'])
    # if index==100:
    #     break
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName)
