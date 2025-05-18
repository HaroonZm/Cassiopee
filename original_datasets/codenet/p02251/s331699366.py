#標準入力と変数の初期化
num = int(input())
coin = 0

#25セントを使える枚数を調べ合計金額から減らす
coin += num // 25
num -= num // 25 * 25

#10セントを使える枚数を調べ合計金額を減らす
coin += num // 10
num -= num // 10 * 10

#5セントを使える枚数を調べ合計金額を減らす
coin += num // 5
num -= num // 5 * 5

#1セントの枚数を足し出力する
print(coin + num)