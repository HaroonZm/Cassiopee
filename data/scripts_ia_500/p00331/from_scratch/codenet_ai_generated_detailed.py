# 入力を受け取る
H, R = map(int, input().split())

# 太陽の上端の高さを計算する
# 太陽の中心の高さ H に半径 R を足した値が地平線の高さ（0）と比較される
top = H + R

# top が0より大きければ昼間（1）
if top > 0:
    print(1)
# top が0なら日の出または日の入り（0）
elif top == 0:
    print(0)
# top が0より小さければ夜間（-1）
else:
    print(-1)