from html.parser import HTMLParser#http://www.python.jp/doc/2.4/lib/module-HTMLParser.html
#From http://d.hatena.ne.jp/yumimue/20080206/1202309902
class WCWebSearchParser(HTMLParser):
    """
    WorldCatの一般（APIキー不要）Webサーチした結果から該当する文献データだけを取り出します
    ... => NOread!
    <tr class="menuElem"> => OKhit!----
    ... =>NOread!
    <strong>著作名</strong> =>OKRead!
    ... => NOread!
    <div class="author">著作者名</div> =>OKRead!
    ... => NOread!
    <span class="itemType">文献のタイプ</span> => OKRead!
    ...=> NOread!
    <span class="itemPublisher">出版元</span> => OKRead!
    ...=> NOread!
    </tr> => NO hit!----
    ... =>NORead!
    例：
    my=WCWebSearchParser(HTMLソース)
    my.compResult()
    for ky in my.kys:
        for record in my.results:
            print(record[ky],end=" ")
        print()
    
    レコードのカタチ→{"title":タイトル,"author":著作者,"type":文献のタイプ,"publisher":出版元(大学名とか)}
    """
    def __init__(self,str_html="<html><body></body></html>"):
        HTMLParser.__init__(self)
        self.results = []
        self.kys=["title","author","type","publisher"]
        self.hit=False
        self.hits=0
        self.itsOK = False
        self.key="No match"
        self.feed(str_html)#このfeed関数は自身をresetするので、最後にfeedすることでインスタンス変数が消滅するのを回避する
    def OKRead(self):
        self.itsOK = True
    def NORead(self):
        self.itsOK = False
    def handle_starttag(self, tag, attrs):#開始タグtr(class=menuElm)を見つける
        if self.hit is True:
            self.collect(tag,attrs)#該当行であれば条件分岐へ突入
        else:
            if tag == "tr":# タグ、属性名は全て小文字
                attrs = dict(attrs)#((属性名, 値), ...) => {属性名:値, ...}
                if "class" in attrs:
                    if "menuElem" == attrs["class"]:#該当行の先頭まで移動
                        self.hit=True
                        self.results.append({})
    def handle_endtag(self, tag): # menuElm終了タグtrを見つけた場合の処理
        if self.hit is True:
            if tag == "tr":
                self.hit = False
                self.hits=self.hits+1

    def handle_data(self,data): # 開始・終了タグに囲まれた中身の処理
        if self.itsOK is True:
            #print(self.key + " " + data + " " + str("\n" in data))
            if "\n" not in data:
                if self.key in self.results[self.hits].keys():
                    self.results[self.hits][self.key] += data 
                self.results[self.hits].update({self.key:data})

    def collect(self,tag,attrs):
            self.NORead()
            if tag == "strong":#タイトルをげっと
                self.key="title"
                self.OKRead()
            if tag == "div":#著者名をげっと
                attrs=dict(attrs)
                if "class" in attrs:
                    if attrs["class"] == "author":
                        self.key="author"
                        self.OKRead()
            if tag == "span":#文献のタイプをげっと
                attrs = dict(attrs)
                if "class" in attrs:
                    if attrs["class"] == "itemType":
                        self.key="type"
                        self.OKRead()
                    if attrs["class"] == "itemPublisher":#出版元（無い場合アリ）をげっと
                        self.key="publisher"
                        self.OKRead()
    def compResult(self):
        for ky in self.kys:
            for no in [x for x in self.results if ky not in x.keys()]:
                no[ky] = "NoData"
