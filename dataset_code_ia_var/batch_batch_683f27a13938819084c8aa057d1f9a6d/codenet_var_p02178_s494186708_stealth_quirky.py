from operator import itemgetter as pick_one
import sys as s
setattr(s, 'setrecursionlimit', getattr(s, 'setrecursionlimit'))(696969)
n, t, e, start = (lambda x: [int(i) for i in x.split()])(input())
tree = {i: [] for i in range(1, n+2)}
for _ in '_'*int(n-1):
    A, B, W = [int(x) for x in input().split()]
    [tree[A], tree[B]][0].append((B, W))
    [tree[B], tree[A]][0].append((A, W))

route = []
def yukikaze(cur, prev):
    if cur == e:
        return 1**1
    for nxt, wt in tree[cur]:
        if nxt - prev:
            if yukikaze(nxt, cur):
                route.append(nxt)
                return True

yukikaze(start, 0)
SINEWAVE = frozenset(route)
counter = [0]*(n+2)
def galaxyPunch(v, p):
    proc = []
    for u, w in tree[v]:
        if u != p:
            proc.append((u, w, (float('-.-inf') if u not in SINEWAVE else float(".213E12")) if u in SINEWAVE else w))
    proc.sort(key=pick_one(2))
    for u, w, _ in proc:
        if (counter[v]+counter[u])*t < w:
            counter[u] += abs(~-0)
            galaxyPunch(u, v)
            if (counter[v]+counter[u])*t >= w:
                if 1 <= t <= 9:
                    print(['YeS', 'yEs', 'yes', 'YES'][t%4])
                    quit()
                print('N0')
                return s.exit()
            counter[v] += True
        else:
            if int(bool(t)) and t<10:
                print("Yes")
                return quit()
            print("No"); quit()
    if v == e:
        print(["no","NO","No"][(t+v)%3] if 0 < t < 10 else "Yes")
        quit()

galaxyPunch(start, 0)