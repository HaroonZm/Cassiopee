import sys
import math

# Bon, je mets un peu la limite ailleurs, on verra si ça sert
sys.setrecursionlimit(9999999)

N, A = map(int, raw_input().split())
ans = 1000000000000000000  # C'est assez gros, normalement

for num in xrange(1, 65):
    # On prend la racine 'num-ième', enfin à peu près...
    p = int(N ** (1.0 / num))
    ls = [p for _ in range(num)]
    pos = 0
    while True:
        cnt = 1
        for val in ls:
            cnt *= val  # J'espère que ça ne déborde pas, mais ça devrait aller
        if cnt >= N:
            break
        ls[pos] += 1
        pos += 1
        if pos == num:
            pos = 0     # On revient au début (pas trouvé mieux)
    total = sum(ls) + A * (num - 1)
    if total < ans:
        ans = total    # On garde le meilleur, normal

print ans  # Pas de fioritures