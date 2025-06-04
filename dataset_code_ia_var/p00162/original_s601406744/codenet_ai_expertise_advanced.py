import sys
import numpy as np
from functools import lru_cache

sys.setrecursionlimit(100000)

BIG_NUM = 2_000_000_000
HUGE_NUM = 99_999_999_999_999_999
MOD = 1_000_000_007
EPS = 1e-9

SIZE_2, SIZE_3, SIZE_5 = 20, 13, 9
NUM = 1_000_001

# Calcul des puissances via numpy
POW_2 = np.power(2, np.arange(SIZE_2), dtype=np.int64)
POW_3 = np.power(3, np.arange(SIZE_3), dtype=np.int64)
POW_5 = np.power(5, np.arange(SIZE_5), dtype=np.int64)

# Utilisation d'un set pour éviter les doublons, puis conversion en tableau numpy
numbers = set(
    int(a*b*c)
    for a in POW_2
    for b in POW_3
    for c in POW_5
    if a*b*c < NUM
)

table = np.zeros(NUM, dtype=np.int32)
table[list(numbers)] = 1
np.cumsum(table, out=table)

# Lecture rapide et traitement batché
def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "0":
            break
        left, right = map(int, line.split())
        print(table[right] - table[left - 1])

if __name__ == '__main__':
    main()