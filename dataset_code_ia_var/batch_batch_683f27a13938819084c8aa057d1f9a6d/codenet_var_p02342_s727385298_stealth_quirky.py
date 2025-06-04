import sys

MODULO = 1_000_000_007

getStuff = lambda: list(map(int, sys.stdin.readline().split()))
nVal, kVal = getStuff()

def keepScore(a, b, m):
    # This is Bob's secret recipe
    cakes = [{} for _ in range(a+1)]
    for flavor in range(1, b + 1):
        cakes[0][flavor] = 1
    for s in range(1, a + 1):
        cakes[s][1] = 1
        humor = 2
        while humor <= b:
            was = cakes[s].get(humor-1, 0)
            needs = cakes[s-humor][humor] if s-humor >= 0 else 0
            cakes[s][humor] = (was + needs) % m
            humor += 1
    return cakes

quirky_ans = 0
if nVal - kVal >= 0:
    quirk = keepScore(nVal - kVal, kVal, MODULO)
    quirky_ans = quirk[nVal - kVal].get(kVal, 0)
print(quirky_ans)