#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import httplib2 #http://code.google.com/p/httplib2/wiki/ExamplesPython3
from urllib.parse import urlencode
from xml.etree.cElementTree import XML
from html.parser import HTMLParseError
from Html import WCWebSearchParser
import time
class WorldCatSearch:
    """
    世界的な論文及び参考文献リポジトリ、WorldCatのAPIを試行するクラス。
    APIキーはOCLC(WorldcatAPI)から所得可能。
    ***リクエストの種類
    OpenSearch:http://oclc.org/developer/documentation/worldcat-search-api/opensearch
    SRU:http://oclc.org/developer/documentation/worldcat-search-api/sru
    Single Bibliographic Record:
    http://oclc.org/developer/documentation/worldcat-search-api/single-bibliographic-record
    Library Locations:
    http://oclc.org/developer/documentation/worldcat-search-api/library-locations
    Library Catalog URL for a Record:
    http://oclc.org/developer/documentation/worldcat-search-api/library-catalog-url
    Formatted-Citations:
    http://oclc.org/developer/documentation/worldcat-search-api/formatted-citations
    ***エラーの種類
    http://www.oclc.org/developer/documentation/worldcat-search-api/error-statuses

    """

    def __init__(self,APIkey,cache=False):#APIkeyはダミーでも可能です。ダミーの場合、WebSearchのみの対応となります
        """
        You need WorldCat APIKey
        From : https://worldcat.org/config/CreateAccountWizard.do
        """
        self.log = []
        self.wskey = APIkey
        self.cformat = ("apa","chicago","harvard","mla","turbian","all")
        self.http = httplib2.Http()
        if cache:
            self.http = httplib2.Http(cache)#cacheフォルダを作成、WEBキャッシュを格納します
        self.iswsKeyActive = self.isKeyActive()
        self.iswsKeySearchAPI = self.isKeySearchAPI()
        self.WebSearchParser = WCWebSearchParser()

    def checknums(self,count=10,start=1):
        if count > 100 or count < 0:raise Exception("100>=count>0")
        if start < 1:raise Exception("start>0")

    def isKeySearchAPI(self):
        try:
            headers,data = self.http.request(\
        "http://worldcat.org/webservices/catalog/search/sru?q=srw.kw%3D%22NURUPO%22&wskey=" + self.wskey,\
        "GET")
        except:
            raise Exception("Connected to the Internet?Is really valid APIkey?")
        self.log.append("http://worldcat.org/webservices/catalog/search/opensearch?q=NURUPO&wskey=" + self.wskey)
        if "Unsupported operation" in data.decode():
            return False
        return True

    def isKeyActive(self):
        try:
            headers,data = self.http.request(\
        "http://worldcat.org/webservices/catalog/search/opensearch?q=NURUPO&wskey=" + self.wskey,\
        "GET")
        except:
            raise Exception("インターネットに繋がらない,もしくはAPIキーに不正な文字が入っている")
        self.log.append("http://worldcat.org/webservices/catalog/search/opensearch?q=NURUPO&wskey=" + self.wskey)
        if headers["status"] != "200":
            return False
        return True

    def stripHTMLTags(self,data):
        p=""
        s=False
        for c in data:
            if c=="<":
                s=True
            elif c==">":
                s=False
                p = p + " "
            elif s is False:
                p= p + c
        return p

    def OpenSearch(self,
        q,
        format="atom",
        start=1,
        count=10,
        cformat="mla"):
        """
        WorldCat Basic/Search API用。
        いわゆる普通の検索.XMLで帰ってきます
        q=検索キーワード。必須
        format=[rss|atom] デフォはatom形式のXML。任意
        start=何番目の文献から出力するか。デフォは1 任意
        count=何個の文献を一度に出力するか(100個まで)。デフォは10　任意
        cformat=文献の概要の表示形式。[apa|chicago|harvard|mla|turbian|all] デフォはmla　任意
        wskey=APIキー。　必須
        例：
        >>import search
        >>test = search.WorldCatSearch("APIキー")
        >>h,d=test.OpenSearch("文章のタイトルや著者の名前など、キーワード")
        >>hits,data=test.parseOpenSearch(d)
        >>data[0]["title"] <=1件目、題名
        >>data[1]["name"] <=2件目、著者名
        >>data[0]["identifier2"] <=1件目、本の2個目のISBN（ISSN）
        """
        if self.iswsKeyActive is not True:
            raise Exception("Your API Key doesn't work")
        self.checknums(count=count,start=start)
        if cformat not in self.cformat:
            raise Exception("cformat:%s" % str(self.cformat))
        if format not in ("rss","atom"):
            raise Exception("format:%s ? 'rss' or 'atom' please" % format)
        uri="http://worldcat.org/webservices/catalog/search/opensearch?" + \
        urlencode({"q":q,"format":format,"start":start,"count":count,"cformat":cformat,"wskey":self.wskey})
        headers,data = self.http.request(uri,"GET")
        self.log.append(uri)
        return headers,data

    def parseOpenSearch(self,xmldata,format="atom"):
        """
        OpenSearchの出力XMLをパースします。
        xmldata=OpenSearch("keyword")[1]
        format=atomまたはrss
        """
        root=XML(xmldata)#xmldata
        if format == "rss":
            entrys=[elm for elm in root.getchildren()[0].getchildren() if "item" == elm.tag]
        elif format == "atom":
            entrys=[elm for elm in root if elm.tag.endswith("entry")]
        else:
            raise Exception("Unknown format : %s" % format)#xmlのフォーマットはatom/rssのみ対応
        hits=len(entrys)
        entrys=[entry.getiterator for entry in entrys]
        entrys=[j for j in [i() for i in entrys]]
        ret=[]
        h="content"
        for entry in entrys:
            buf={}
            for val in entry:
                dual=1
                if val != None and val.text != None:
                    if not val.text.startswith("\n"):
                        if buf.get(val.tag[val.tag.find("}")+1:]) == None:
                            buf[val.tag[val.tag.find("}")+1:]] = val.text
                        else:
                            dual= dual+1
                            buf[val.tag[val.tag.find("}")+1:] + str(dual)] = val.text
            if h in buf.keys():buf[h]=self.stripHTMLTags(buf[h])
            ret.append(buf)
        return hits,ret#data[0]["name"] で著者

    def SRU(self,
        query,
        recordSchema="info:srw/schema/1/marcxml",
        startRecord=1,
        maximumRecords=10,
        sortKeys="relevance",
        frbrGrouping="off",
        servicelevel="default"):
        """
        WorldCat Search API専用.　信頼された組織の認証を受けないとAPIキー認証されません
        query=CQLクエリ。必須。http://www.worldcat.org/webservices/catalog/
        recordSchema=出力フォーマット MARC XML(info%3Asrw%2Fschema%2F1%2Fmarcxml)か
        Dublin Core(info%3Asrw%2Fschema%2F1%2Fdc)が選べる。デフォはMARC XML。任意。

        startRecord=何番目の文献から出力するか。デフォは1 任意
        maximumRecords=何個の文献を一度に出力するか(100個まで)。デフォは10　任意
        sortKeys=なにでソートするか。（relevance, Title, Author, Date, Library Count,Score)デフォはrelevance。任意
        並びはデフォで昇順。降順にする場合、「,,0」をsortKeysに追加すること。スペースを間に入れてソートを複数かけることができます。
        frbrGrouping=[on|off].FRBRグルーピング(最も近い著作のみをグループ毎に代表して出力するか否か。任意。デフォoff。
        servicelevel=[default|full].任意。デフォはdefault
        """

        if self.iswsKeyActive is not True:
            raise Exception("Your API Key doesn't work")
        if self.iswsKeySearchAPI is not True:
            raise Exception("Your API Key is not WCSearchAPI(Basic API is only for OpenSearch)")
        self.checknums(start=startRecord,count=maximumRecords)
        uri="http://worldcat.org/webservices/catalog/search/sru?" + \
        urlencode({
        "query":query,
        "recordSchema":recordSchema,
        "startRecord":startRecord,
        "maximumRecords":maximumRecords,
        "sortKeys":sortKeys,
        "wskey":self.wskey})
        headers,data = self.http.request(uri,"GET")
        self.log.append(uri)
        if "**SearchAPI無いの・・・誰か教えて" in data.decode():#CQLクエリがどっかおかしい時表示される文字
            raise Exception("invalid CQL Query")
        return headers,data

    def WebSearch(self,kw="",no="",
            au="",co="",bn="",
            n2="",ln="",pn="",
            pl="",pb="",se="",
            sn="",su="",ti="",
            yrf="0",yrt="3000",
            limit3mt=" ",limit4mt=" ",
            limit5mtx0=" ",limit6ln=" ",count=10):
        """
        Worldcat API key不要.HTMLで返します.
        ----------1個以上３個以下
        kw=キーワード
        no=Accession number
        au=著者名
        co=組織名
        bn=ISBN
        n2=ISSN
        ln=言語のフレーズ
        pn=個人名
        pl=出版された場所
        pb=出版社
        se=シリーズ
        sn=シリーズナンバー
        su=サブタイトル
        ti=タイトル
        ----------以下任意
        yrf,yrt=出版～絶版年の範囲指定、yrf年からyrt年まで 例：yrf=1990,yrt=2000
        limit3mt=子供向けかどうか 半角スペースで両方,mt:juvで子供,-mt:juvで大人
        limit4mt=文書の種類。半角スペースでany,mt:ficで小説・物語,-mt:ficでレポートなどノンフィクション,
                    mt:bioで個人伝記,mt:degで"論文,mt:msrで音楽レコード,mt:nsrで非音楽レコード
        limit5mtx0=文書形式。半角スペースでALL,x0:archvでアーカイブ,x0:artchapで著作品
                    　x0:audiobookで本（オーディオ）,x0:bookで本,
                    　x0:compfileで電子文書,x0:mapで地図
                    　x0:musicで歌詞,x0:msscrで楽譜,
                    　x0:newsでニュース記事,(x0:web | x4:digital)でHTML,
                    　(x0:snd | x0:audiobook | x0 music)で音楽関連
                    　x0:gameでゲーム,x0:visで視覚資料,
                    　x0:imageで画像,x0:image + x4:2dでダウンロード可能な画像,
                    　x0:videoで動画,x0:video + x4:dvdでDVD,
                    　x0:vis + x4:digitalでダウンロード可能な動画
                    　x0:book + x4:largeprintで大型の本
                    　x0:book + x4:digitalで電子書籍
        limit6ln=文書の言語。半角スペースでALL,ln:<言語>でその言語の文書のみ表示
                <言語> ::= [ara|nul|chi|scr|cze|dan|dut|eng|
                       fre|ger|gre|heb|hin|ind|ita|jpn|
                       kor|lat|nor|per|pol|por|rum|rus|
                       spa|swe|tha|tur|ukr|other]
        """
        k=0
        wds={0:"kw",1:"ti",2:"au",3:"co",4:"bn",5:"n2",6:"ln",
        7:"pn",8:"pl",9:"pb",10:"se",11:"sn",12:"su",13:"no"}
        #Priorities are kw>ti>au>....>no
        s = ["","",""]
        i = ["","",""]
        for m,text in enumerate([kw,ti,au,co,bn,n2,ln,pn,pl,pb,se,sn,su,no]):
            if k == 3:
                print("[*]Passed:%s" % wds[m])
                pass
            if text != "":
                s[k] = wds[m]
                i[k] = text
                k= k+1
        if k == 0:
            raise Exception("引数になんか入れて")
        searchN = {}
        while k > 0:
            k = k - 1
            searchN.update({"search%s" % str(k+1):"idx_%s" % s[k],"i%s" % str(k+1):i[k]})
        requestRing={
        "qt":"advanced","dblist":"239",
        "yrf":yrf,"yrt":yrt,    "limit-3-mt":limit3mt,"limit-4-mt":limit4mt,
        "limit-5-mt-x0":limit5mtx0,"limit-6-ln":limit6ln}
        requestRing.update(searchN)
        uri="http://oaister.worldcat.org/search?" + urlencode(requestRing)
        self.log.append(uri)
        headers,data = self.http.request(uri,"GET")
        h=headers
        start = 11
        print("%sページ目読み込み終了。" % str(int(start/10)))
        data=[data]
        count = int(count / 10) * 10
        if count > 0 and count < 4991:
            d=data[0]
            while start < count and "menuElem" in d.decode():
                uri=headers["content-location"] + "&start=%s" % str(start)
                self.log.append(uri)
                h,d = self.http.request(uri,"GET")
                data.append(d)
                start +=10
                print("%sページ目読み込み終了。" % str(int(start/10)))
                #time.sleep(5)
        self.WebSearchParser.close()
        for htmlpage in data:
            htmlpage=bytes(htmlpage)
            self.WebSearchParser.feed(htmlpage.decode())
        self.WebSearchParser.compResult()
        return len(data),len(self.WebSearchParser.results)#pages,hits

