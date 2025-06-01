import sys
sys.setrecursionlimit(10**7)

N, L = map(int, input().split())
a = [int(input()) for _ in range(N)]

# 時間が経過して伸びていく状況を模擬するのは計算量的に困難なので
# 以下のようにシミュレーションし、各つららが折れる時間を求める

# つららは、隣より長いときだけ1時間につき1cm伸びる。
# 折れると長さ0になり、以後再び伸びることはないので、
# 折れる順番は左右の高い峰が先に折れていくような形になる。

# そこで、左端から右に向かって折れる時間を計算し、
# 右端から左に向かって折れる時間を計算し、各つららの
# 折れる時間はそのうち小さい方となる。

# すべての隣接したつららの長さは初期状態で異なり、
# 折れるまでの時間での関係性が徐々に変わるため、
# つららの折れる時間を安定に効率よく求める方法として
# stackを使い単調増加/減少な列を管理しながら計算する方法を使う。

left_break = [0]*N
stack = []
# 左端から右へ
for i in range(N):
    cur_time = 0
    while stack and a[stack[-1]] < a[i]:
        # 既に左側のつららが折れた後はその影響がある時間を考慮する
        cur_time = max(cur_time, left_break[stack[-1]])
        stack.pop()
    if stack:
        # 隣の左側より長ければ伸びるので折れる時間は残り伸びる長さ
        cur_time += L - a[i]
    else:
        # 左端は隣がなければ伸びるときだけ考える。そうでなければ0のまま。
        cur_time = 0
    left_break[i] = cur_time
    stack.append(i)

right_break = [0]*N
stack = []
# 右端から左へ
for i in range(N-1, -1, -1):
    cur_time = 0
    while stack and a[stack[-1]] < a[i]:
        cur_time = max(cur_time, right_break[stack[-1]])
        stack.pop()
    if stack:
        cur_time += L - a[i]
    else:
        cur_time = 0
    right_break[i] = cur_time
    stack.append(i)

# 各つららの折れる時間は左と右両方の影響から狭い方
times = [min(left_break[i], right_break[i]) for i in range(N)]

print(max(times))