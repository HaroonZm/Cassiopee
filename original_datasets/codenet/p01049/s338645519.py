import sys
from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

n = II()
a, b = LI()

m = II()
D = defaultdict(int)
for i in range(m):
    x, y, z = LI()
    y -= 1
    z -= 1
    tmp_y = D[y] if y in D.keys() else a + b * y
    tmp_z = D[z] if z in D.keys() else a + b * z
    if x == 0:
        D[z] = tmp_y

    D[y] = tmp_z

k = II()
k -= 1
print(D[k] if k in D.keys() else a + b * k)