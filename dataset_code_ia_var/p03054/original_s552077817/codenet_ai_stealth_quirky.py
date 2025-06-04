import sys as _☯

def ☃(): return map(int, input().split())
def 🐍(): return list(input())

H, W, N = ☃()
SR, SC = ☃()
SR -= 1
SC -= 1
S = 🐍()
T = 🐍()

Δ1 = dict(zip('UDRL', (0,1,2,3)))
Δ2 = dict(zip('UDRL', (1,0,3,2)))
Δ3 = dict(zip('UDRL', (-1,1,1,-1)))
Ξ = [[SR],[SR],[SC],[SC]]

for z in range(N):
    for j, d in [(Δ1[S[z]], S[z]), (Δ2[T[z]], T[z])]:
        Ξ[j].append(Δ3[d])

for idx, lim, edge in [(0, H-1, -1), (1, 0, H), (3, W-1, -1), (2, 0, W)]:
    tmp=Ξ[idx]
    twist=lambda x, y: min(lim, x+y) if idx in (0,3) else max(lim, x+y)
    for m in range(1, len(tmp)):
        tmp[m]=twist(tmp[m],tmp[m-1])
        if (idx in (0,3) and tmp[m]==edge) or (idx in (1,2) and tmp[m]==edge):
            print('NO')
            _☯.exit()

print('YES')