#
# 教師あり機械学習によるチート判定チュートリアル モデル学習用スクリプト(評価なし)
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

# dataset値
#  user_id  attack  gurd   life  is_cheat
#     2949    32.2  73.5  370.5       FALSE
#     3680    35.9  43.9  274.8       TRUE
#     4992    34.5  64.5  300.5       FALSE
#     2502    78.2  59.3  471.5       TRUE
#     4687    61.5  54.1  663.3       TRUE
#  ...

#
# データセット前処理
#   特徴量選定、データ整形など
#
print('preprocessing...')

# データ整形
#   is_cheatカラムを数値に置き換える
dataset = dataset.replace('TRUE', 1)
dataset = dataset.replace('FALSE', 0)

# 特徴量選定
#   lifeの特徴量は学習に必要ないと判断し、データセットから消す
dataset = dataset.drop('life', axis=1)
#   user_idカラムは特徴量としてはいらないので消す
feature_data = dataset.drop('user_id', axis=1)

# 特徴量データと正解データに分割する
#   is_cheatカラム(今回識別したい正解データ)をデータセットから分離する
correct_data = dataset['is_cheat']  # is_cheatカラムだけ取り出す
#   attack、gurdカラム(今回の特徴量データ)にする
feature_data = feature_data.drop('is_cheat', axis=1)  # is_cheatカラムを消す

# feature_dataの値   correct_dataの値
#  attack  guard       is_cheat
#    41.0  56.3        1
#    44.2  58.4        1
#    41.6  47.6        0
#    21.3  84.6        0
#    49.7  43.3        0

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
# attackとguardの組み合わせからis_cheatを学習
clf.fit(feature_data, correct_data)

#
# モデル保存
#   学習したモデルを保存する
#
print('save training model...')
dump(clf, Path(__file__).parent / 'train_model.joblib')

print('completed!')