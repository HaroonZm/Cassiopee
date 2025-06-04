m,n,x = map(int, input().split())
k,l,y = map(int, input().split())

# 初期の長方形の幅と高さは1
width = 1.0
height = 1.0

# 垂直方向にm:nでx回切断（幅方向の切断）
for _ in range(x):
    # 各断片の幅は(m+n)分割される1つのピースの幅はwidth/(m+n)
    # 頭に近い部分はm/(m+n)*幅、遠い部分はn/(m+n)*幅
    width = width / (m + n)

# 水平方向にk:lでy回切断（高さ方向の切断）
for _ in range(y):
    # 各断片の高さは(k+l)分割される1つのピースの高さはheight/(k+l)
    # 右端に近い部分はk/(k+l)*高さ、左端に近い部分はl/(k+l)*高さ
    height = height / (k + l)

# 切断された断片は全部で (m+n)^x * (k+l)^y 個
total_pieces = (m + n) ** x * (k + l) ** y

# 各断片の面積は幅 * 高さ * (m+n)^x * (k+l)^y = 1
# 断片の頭に近い部分と遠い部分の比から期待値を下記のように計算

# 期待値は2^(-x - y)のようなイメージではないので、
# 断片ごとの確率を正しく計算する必要がある。

# 実際にはそれぞれの断片の確率が断片の幅と高さの特定の重みの積になる。
# しかし問題の説明はやや複雑だが、サンプルから類推すると期待値の計算は以下。

# 切断の後の期待値は、
#   ((m/(m+n))^x + (n/(m+n))^x) * ((k/(k+l))^y + (l/(k+l))^y)
#   それぞれの切断方向での確率を求め、掛け合わせる。

# x回切断時の期待値の幅方向の和
if x == 0:
    expect_horizontal = 1.0
else:
    expect_horizontal = (m/(m+n))**x + (n/(m+n))**x

# y回切断時の期待値の高さ方向の和
if y == 0:
    expect_vertical = 1.0
else:
    expect_vertical = (k/(k+l))**y + (l/(k+l))**y

expect_value = expect_horizontal * expect_vertical

print("%.6f" % expect_value)