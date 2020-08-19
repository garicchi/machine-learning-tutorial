#
# 教師あり機械学習による弁当判定チュートリアル モデル学習用スクリプト(評価あり)
#   [使い方] python train_and_eval.py
#   [出力] 評価スコアのprint、学習済みモデルファイル(train_model.joblib)
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
#   is_bentoカラムを数値に置き換える


# 特徴量選定
#   heightの特徴量は学習に必要ないと判断し、データセットから消す


# 特徴量データと正解データに分割する
#   is_bentoカラム(今回識別したい正解データ)をデータセットから分離する

#   今回の特徴量データにする(is_bentoカラムを消す)


# 学習用データとテスト用データを分割する 7:3


# テストデータのitem_idカラムは予測結果表示時に必要なので取り出しておく

# item_idカラムは特徴量としてはいらないので消す


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
# モデル評価
#   [評価スコア] precision、recall、f_measure
#
print('evaluating...')
# 30%分割したテスト用データを学習したモデルに通して、出てきた結果と正解を比較する


# テスト推論結果をprintしてみる


# [precision] 学習モデルがチートと判定した中で、どれだけが本当にチートだったか

# [recall] 本当にチートだったデータの中から、どれだけチートだと予測できたか

# [f-measure] precisionとrecallの調和平均

#
# モデル保存
#   学習したモデルを保存する
#
print('save training model...')


print('completed!')