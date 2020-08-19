#
# 教師あり機械学習による弁当判定チュートリアル 弁当判定用スクリプト
#   [使い方] python detect.py
#   [出力] 弁当判定結果をprint
#

#
# ライブラリのインポート
#
from sklearn.neural_network import MLPClassifier
from joblib import load
from pathlib import Path

#
# 学習済みモデルのロード
#
clf: MLPClassifier = load(Path(__file__).parent / 'train_model.joblib')

#
# 判定する特徴量の入力
#
print('入力されたアイテムの特徴からカテゴリを判別します')
item_id = input('item_idを入力してください: ')
width = input('width値を入力してください: ')
height = input('height値を入力してください: ')
weight = input('weight値を入力してください: ')
price = input('price値を入力してください: ')

#
# 判定
#
input_data = [
    [float(width), float(weight), float(price)]
]
predict_data = clf.predict(input_data)

predict_row = predict_data[0]
#
# 結果の出力
#
print('----------')
if predict_row == 1:
    print(f'[{item_id}]は機械学習により[bento]と判定されました')
else:
    print(f'[{item_id}]は機械学習により[bentoではない]と判定されました')
print('----------')

print('completed!')