#以下デバッグ用
if __name__ == "__main__":
    WCSearch = WorldCatSearch("")
    #            　　　↑
    #            ここにAPIキーを入力しなさい！
    #
    #
    #
    print("Does the APIKey work?: " + str(WCSearch.iswsKeyActive) )
    print("Is the APIKey SearchAPI?: " + str(WCSearch.iswsKeySearchAPI))
    if 1==1:
        import completer
        print("[*]WebSearch(return pages,hits)")
        page,hit=WCSearch.WebSearch(
                kw=input("キーワード?"),count=int(input("何件くらいまで検索したい？")),su=input("サブタイトル?"),
                ti=input("タイトル?"),au=input("著作者?"),
                co=input("組織名?"),bn=input("ISBN?"),
                n2=input("ISNN?"),ln=input("言語?"),
                pn=input("固有名詞?"),pl=input("地域?"),
                pb=input("出版社?"),se=input("シリーズ?"),
                sn=input("シリーズナンバー?"),no=input("アクセスナンバー?"),
                yrf=input("何年から?"),yrt=input("何年まで?"),
                limit3mt=" ",limit4mt=" ",
                limit5mtx0="x0:compfile",limit6ln=" ")#5=x0:compfile to ダウンロードファイル
        for line in WCSearch.WebSearchParser.results:
            print("\n題名:",line["title"],"\n著者:",line["author"],"\n出版:",line["publisher"],"\n形式:",line["type"])
        print()
        print(page,"ページ、",hit,"ヒット")
    if 1==2:
        import completer
        #-----------
        print("[*]OpenSearch(return h,d)")
        q = input("opensearch keyword?")
        c = input("how many results do you want?")
        if c == "":c=10
        h,d = WCSearch.OpenSearch(q,count=int(c))
        print("HTTP STATUS %s" % h["status"])
        hit,data=WCSearch.parseOpenSearch(d)
        print("%shits:" % str(hit))
        for d in data:
            print(d)
            print()
        exit("OpenSearchDEMO")
    #-----------
