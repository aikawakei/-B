#wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ja.300.vec.gz
import gensim
import torch
import itertools
from einops import rearrange
import numpy as np
import pickle

class Word2Vec:
    '''
    初期化に5分ほどかかると思われます。
    使う関数はtopicsです。
    '''
    def __init__(self):
        
        self.model = gensim.models.KeyedVectors.load_word2vec_format('cc.ja.300.vec.gz', binary=False)
 
    def subject_step(self,p,n,topn):
        words=[]
        print(p)
        print(n)
        print(topn)
        try:
            lis_tup=self.model.most_similar(positive=p,negative=n,topn=topn)
            for tup in lis_tup:
                words.append(tup[0])
        except KeyError:
            p=list(p)
            for i in range(len(p)):
                if not p[i] in self.model:
                    p[i]='趣味'
            lis_tup=self.model.most_similar(positive=p,negative=n,topn=topn)
            for tup in lis_tup:
                words.append(tup[0])
        return words

    def subject_loop(self,p,n,topn,steps=1):
        for i in range(steps):
            p=self.subject_step(p,n,topn)
        return p

    def p_pairs(self,p):
        return list(itertools.combinations(p,2))

    def clean_up(self,words):
        topic=[]
        for word in words:
            if (word in topic):
                continue
            topic.append(word)
        return topic

    def topics(self,p,n=("None","none"),topn=9):
        """
        p: 単語のリスト（日本語）を入力
        n: 単語ベクトルのマイナスしたいもの。defaultはNone
        topn: 数が大きい方が出力単語数が増える。defaultは7
        出力:類似単語のリスト
        """
        pairs=self.p_pairs(p)
        topics=[]
        for pair in pairs:
          topics.append(self.subject_loop(pair,n,topn))
        print(topics)

a=Word2Vec()
#メイン
b=('センター','収容','譲')
a.topics(b)
b=('以外','動物','譲')
a.topics(b)
b=('寄付','寄附','基金')
a.topics(b)
b=('センター','見学','自由')
a.topics(b)
b=('センター','墓','死亡')
a.topics(b)
b=('センター','供養','死亡')
a.topics(b)
b=('センター','ボランティア','できる')
a.topics(b)
b=('働く','採用','ページ')
a.topics(b)
b=('学校','授業','いのち')
a.topics(b)
b=('課題','卒論','取材')
a.topics(b)
b=('迷子','自宅','保護')
a.topics(b)
b=('自宅','保護','飼う')
a.topics(b)
b=('野良猫','被害','捕獲')
a.topics(b)
b=('犬','放し飼い','鳴き声')
a.topics(b)
b=('動物','虐待','見る')
a.topics(b)
b=('犬','かむ', 'どうしたら')
a.topics(b)
b=('サル','ヘビ','ワニ')
a.topics(b)
b=('病気','ケガ','野生')
a.topics(b)
b=('神奈川','野犬','いる')
a.topics(b)
b=('猫','室内','飼う')
a.topics(b)
b=('野良猫','エサ','よい')
a.topics(b)
b=('飼う','動物','逃げる')
a.topics(b)
b=('収容','写真','自分')
a.topics(b)
b=('犬','観察','取る')
a.topics(b)
b=('犬','しつけ','相談')
a.topics(b)
b=('動物','飼う','引き取り')
a.topics(b)
b=('飼い犬','人','かむ')
a.topics(b)
b=('飼う','亡くなる','死体')
a.topics(b)
b=('病気','獣医','死')
a.topics(b)
b=('ペット','ブリーダー','選ぶ')
b=('マイクロ','義務','どのような')
a.topics(b)
b=('飼育','愛護','法律')
a.topics(b)
b=('野良猫','エサ','いなくなる')
a.topics(b)
b=('留守','時間','どのくらい')
a.topics(b)
b=('保護','譲り受ける','譲渡金')
a.topics(b)
b=('適正','評価','なぜ')
a.topics(b)
b=('犬','登録','予防')
a.topics(b)
b=('しつけ','いつ','始める')
a.topics(b)
b=('保護','迷う','どうなる')
a.topics(b)
b=('保護','ショップ','病気')
a.topics(b)
b=('場所','どこ','ある')
a.topics(b)
b=('エサ','いくら','かかる')
a.topics(b)
b=('特定','数','種類')
a.topics(b)
b=('危険','動物','許可')
a.topics(b)
b=('手続','動物','問い合わせ')
a.topics(b)
b=('施設','構造','規模')
a.topics(b)
b=('飼養','施設','管理')
a.topics(b)
b=('動物','管理','概要')
a.topics(b)
b=('基準','守る','罰則')
a.topics(b)
b=('保管','許可','申請')
a.topics(b)
b=('書類','必要','ダウンロード')
a.topics(b)
b=('野良猫','捕獲','収容')
a.topics(b)
b=('野良猫','住み着く','駆除')
a.topics(b)
b=('野良猫','子供','産む')
a.topics(b)
b=('子猫','母','ない')
a.topics(b)
b=('野良猫','路上','死ぬ')
a.topics(b)
b=('猫','感染','病気')
a.topics(b)
b=('野良猫','飼う','よい')
a.topics(b)
b=('野良猫','エサ','人')
a.topics(b)
b=('野良猫','虐待','人')
a.topics(b)
b=('野良猫','去勢','補助')
a.topics(b)
b=('野良猫','庭','来')
a.topics(b)
b=('野良猫','対処','知り')
a.topics(b)
b=('動物','登録','相談')
a.topics(b)
b=('登録','必要','取扱')
a.topics(b)
b=('取扱','管理','法律')
a.topics(b)
b=('取扱','登録','方法')
a.topics(b)
b=('更新','変更','書類')
a.topics(b)
b=('動物','取扱','一覧')
a.topics(b)
b=('動物','取扱','違い')
a.topics(b)
b=('取扱','目的','何')
a.topics(b)
b=('業者','基準','法令')
a.topics(b)
b=('取扱','届出','書類')
a.topics(b)
b=('取扱','手数料','金')
a.topics(b)
b=('取扱','飼育','頭数')
a.topics(b)
b=('取扱','責任','研修')
a.topics(b)
b=('伝染','予防','対象')
a.topics(b)
b=('感染','LINE','お知らせ')
a.topics(b)
b=('ウイルス','患者','発生')
a.topics(b)
b=('運動','スペース','ケージ')
a.topics(b)
b=('運動','床','面積')
a.topics(b)
b=('取扱','業種','種類')
a.topics(b)
b=('犬','猫','しつけ')
a.topics(b)
b=('講演','受け','受講')
a.topics(b)
b=('譲渡','希望','引き取り')
a.topics(b)
b=('神奈川','愛護','センター')
a.topics(b)
b=('神奈川','愛護','センター')
a.topics(b)
#b=("会話","セミ")
#a.topics(b)