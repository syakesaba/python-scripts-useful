#!/usr/bin/env python3
# encoding: utf-8

夢=理想=None # python3スクリプトです。 python3 で実行してください。

成功=True
失敗=False
例外=Exception

無=0
小=1
中=2
大=3

上回る=lambda こっち,あっち:int(こっち>あっち)
同等=0

class どうしようもないわエラー(例外):
    def __str__(これ):
        return "これどうしようもないわ"

class 人間:
    def __init__(自分,外見,心=None):
        自分.外見的魅力=外見
        del 心
    @property
    def 魅力(自分):
        return 自分.外見的魅力
    def 出会い(自分,相手):
        if 自分.魅力 > 無:
            return 成功
        return 失敗
    def 恋愛(自分,相手):
        if 上回る(自分.魅力,相手.魅力) >= 同等:
            return 成功
        return 失敗
    def 結婚(自分,相手):
        if 上回る(自分.魅力,相手.魅力) > 同等:
            return 成功
        return 失敗

class 男(人間):
    def __init__(自分,遺伝子):
        人間.__init__(自分,遺伝子)
        pass

class 女(人間):
    def __init__(自分,遺伝子):
        人間.__init__(自分,遺伝子)
        pass

俺=男(12)

def 人生における人との出会い():
    yield 女(15)
    yield 男(120)
    yield 女(12.1)
    yield 女(12)
    yield 女(100)
    yield 男(120)
    yield 女(110)
    #yield 女(0.1)

for 人 in 人生における人との出会い():
    if isinstance(人,男):
        continue
    女性=人
    if 俺.出会い(女性) == 成功:
        if 俺.恋愛(女性) == 成功:
            if 俺.結婚(女性) == 成功:
                print("カップリング成功。相手の女性の魅力 = " + str(女性.魅力))
                exit(-1)

raise どうしようもないわエラー()
