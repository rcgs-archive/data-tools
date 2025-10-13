import xml.etree.ElementTree as ET
import xml.dom.minidom as md
from rdflib import Graph

def prettify(elem): #xmlに改行を入れる
    string = ET.tostring(elem, 'utf-8')
    reparsed = md.parseString(string)
    return reparsed.toprettyxml(indent="  ")
def setData(parent,tag,text=None,attrib=None,pretxt=''):
    if text is None:
        if "" not in attrib.values():
            if r'\\' in ''.join(list(attrib.values())): #属性値内に\\を含むか判定
                ks_vs = separateData(attrib) #\\で分割 #このseparateData関数が汚すぎる.ごり押し
                for k,v in zip(ks_vs[0],ks_vs[1]):
                    element = ET.SubElement(parent,tag,attrib={k:v})
            else:
                if not pretxt=='':
                    newattrib = {}
                    for k,v in attrib.items():
                        if k=='rdf:resource':
                            v = v.replace('\n','')
                            v = v.replace(' ','')
                        v = pretxt+v
                        newattrib[k] = v
                    element = ET.SubElement(parent,tag,attrib=newattrib)
                else:
                    element = ET.SubElement(parent,tag,attrib=attrib)
    else:
        if not text=="":
            datas = text.split(r'\\')
            for data in datas:
                if attrib is not None:
                    element = ET.SubElement(parent,tag,attrib=attrib)
                    element.text = pretxt+data
                else:
                    element = ET.SubElement(parent,tag)
                    element.text = pretxt+data
def isNullData(data_lst):
    nullFlag = 1
    for data in data_lst:
        if not data == '':
            nullFlag = 0
    return nullFlag
def separateData(dic): #属性値内の\\に対する分割処理関数
    lst_v = []
    lst_k = []
    for k,v in dic.items():
        vs = v.split(r'\\')
        url = checkURL(vs[0])
        vs[0] = vs[0].replace(url,'')
        for data in vs:
            lst_v.append(url+data)
            lst_k.append(k)
    return lst_k,lst_v
def checkURL(data): #URLがつかない場合に対応する処理関数
    if 'https://www.metacritic.com/' in data:
        return 'https://www.metacritic.com/'
    elif 'https://www.mobygames.com/game/' in data:
        return 'https://www.mobygames.com/game/'
    elif 'https://www.imdb.com/title/' in data:
        return 'https://www.imdb.com/title/'
    else:
        return ''
def percentEncode(txt): #特殊記号はRDF内に記述できないので、パーセントエンコードに変換
    txt = txt.replace(' (invalid)','').replace(' (Invalid)','').replace(' <Invalid>','').replace(' <invalid>','').replace(' (Invaild)','').replace('[invalid]','').replace(']','').replace('[','')
    txt = txt.replace(' ','%20').replace(r'"','%22').replace(r'%','%25')
    txt = txt.replace('\n','')
    return txt
def validator(filename):
    g = Graph()
    g.parse(filename)
    print(filename+" Variating finish")
def makePrefix(elem):
    elem.set('xmlns:rdf','http://www.w3.org/1999/02/22-rdf-syntax-ns#')
    elem.set('xmlns:dcndl','http://ndl.go.jp/dcndl/terms/')
    elem.set('xmlns:dc','http://purl.org/dc/elements/1.1/')
    elem.set('xmlns:dcterms','http://purl.org/dc/terms/')
    elem.set('xmlns:schema','http://schema.org/')
    elem.set('xmlns:skos','http://www.w3.org/2004/02/skos/core#')
    elem.set('xmlns:rdfs','http://www.w3.org/2000/01/rdf-schema#')
    elem.set('xmlns:foaf','http://xmlns.com/foaf/0.1/')
    # elem.set('xmlns:omeka','http://omeka.org/s')
    elem.set('xmlns:rcgs','http://www.rcgs.jp/terms/')
