0.はじめに
	readmeとして、RDF生成プログラム(RDFGenerator)の使い方を以下に記す。各種RDFGeneratorに共通する部分はライブラリとしてlibrary_rdfGen.pyにしている
	進捗状況メモのスプレッドシート：https://docs.google.com/spreadsheets/d/1yxfc_5KzVA83ARHuL05J_WiCnlC0nJmEqWmkeJs_zb0/edit?usp=sharing


1．対応表の作成
	ファイルメーカーでの値とRDFの要素名の対応表を作成する。
	対応表：https://docs.google.com/spreadsheets/d/1yxfc_5KzVA83ARHuL05J_WiCnlC0nJmEqWmkeJs_zb0/edit#gid=294723067
	福田さんが作成したDSPver1100.xlsxを参考に、対応を考えて表を作る。
	値制約が構造化の場合、rdf:resouceの属性値にURLを与える。
	例：dcterms:creatorの値制約は「構造化」で「foaf:Agent」なので、<dcterms:creator rdf:resouce="https://collection.rcgs.jp/s/rcgs/resource/AGENT00000">とする。
	この際、RDFに必要なデータがファイルメーカーのフィールドにない場合、レイアウトを編集してフィールドを適宜増やす(可能ならでいい)。
2．プログラムコード作成
	0．空白行のスキップ
		ファイルメーカーからCSVを吐き出すと、関係のないデータまで出ることがある(この辺よくわからない)
		そこで、レコードIDを参照して、その値持つ行だけを抽出している。
		コード：	if row['レコードID']=='':#空データのスキップ
        				continue
	1．IDの記述
		記述するWorkやPackage自体のレコードIDは最初に書く。属性は"rdf:about"で属性値がURL+レコードID
		コード：	Work = ET.SubElement(RDF,'rcgs:Work',attrib={'rdf:about':'https://collection.rcgs.jp/s/rcgs/resource/'+row['レコードID']})
		RDF　 ：	<rcgs:Work rdf:about="https://collection.rcgs.jp/s/rcgs/resource/WORK0000010">
	2．値参照＝文字列
		コード：	rg.setData(Work,'dc:type',row['形式'])
		RDF　 ：	<dc:type>video game</dc:type>
	3．値参照＝参照値
		attribに辞書型を与えると、key=属性名、value=属性値でRDFが生成される
		コード：	rg.setData(Work,'rcgs:mobyGames',attrib = {'rdf:resource':row['Mobygames Link']})
		RDF　 ：	<rcgs:mobyGames rdf:resource="https://www.mobygames.com/game/global-defence-force"/>
		コード：	rg.setData(Work,'skos:altLabel',row['その他のタイトル@en'],attrib={'xml:lang':'en'})
		RDF 　：	<skos:prefLabel xml:lang="en">Tomb Raider</skos:prefLabel>
	4．パーセントエンコード
		URL内に空白や”が含まれるとエラーになる。percentEncode関数を使うと、それらが％エンコードされる。
		コード：	rg.setData(Work,'rcgs:twitch',attrib = {'rdf:resource':rg.percentEncode(row['twitch Link'])})
		RDF　 ：	<rcgs:twitch rdf:resource="https://www.twitch.tv/directory/game/Myst%20III:%20Exile"/>
	5.接頭語追加
		pretxtにその要素の頭につけたい文字列を与えるとつけてくれる。
		コード：	rg.setData(Work,'skos:closeMatch',attrib = {'rdf:resource':row['Wikidata ID']},pretxt='https://www.wikidata.org/wiki/')
		RDF　 ：	<skos:closeMatch rdf:resource="https://www.wikidata.org/wiki/Q5570229"/>
3．バリデーション
	生成されたRDFが正しいかの確認を行う。以下のサイトに貼り付けることで確認ができる。RDFのサイズが大きくなるとエラーができるので最初は小さくして試す。
	最終的に出来上がったRDFは大きすぎて、下記のサイトでバリデーションできないので、validator関数を用いてバリデーションする。
	https://www.w3.org/RDF/Validator/
	コード：rg.validator(outputFileName) #バリデーションチェック
4．記録
	対応表のスプレッドシートにある、全体進捗にどこまで進んだかを記録する。問題点があれば記入する
