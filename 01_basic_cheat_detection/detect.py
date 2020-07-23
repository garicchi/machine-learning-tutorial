#
# 教師あり機械学習によるチート判定チュートリアル bot判定用スクリプト
#   [使い方] python detect.py
#   [出力] bot判定結果をprint
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
print('入力されたユーザーの特徴からbotかどうか判定します')
user_id = input('user_idを入力してください: ')
attack = input('attack値を入力してください: ')
guard = input('guard値を入力してください: ')
life = input('life値を入力してください: ')

#
# 判定
#
input_data = [
    [float(attack), float(guard)]
]
predict_data = clf.predict(input_data)

predict_row = predict_data[0]
#
# 結果の出力
#
print('----------')
if predict_row == 1:
    print(f'[{user_id}]は機械学習により[チート]と判定されました')
else:
    print(f'[{user_id}]は機械学習により[チートではない]と判定されました')
print('----------')

print('completed!')