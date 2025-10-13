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
    RelatedInstanseType = ''
    if row['クラス種別']=='rcgs:InstanceProductType':
        RelatedInstanseType = 'rcgs:InstanceProductType'
    RelatedInstanse = ET.SubElement(RDF,RelatedInstanseType,attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
    rg.setData(RelatedInstanse,'dcterms:title',row['ラベル'])
    rg.setData(RelatedInstanse,'rdfs:label',row['ラベル'])
    rg.setData(RelatedInstanse,'dc:title',row['タイトル'])
    rg.setData(RelatedInstanse,'dcndl:titleTranscription',row['翻字タイトル @ja-Hrkt'],attrib={'xml:lang':'ja-Hrkt'})
    rg.setData(RelatedInstanse,'dcndl:titleTranscription',row['翻字タイトル @ja-Latn'],attrib={'xml:lang':'ja-Latn'})
    rg.setData(RelatedInstanse,'rcgs:parallelTitle',row['並列タイトルA'])
    rg.setData(RelatedInstanse,'rcgs:parallelTitle',row['並列タイトルB'])
    rg.setData(RelatedInstanse,'rcgs:parallelTitle',row['並列タイトルC'])
    rg.setData(RelatedInstanse,'rcgs:parallelTitle',row['並列タイトルD'])
    rg.setData(RelatedInstanse,'rcgs:variantTitle',row['異形タイトル A'])
    rg.setData(RelatedInstanse,'rcgs:variantTitle',row['異形タイトル B'])
    rg.setData(RelatedInstanse,'rcgs:abbreviatedTitle',row['省略タイトル'])
    rg.setData(RelatedInstanse,'rcgs:responsibilityStatement',row['責任表示'])
    rg.setData(RelatedInstanse,'dcterms:creator',attrib={'rdf:resource':row['創作者A']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(RelatedInstanse,'dcterms:creator',attrib={'rdf:resource':row['創作者B']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(RelatedInstanse,'dcterms:creator',attrib={'rdf:resource':row['創作者C']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(RelatedInstanse,'dcterms:contributor',attrib={'rdf:resource':row['貢献者A']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(RelatedInstanse,'dcterms:contributor',attrib={'rdf:resource':row['貢献者B']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    rg.setData(RelatedInstanse,'dcterms:contributor',attrib={'rdf:resource':row['貢献者C']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
    if not rg.isNullData([row['キャリア種別 メインユニット'],row['数量 メインユニット'],row['大きさ メインユニット']]):
        Format=ET.SubElement(RelatedInstanse,'dcterms:format')
        MediaTypeOrExtent_Format = ET.SubElement(Format,'dcterms:MediaTypeOrExtent')
        rg.setData(MediaTypeOrExtent_Format,'dc:type',attrib={'rdf:resource':row['キャリア種別メインユニット統制語彙::URI']})
        rg.setData(MediaTypeOrExtent_Format,'dc:extent',row['数量 メインユニット'])
        rg.setData(MediaTypeOrExtent_Format,'rcgs:dimension',row['大きさ メインユニット'])
    if not rg.isNullData([row['キャリア種別 サブユニット'],row['数量 サブユニット'],row['大きさ サブユニット']]):
        FormatOfSubunit=ET.SubElement(RelatedInstanse,'rcgs:formatOfSubunit')
        MediaTypeOrExtent_FormatOfSubunit = ET.SubElement(FormatOfSubunit,'dcterms:MediaTypeOrExtent')
        rg.setData(MediaTypeOrExtent_FormatOfSubunit,'dc:type',attrib={'rdf:resource':row['キャリア種別サブユニット統制語彙 2::URI']})
        rg.setData(MediaTypeOrExtent_FormatOfSubunit,'dcterms:extent',row['数量 サブユニット'])
        rg.setData(MediaTypeOrExtent_FormatOfSubunit,'rcgs:dimension',row['大きさ サブユニット'])
    rg.setData(RelatedInstanse,'dcterms:medium',attrib={'rdf:resource':row['素材統制語彙 A::URI']})
    rg.setData(RelatedInstanse,'dcterms:medium',attrib={'rdf:resource':row['素材統制語彙 B::URI']})
    rg.setData(RelatedInstanse,'dcterms:medium',attrib={'rdf:resource':row['素材統制語彙 C::URI']})
    rg.setData(RelatedInstanse,'dcterms:medium',attrib={'rdf:resource':row['素材統制語彙 D::URI']})
    rg.setData(RelatedInstanse,'dcterms:medium',attrib={'rdf:resource':row['素材統制語彙 E::URI']})
    rg.setData(RelatedInstanse,'dcterms:medium',attrib={'rdf:resource':row['素材統制語彙 F::URI']})
    rg.setData(RelatedInstanse,'dcterms:medium',attrib={'rdf:resource':row['素材統制語彙 G::URI']})
    rg.setData(RelatedInstanse,'schema:gtin13',row['GTIN A'])
    rg.setData(RelatedInstanse,'schema:gtin13',row['GTIN B'])
    rg.setData(RelatedInstanse,'schema:gtin13',row['GTIN C'])
    rg.setData(RelatedInstanse,'schema:isbn',row['ISBN'])
    rg.setData(RelatedInstanse,'schema:issn',row['ISSN'])
    rg.setData(RelatedInstanse,'rcgs:modelNumber',row['型番 A'])
    rg.setData(RelatedInstanse,'rcgs:modelNumber',row['型番 B'])
    rg.setData(RelatedInstanse,'rcgs:jpNumber',row['全国書誌番号'])
    rg.setData(RelatedInstanse,'rcgs:ndlBiBID',row['国立国会図書館書誌ID'])
    rg.setData(RelatedInstanse,'rcgs:oclcNumber',row['OCLCナンバー'])
    rg.setData(RelatedInstanse,'schema:copyrightYear',row['著作権年'])
    rg.setData(RelatedInstanse,'dcterms:accessRights',row['アクセス制限'])
    rg.setData(RelatedInstanse,'dcterms:hasPart',attrib={'rdf:resource':row['関連(hasPart) A']})
    rg.setData(RelatedInstanse,'dcterms:hasPart',attrib={'rdf:resource':row['関連(hasPart) B']})
    rg.setData(RelatedInstanse,'dcterms:hasPart',attrib={'rdf:resource':row['関連(hasPart) C']})
    rg.setData(RelatedInstanse,'dcterms:description',row['説明(description)'])
    rg.setData(RelatedInstanse,'dcterms:language',attrib={'rdf:resource':row['言語URI A']})
    rg.setData(RelatedInstanse,'dcterms:language',attrib={'rdf:resource':row['言語URI B']})
    rg.setData(RelatedInstanse,'dcterms:language',attrib={'rdf:resource':row['言語URI C']})
    rg.setData(RelatedInstanse,'dcterms:source',row['出典'])
    if row['クラス種別']=='rcgs:InstanceProductType':
        rg.setData(RelatedInstanse,'dcndl:edition',row['エディションA'])
        rg.setData(RelatedInstanse,'dcndl:edition',row['エディションB'])
        rg.setData(RelatedInstanse,'dcndl:edition',row['エディションC'])
        rg.setData(RelatedInstanse,'schema:brand',row['ブランド'])
        if not rg.isNullData([row['出版者名'],row['出版日正規化'],row['出版日取得元'],row['出版地']]):
            ProvisionActivity = ET.SubElement(RelatedInstanse,'rcgs:provisionActivity')
            Publication = ET.SubElement(ProvisionActivity,'rcgs:Publication')
            rg.setData(Publication,'dc:publisher',row['出版者名'])
            rg.setData(Publication,'dcterms:date',row['出版日正規化'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
            rg.setData(Publication,'dcterms:source',row['出版日取得元'],pretxt='Data from ')
            rg.setData(Publication,'dcterms:spatial',row['出版地'])
        if not rg.isNullData([row['頒布者名'],row['頒布日正規化'],row['頒布日取得元'],row['頒布地']]):
            ProvisionActivity = ET.SubElement(RelatedInstanse,'rcgs:provisionActivity')
            Distribution = ET.SubElement(ProvisionActivity,'rcgs:Distribution')
            rg.setData(Distribution,'dc:publisher',row['頒布者名'])
            rg.setData(Distribution,'dcterms:date',row['頒布日正規化'],attrib={'rdf:datatype':'http://purl.org/dc/terms/W3CDTF'})
            rg.setData(Distribution,'dcterms:source',row['頒布日取得元'],pretxt='Data from ')
            rg.setData(Distribution,'dcterms:spatial',row['頒布地'])
        rg.setData(RelatedInstanse,'rcgs:publisher',attrib={'rdf:resource':row['出版者']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
        rg.setData(RelatedInstanse,'rcgs:distributor',attrib={'rdf:resource':row['頒布者']},pretxt='https://collection.rcgs.jp/s/rcgs/resource/')
        chars = ['A','B','C']
        for char in chars:
            if not rg.isNullData([row['シリーズ本タイトル '+char]]):
                if not rg.isNullData([row['シリーズ内ナンバー '+char]]):
                    rg.setData(RelatedInstanse,'rcgs:seriesStatement',row['シリーズ本タイトル '+char]+' ; '+row['シリーズ内ナンバー '+char])
                else:
                    rg.setData(RelatedInstanse,'rcgs:seriesStatement',row['シリーズ本タイトル '+char])
        for char in chars:
            if not rg.isNullData([row['サブシリーズ本タイトル '+char]]):
                if not rg.isNullData([row['サブシリーズ内ナンバー '+char]]):
                    rg.setData(RelatedInstanse,'rcgs:subseriesStatement',row['サブシリーズ本タイトル '+char]+' ; '+row['サブシリーズ内ナンバー '+char])
                else:
                    rg.setData(RelatedInstanse,'rcgs:subseriesStatement',row['サブシリーズ本タイトル '+char])
        rg.setData(RelatedInstanse,'rcgs:modeOfIssuance',attrib={'rdf:resource':row['刊行方式統制語彙::URI']})
        rg.setData(RelatedInstanse,'dcndl:publicationPeriodicity',attrib={'rdf:resource':row['刊行頻度統制語彙::URI']})
        rg.setData(RelatedInstanse,'schema:serialNumber',row['シリアルナンバー'])
        rg.setData(RelatedInstanse,'schema:price',row['入手条件 価格'])
        rg.setData(RelatedInstanse,'schema:downloadUrl',row['URL'])
        rg.setData(RelatedInstanse,'dcterms:tableOfContent',row['サブユニットリスト'])
        rg.setData(RelatedInstanse,'rcgs:digitalFileType',attrib={'rdf:resource':row['デジタルファイル種別統制語彙 2::URI']})
    # if index==20:
        # break
    # print(rg.prettify(RDF))
with open(outputFileName,"w",encoding="utf_8") as f:
    f.write(rg.prettify(RDF))
rg.validator(outputFileName) ##バリデーションチェック
