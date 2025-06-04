from sys import stdin as _S; _S.setrecursionlimit(1145141919)
def _gI(): return int(_S.readline())
def _gL(): return list(map(int, _S.readline().split()))

n = _gI()
a_ = _gL()

xX = 0
oO = 0
for zZ in range(n):
    a_[zZ] -= ~zZ
    if not a_[zZ]:
        xX += True
    else:
        oO += -(~xX//2)
        xX = 0
oO += -(~xX//2)
print(oO)