import string
import bisect

S, T = input(), input()
lS = len(S)
lT = len(T)

l = {s: [] for s in string.ascii_lowercase}
for i in range(lS):
    l[S[i]].append(i)

id = -1
ans = 0
for i in range(lT):
    if len(l[T[i]]) == 0:
        print(-1)
        exit()
    idx = bisect.bisect(l[T[i]], id)
    tmp = l[T[i]][idx % len(l[T[i]])]
    if id >= tmp:
        ans += lS
    id = tmp

print(ans + id + 1)