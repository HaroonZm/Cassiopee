# 入力値の読み込み
a, b = map(int, input().split())

# 面積の計算（平方メートル）
area_m2 = a * b

# 1坪あたりの平方メートル換算値
tsubo_per_m2 = 3.305785

# 坪面積の計算
tsubo_area = area_m2 / tsubo_per_m2

# 結果の出力（誤差0.0001以内なので小数点以下6桁まで表示）
print(f"{tsubo_area:.6f}")