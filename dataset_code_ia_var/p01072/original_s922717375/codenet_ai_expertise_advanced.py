from sys import stdin
from operator import itemgetter

w, h, t = map(int, stdin.readline().split())
p = int(stdin.readline())
hiryo = [tuple(map(int, stdin.readline().split())) for _ in range(p)]
hatake_boolean = [[b == '1' for b in stdin.readline().split()] for _ in range(h)]

# Utiliser un set pour l'accès O(1) aux cellules fertiles
fertile_cells = {(x, y) for y, row in enumerate(hatake_boolean) for x, val in enumerate(row) if val}
from collections import Counter

# Compter uniquement les apports qui sont sur une cellule fertile
ans = sum(1 for x, y, _ in hiryo if (x, y) in fertile_cells)
print(ans)