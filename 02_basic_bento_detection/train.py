#
# 教師あり機械学習によるbento判定チュートリアル モデル学習用スクリプト(評価なし)
#   [使い方] python train.py
#   [出力] 学習済みモデルファイル(train_model.joblib)
#

#
# ライブラリのインポート
#   [sklearn] 機械学習用ライブラリ
#   [pandas] 表データを扱うライブラリ
#
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd
from joblib import dump
from pathlib import Path

#
# 学習用データセット(CSV)の読み込み
#   [data.csv] 事前に用意しておいたユーザーの特徴とbotかどうかが記録されたデータ
#
print('loading datasets...')

#
# データセット前処理
#   特徴量選定、データ整形など
#
print('preprocessing...')

# データ整形
#   is_cheatカラムを数値に置き換える


# 特徴量選定
#   heightの特徴量は学習に必要ないと判断し、データセットから消す

#   item_idカラムは特徴量としてはいらないので消す


# 特徴量データと正解データに分割する
#   is_bentoカラム(今回識別したい正解データ)をデータセットから分離する

#   今回の特徴量データにする


#
# モデル学習
#   [アルゴリズム] ニューラルネットワーク
#   [学習方法] 教師あり
#   [タスクの種類] 分類タスク
#
print('training...')
# [MLPClassifier] Multilayer Perceptron=ニューラルネットワーク
#   [solver] ニューラルネットワークの重み調整アルゴリズム

# 特徴量の組み合わせからis_bentoを学習

#
# モデル保存
#   学習したモデルを保存する
#
print('save training model...')


print('completed!')