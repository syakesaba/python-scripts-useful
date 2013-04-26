import numpy

try:
    import completer
except:
    pass

def randmatrix(row=0,col=0):
    row=round(row)
    col=round(col)
    if row == 0:row=2
    if col == 0:col=2
    return numpy.matrix([[numpy.random.random() for j in range(col)] for i in range(row)])

def difcost(a,b):
    """
    a,b=matrix
    a及びbはおなじ行数、列数でなければならない。
    difcost ---残差平方和---
      a       b                           dif
    ([1,2]   ([5,6] => ([(1-5)^2,(2-6)^2] => ([16,16]
     [3,4])   [7,8])    [(3-7)^2,(4-8)^2])    [16,16])
    """
    dif=0
    for i in range(numpy.shape(a)[0]):
        for j in range(numpy.shape(a)[1]):
            dif+=numpy.square(a[i,j]-b[i,j])
    return dif

def factorize(v,pc=10,iter=50):
    """
    {オライリー本
    「集合知プログラミング」より}
    
    v=因子分解するデータ行列（行＝テストケースの番号、列＝テスト結果得るデータたちの番号）
    pc=因子の数
    iter=更新回数

    vのﾌｫｰﾏｯﾄ～
    array(No1,No2.....) = 記事ナンバー？テストケースナンバー？
    array(value1,value2.....) = 記事の単語たち　テストケースの結果たち
    data=matrix([No1.value1.times,No1.value2.times,....]
                [No2.value1.times,No2.value2.times,....])
    すべて正の値でなければならない（非負値因子分解）
    ～～～～～～
    factorize(data,)
    """
    #行列なので、掛け算には順序があります
    
    w=numpy.randmatrix(int(numpy.shape(v)[0]),pc)#vの行数×pc のランダム行列wを生成（初期重み） 
    #テストケース番号毎の各因子の重み
    h=numpy.randmatrix(pc,int(numpy.shape(v)[1]))#pc×vの列数 のランダム行列hを生成（初期特徴）
    #テストケース結果毎の持つ因子
    
    #乗法的更新ルール(勾配降下法)
    for i in range(iter):#iter回ループ
        wh=w*h#重み*特徴
        cost=numpy.difcost(v,wh)#目的行列との距残差平方和を計算
        #if i%10==0:print(cost)#10回毎に距残差平方和を表示する
        if cost==0:break#距残差平方和が0なら目的変数と完全に合致、完全な因子w,hを発見
        h=numpy.matrix(numpy.array(h)*numpy.array(w.T*v)/numpy.array(w.T*w*h))
        #行列H=配列計算{配列(H)*配列(行列計算(w.T*v))/配列(行列計算(w.T*w*h))}
        w=numpy.matrix(numpy.array(w)*numpy.array(v*h.T)/numpy.array(w*h*h.T))
        #行列W=配列計算{配列(w)*配列(行列計算(v*h.T))/配列(行列計算(w*h*h.T))}
    #}
    return w,h

def showfeatures(w,h,titles,wordvec):#(w,h,titles,wordvec,out="filename")
    pc,wc=numpy.shape(h)
    toppatterns=[ [] for i in range(len(titles))]#題名の分だけ[[],...]
    
    for i in range(pc):#因子の数だけ繰り返し
        slist=[]
        for j in range(wc):#重み回
            slist.append((h[i,j],wordvec[j]))
        slist.sort()#整列し
        slist.reverse()#降順にする
        top5w=[s[1] for s in slist[0:5]]#値が上位5位の重みを抽出["","",""]
        #for k in range(5):
        #    print("%s位：%s" % (str(k+1),top5w[k]))#上位5位を書き込み
        flist=[]
        for j in range(len(titles)):#記事のタイトルの数
            flist.append((w[j,i],titles[j]))#該当する重みに対応する記事のタイトルを結合する
            toppatterns[j].append((w[j,i],i,titles[j]))#
        flist.sort()
        flist.reverse()
        
        #for f in flist[0:3]:
        #    print(str(f))
        return toppatterns,top5w

def test():
    for i in range(10):
        print()
    a=numpy.randmatrix(5,5)
    b=numpy.randmatrix(5,5)#10個の
    print("a*b=",str(a*b))
    w,h=numpy.factorize(a*b)
    print("w*h",str(w*h))
    print("誤差：" + str(numpy.difcost(a*b,w*h)))
    titles,words = numpy.showfeatures(w,h,\
    ["Google","Microsoft","Twitter","Codepad","Skype"],\
    [\
    [0,5,2,0],\
    [5,2,2,0],\
    [0,1,0,5],\
    [2,2,5,2],\
    [0,2,0,5],\
    ])
    #5社
    #PC,Search,Programming,Talk
    print("PC,Search,Programming,Talk")
    for title,word in zip(titles,words):
        print(title,word)

numpy.残差平方和=numpy.difcost=difcost
numpy.因子分解=numpy.factorize=factorize
numpy.ランダム行列=numpy.randmatrix=randmatrix
numpy.因子分析結果=numpy.showfeatures=showfeatures
numpy.factorize.test=test
test()
