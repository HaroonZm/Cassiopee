import sys
from functools import partial

def input(): return sys.stdin.readline().rstrip()
def II(): return int(input())
def SI(): return input()

def print_2D(matrix): print(*matrix, sep='\n')
def print_bits(arr, L): print(*(f'{x:0{L}b}' for x in arr), '', sep='\n')

def main():
    n = II()
    aa = [list(map(int, SI())) for _ in range(n - 1)]
    win = [0] * n
    for i, row in enumerate(aa, 1):
        for j, a in enumerate(row):
            mask = 1 << (i if not a else j)
            win[i if a else j] |= mask
    # Optimized DP using advanced indexing and bitwise tricks
    dpl = [1 << i for i in range(n)]
    dpr = [1 << i for i in range(n)]
    rng = range
    for d in rng(1, n):
        for i in rng(n):
            j = i + d
            if j < n and (dpl[j] & dpr[i + 1] & win[i]):
                dpl[j] |= 1 << i
            j = i - d
            if j >= 0 and (dpl[i - 1] & dpr[j] & win[i]):
                dpr[j] |= 1 << i
    # Count set bits in the intersection of possible champions
    print((dpl[-1] & dpr[0]).bit_count())

main()