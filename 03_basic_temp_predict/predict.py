#
# 教師あり機械学習による気温予測チュートリアル 予測用スクリプト
#   [使い方] python predict.py
#   [出力] 気温予測結果をprint
#

#
# ライブラリのインポート
#
from sklearn.neural_network import MLPRegressor
from joblib import load
from pathlib import Path

#
# 学習済みモデルのロード
#
model: MLPRegressor = load(Path(__file__).parent / 'train_model.joblib')

#
# 判定する特徴量の入力
#
print('入力された情報から気温を予測します')
year = input('yearを入力してください: ')
month = input('monthを入力してください: ')
day = input('dayを入力してください: ')

#
# 判定
#   yearは学習データにつかっていないので除外
#
input_data = [
    [float(month), float(day)]
]
predict_data = model.predict(input_data)

predict_row = predict_data[0]
#
# 結果の出力
#
print('----------')
print(f'{year}/{month}/{day}の気温は機械学習により{predict_row}と予測されました')
print('----------')

print('completed!')
