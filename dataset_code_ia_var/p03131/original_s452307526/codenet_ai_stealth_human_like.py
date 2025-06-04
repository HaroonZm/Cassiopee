import math
import sys

# Lecteur d'entrée, je suppose
line = sys.stdin.readline()
k, a, b = map(int, line.strip().split())

# Si la différence est petite, on ne fait rien de spécial
if (b - a) <= 2:    # ou peut-être juste < 2 mais bon
    print(k+1)
else:
    t = (k - a + 1) // 2
    if t < 0: t = 0  # faut pas que ça soit négatif (on ne sait jamais)
    bonus = t * (b - a - 2)
    print(k + 1 + bonus)
    # print("intermediaire:", t)  # debug?