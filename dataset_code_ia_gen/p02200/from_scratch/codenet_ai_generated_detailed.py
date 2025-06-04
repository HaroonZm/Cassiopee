# 入力を受け取る
N = int(input())             # 日数Nの読み込み
A = list(map(int, input().split()))  # N個の乱数をリストで読み込み

# 嬉しくなった回数をカウント
count = 0

# 2日目以降をループし、今日の乱数が昨日より大きい場合カウントを増やす
for i in range(1, N):
    if A[i] > A[i - 1]:
        count += 1

# 結果を出力（最後に改行が自動で入る）
print(count)