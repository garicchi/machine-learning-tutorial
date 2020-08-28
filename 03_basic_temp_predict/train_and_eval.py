#
# 教師あり機械学習による気温予測チュートリアル学習用スクリプト(評価あり)
#   [使い方] python train_and_eval.py
#   [出力] 評価スコアのprint、学習済みモデルファイル(train_model.joblib)
#

#
# ライブラリのインポート
#   [sklearn] 機械学習用ライブラリ
#   [pandas] 表データを扱うライブラリ
#
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import pandas as pd
from joblib import dump
from pathlib import Path

#
# 学習用データセット(CSV)の読み込み
#   [data.csv] 事前に用意しておいたユーザーの特徴とbotかどうかが記録されたデータ
#
print('loading datasets...')
dataset = pd.read_csv(Path(__file__).parent / 'dataset.csv')
print(dataset.head())

# dataset値
#  year  month  day  temperature
#  2019      8   27         25.3
#  2019      8   28         25.6
#  2019      8   29         28.9
#  2019      8   30         26.0
#  2019      8   31         27.3

#
# データセット前処理
#   特徴量選定、データ整形など
#
print('preprocessing...')

# 特徴量選定
#   年の情報は気温予測に関係ないとして、データセットから消す
dataset = dataset.drop('year', axis=1)

# 特徴量データと正解データに分割する
#   temperatureカラム(今回識別したい正解データ)をデータセットから分離する
correct_data = dataset['temperature']  # temperatureカラムだけ取り出す
#   month、dayカラム(今回の特徴量データ)にする
feature_data = dataset.drop('temperature', axis=1)  # temperatureカラムを消す

# 学習用データとテスト用データを分割する 7:3
train_feature, test_feature, train_correct, test_correct = train_test_split(
    feature_data, correct_data, test_size=0.3
)


#
# モデル学習
#   [アルゴリズム] ニューラルネットワーク
#   [学習方法] 教師あり
#   [タスクの種類] 分類タスク
#
print('training...')
# [MLPRegressor] ニューラルネットワークをつかった回帰分析(数値の予測ができる)
model = MLPRegressor()
# monthとdayの組み合わせからtemperatureを学習
model.fit(train_feature, train_correct)


#
# モデル評価
#   [評価スコア] mean absolute error(予測値が実際のあたいから平均でどれぐらいずれていたか)
#
print('evaluating...')
# 30%分割したテスト用データを学習したモデルに通して、出てきた結果と正解を比較する
predict = model.predict(test_feature)

# テスト推論結果をprintしてみる
print('\nテスト推論結果プレビュー(一部データ)')
result = pd.DataFrame({
    '正解データ': test_correct,  # 正解データ
    '予測結果': predict  # 予測したデータ
})
print(result.head().to_string(index=None))

mae = mean_absolute_error(test_correct, predict)
print('\n---- evaluation score -----')
print(f'MEAN ABSOLUTE ERROR(平均でこれぐらい予測がずれてる): {mae}')
print('---------------------------\n')

#
# モデル保存
#   学習したモデルを保存する
#
print('save training model...')
dump(model, Path(__file__).parent / 'train_model.joblib')

print('completed!')
