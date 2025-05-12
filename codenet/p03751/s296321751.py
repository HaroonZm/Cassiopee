N = int(input())
S = [input().strip() for i in range(N)]
T = input().strip()

lower = 1  # Tが入りうる番号の下限。先頭に入りうるので初期値1
upper = N + 1  # Tが入りうる番号の上限。末尾に入りうるので初期値N+
for s in S:
    # s中の'?'をすべて'a'に置き換えたものは先頭に来るし、
    # すべて'z'に置き換えたものは末尾に来る
    s_first = s.replace('?', 'a')
    s_last = s.replace('?', 'z')
    if T < s_first:
        upper -= 1  # sの取りうる最小値より小さい場合、上限が下がる
    if s_last < T:
        lower += 1  # sの取りうる最大値より大きい場合、下限が上がる

ans = ' '.join(map(str, range(lower, upper + 1)))
print(ans)