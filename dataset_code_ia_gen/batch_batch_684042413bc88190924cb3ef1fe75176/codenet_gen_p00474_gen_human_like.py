import sys
sys.setrecursionlimit(10**7)

N, L = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for _ in range(N)]

# 各つららが折れるまでの時間を格納（0ならまだ折れていない）
break_time = [0] * N

# 再帰的に折れる時間を計算
def dfs(i):
    if break_time[i] != 0:
        return break_time[i]
    left = dfs(i-1) if i-1 >= 0 else 0
    right = dfs(i+1) if i+1 < N else 0

    # 増加できる時間はL - a[i]が上限
    # つららiは隣のつららより長い間だけ増加可能（つまり隣が折れるまで）
    # 両端は片方の隣だけを見る
    if i == 0:
        time = min(L - a[i], right)
    elif i == N -1:
        time = min(L - a[i], left)
    else:
        time = min(L - a[i], left, right)

    break_time[i] = time
    return time

# ベースケース：最初は両端が折れる時間(L - a[i])で確定させるために初期化
# 実際には再帰のベースケースとして隣の情報を使うので、
# すべて0のまま始め、呼び出しで計算させる。
# 先に折れるつららの時間を決めることで伝播するため、
# まずは末端から計算開始する。
for i in range(N):
    dfs(i)

print(max(break_time))