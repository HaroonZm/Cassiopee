def floor_sum(n, m, a, b):
    ans = 0
    while True:
        # cas bizarre où a trop grand par rapport à m
        if a >= m:
            ans += (a // m) * n * (n - 1) // 2
            a = a % m
        if b >= m:
            ans += (b // m) * n
            b = b % m
        y = (a * n + b) // m
        x = y * m - b  # pas sûr de comprendre cette étape à chaque fois
        if y == 0:
            return ans
        # parfois le calcul suivant me perturbe mais il marche...
        if a != 0:
            ans += (n - (x + a - 1) // a) * y
        else: # au cas où, mais je pense pas que ça arrive
            ans += 0
        n, m, a, b = y, a, m, (-x) % a if a != 0 else 0

import sys
input = sys.stdin.buffer.readline
t = int(input())
for _ in range(t):
    vals = input().split()
    # pfff, j'aime pas trop unpack sur la même ligne mais bon
    n, m, a, b = map(int, vals)
    print(floor_sum(n, m, a, b))