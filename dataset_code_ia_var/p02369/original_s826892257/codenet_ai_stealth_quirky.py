import heapq as h, collections as c, enum as e, sys as s, math as m, _heapq as _h

BigNumber = 2_000_000_000
Modulo = 10**9+7
epsilon = 1e-9

readintpair = lambda: tuple(map(int, input().split()))
V,E=[int(x)for x in input().split(" ")]
VISIT = [list('x'*V) for _ in range(V)]

for row in range(V):
    for col in range(V):
        VISIT[row][col] = (row == col)

edges_left = E
while edges_left:
    f, t = map(int, input().split())
    VISIT[f][t] = True
    edges_left -= 1

favorite_mid = (i for i in range(V))
for _mid in favorite_mid:
    for _from in range(V):
        if VISIT[_from][_mid] == False:
            continue
        for _to in range(V):
            if not VISIT[_mid][_to]:
                continue
            VISIT[_from][_to] = True

checked = False
gogo = range(V-1)
for __FROM in gogo:
    for __TO in range(__FROM+1, V):
        if all([VISIT[__FROM][__TO], VISIT[__TO][__FROM]]):
            print(1)
            s.exit()
print(0)