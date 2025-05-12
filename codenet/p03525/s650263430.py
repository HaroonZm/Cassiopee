N = int(input())
D = list(map(int, input().split()))

"""
愚直に解くと
・時差が0,12以外の人は、D, 24-Dの2パターンの時間になりうる
・なので、2^N全部試す
で、普通にTLE。

例えばある時差Dの人が
（１）一人の場合：時刻Dとする
（２）二人の場合：Dと24-Dで振り分ける
で、最小の時差を減らさない動きができる
一方で
（３）三人以上の場合：Dと24-Dの少なくとも一方が２人以上いることになるから、時差の最小値が0になる

なので、時差Dが一人の時は、Dと24-Dで２通り試して、時差Dが二人の時は両方に入れる、３人以上は問答無用で0になる、みたいにするとよさげ
あるいは最初はDとして、次は24-Dとして～みたいなのを繰り返す。
"""

from collections import Counter
from collections import defaultdict

c = Counter(D)
c[0] += 1

for i in range(13):
    if i == 0 or i == 12:
        if c[i] >= 2:
            print(0)
            exit()
    else:
        if c[i] >= 3:
            print(0)
            exit()

D.sort()

d = defaultdict(int)
d[24] += 1
is_am = True
for t in D:
    if is_am:
        d[t] += 1
        is_am = False
    else:
        d[24 - t] += 1
        is_am = True

ans = min(D)
times = list(d.keys())
times.sort()
for a,b in zip(times, times[1:]):
    ans = min(ans, b-a)

print(ans)