import sys
import math

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    s, d = map(int, input().split())
    diff = d - s
    # On cherche le plus grand n tel que 2^n divise diff
    # Ceci équivaut à la puissance de 2 maximale qui divise diff
    if diff == 0:
        print(0)
        continue
    # extraire la plus grande puissance de 2 qui divise diff
    # utiliser le fait que diff & (-diff) donne la plus petite puissance de 2 qui divise diff
    p = diff & (-diff)
    # p = 2^n, donc n = nombre de bits de p - 1
    n = p.bit_length() - 1
    print(n + 1)