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
dataset = pd.read_csv(Path(__file__).parent / 'dataset.csv')

#
# データセット前処理
#   特徴量選定、データ整形など
#
print('preprocessing...')

# データ整形
#   is_cheatカラムを数値に置き換える
dataset = dataset.replace('bento', 1)
dataset = dataset.replace('not_bento', 0)

# 特徴量選定
#   heightの特徴量は学習に必要ないと判断し、データセットから消す
dataset = dataset.drop('height', axis=1)
#   item_idカラムは特徴量としてはいらないので消す
feature_data = dataset.drop('item_id', axis=1)

# 特徴量データと正解データに分割する
#   is_bentoカラム(今回識別したい正解データ)をデータセットから分離する
correct_data = dataset['is_bento']  # is_bentoカラムだけ取り出す
#   今回の特徴量データにする
feature_data = feature_data.drop('is_bento', axis=1)  # is_bentoカラムを消す

#
# モデル学習
#   [アルゴリズム] ニューラルネットワーク
#   [学習方法] 教師あり
#   [タスクの種類] 分類タスク
#
print('training...')
# [MLPClassifier] Multilayer Perceptron=ニューラルネットワーク
#   [solver] ニューラルネットワークの重み調整アルゴリズム
clf = MLPClassifier(solver='adam')
# 特徴量の組み合わせからis_bentoを学習
clf.fit(feature_data, correct_data)

#
# モデル保存
#   学習したモデルを保存する
#
print('save training model...')
dump(clf, Path(__file__).parent / 'train_model.joblib')

print('completed!')