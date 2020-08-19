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
dataset = pd.read_csv(Path(__file__).parent / 'dataset.csv')


#
# データセット前処理
#   特徴量選定、データ整形など
#
print('preprocessing...')

# データ整形
#   is_bentoカラムを数値に置き換える
dataset = dataset.replace('not_bento', 0)
dataset = dataset.replace('bento', 1)

# 特徴量選定
#   heightの特徴量は学習に必要ないと判断し、データセットから消す
dataset = dataset.drop('height', axis=1)

# 特徴量データと正解データに分割する
#   is_bentoカラム(今回識別したい正解データ)をデータセットから分離する
correct_data = dataset['is_bento']
#   今回の特徴量データにする(is_bentoカラムを消す)
feature_data = dataset.drop('is_bento', axis=1)

# 学習用データとテスト用データを分割する 7:3
train_feature, test_feature, train_correct, test_correct = train_test_split(
    feature_data, correct_data, test_size=0.3
)
# テストデータのitem_idカラムは予測結果表示時に必要なので取り出しておく
test_item_id = test_feature['item_id']
# item_idカラムは特徴量としてはいらないので消す
train_feature = train_feature.drop('item_id', axis=1)
test_feature = test_feature.drop('item_id', axis=1)

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
clf.fit(train_feature, train_correct)


#
# モデル評価
#   [評価スコア] precision、recall、f_measure
#
print('evaluating...')
# 30%分割したテスト用データを学習したモデルに通して、出てきた結果と正解を比較する
predict = clf.predict(test_feature)

# テスト推論結果をprintしてみる
print('\nテスト推論結果プレビュー(一部データ)')
result = pd.DataFrame({
    'item_id': test_item_id,
    '正解データ': test_correct,  # 正解データ
    '推論結果': predict  # 予測したデータ
})
print(result.head().to_string(index=None))

# [precision] 学習モデルがチートと判定した中で、どれだけが本当にチートだったか
precision = precision_score(test_correct, predict)
# [recall] 本当にチートだったデータの中から、どれだけチートだと予測できたか
recall = recall_score(test_correct, predict)
# [f-measure] precisionとrecallの調和平均
f_measure = f1_score(test_correct, predict)
print('\n---- evaluation score -----')
print(f'PRECISION: {precision}')
print(f'RECALL: {recall}')
print(f'F_MEASURE: {f_measure}')
print('---------------------------\n')


#
# モデル保存
#   学習したモデルを保存する
#
print('save training model...')
dump(clf, Path(__file__).parent / 'train_model.joblib')

print('completed!')