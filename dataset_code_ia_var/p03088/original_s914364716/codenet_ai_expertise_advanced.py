from sys import stdin
from functools import reduce
from itertools import product

MOD = 10**9 + 7
N = int(stdin.readline())

# Mapping: 'A','G','C','T' => 0,1,2,3
ALPHA = 4
BAD_PATTERNS = {
    (0, 1, 2),  # AGC
    (1, 0, 2),  # GAC
    (0, 2, 1),  # ACG
}

def is_valid(j, k, l, a):
    window = [j, k, l, a]
    for idxs in [(1,2,3),(0,2,3),(0,1,3),(0,1,2)]:
        if tuple(window[i] for i in idxs) in BAD_PATTERNS:
            return False
    return True

# Use two rolling 3D tables instead of (N+1)*4*4*4 memory
dp_prev = [[[0]*ALPHA for _ in range(ALPHA)] for _ in range(ALPHA)]
dp_prev[3][3][3] = 1  # 3 as dummy index representing initial blank

for _ in range(N):
    dp_next = [[[0]*ALPHA for _ in range(ALPHA)] for _ in range(ALPHA)]
    for j, k, l in product(range(ALPHA), repeat=3):
        val = dp_prev[j][k][l]
        if not val: continue
        for a in range(ALPHA):
            if is_valid(j, k, l, a):
                dp_next[k][l][a] = (dp_next[k][l][a] + val) % MOD
    dp_prev = dp_next

print(sum(map(sum, (map(sum, dp_prev)))) % MOD)