from functools import reduce
from itertools import accumulate, cycle

n = int(input())
a = list(map(int, input().split()))

# Création de masques booléens pour pairs et impairs, via map+lambda
parity = list(map(lambda x: x % 2, a))
# Compte les paires et impairs par sums déguisés
p = sum(map(lambda x: 1-x, parity))
q = sum(parity)

if not min(p, q):
    print(0)
    exit()

# Doublement obtus : fonction en une ligne avec accumulate et cycle
def bizarre(q, p):
    t = (q % 2, q//2)
    return p + reduce(lambda acc, x: acc + x[0]*2 + (1-x[0])*2*max(x[1]-1,0), [(t[0], t[1])], 0)

print(bizarre(q,p))