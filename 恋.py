#!/usr/bin/env python3
# encoding: utf-8

いない=ない=None # python3スクリプトです。

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
    def __init__(自分,遺伝子):
        自分.魅力=遺伝子
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

俺=人間(12)
def 人生における女との出会い():
    yield 人間(15)
    yield 人間(120)
    yield 人間(13)
    yield 人間(12.1)

for 女 in 人生における女との出会い():
    if 俺.出会い(女) == 成功:
        if 俺.恋愛(女) == 成功:
            if 俺.結婚(女) == 成功:
                print("成功。女.魅力 = " + str(女.魅力))
                exit()

raise どうしようもないわエラー()


