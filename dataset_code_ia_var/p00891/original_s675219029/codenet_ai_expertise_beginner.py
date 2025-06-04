import string
import sys

# Alphabet utilisé pour l'encodage
alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

# Constantes pour le hash
MOD = 10**9 + 9
P = 13
Q = 19
L = 1000

# Pré-calcul pour les puissances de P et Q
pows_p = [1] * (L+1)
pows_q = [1] * (L+1)
for i in range(L):
    pows_p[i+1] = pows_p[i] * P % MOD
    pows_q[i+1] = pows_q[i] * Q % MOD

def hash_table(grid, w, h):
    table = [[0] * (w+1) for i in range(h+1)]
    for i in range(h):
        sum_val = 0
        prev = table[i]
        curr = table[i+1]
        line = grid[i]
        for j in range(w):
            sum_val = (sum_val * P + line[j]) % MOD
            curr[j+1] = (sum_val + prev[j+1] * Q) % MOD
    return table

def sub_hash(table, x0, y0, x1, y1):
    pw = pows_p[x1 - x0]
    qh = pows_q[y1 - y0]
    val = table[y1][x1] - table[y1][x0] * pw
    val -= table[y0][x1] * qh
    val += table[y0][x0] * (pw * qh % MOD)
    return val % MOD

def rotate(grid, w, h):
    new_grid = [[0] * h for i in range(w)]
    for i in range(h):
        for j in range(w):
            new_grid[j][h-1-i] = grid[i][j]
    return new_grid

def mirror(grid, w, h):
    new_grid = []
    for row in grid:
        new_grid.append(list(reversed(row)))
    return new_grid

def read_input():
    return sys.stdin.readline()

def write_output(s):
    sys.stdout.write(s)

def parse_grid(height, index_func):
    grid = []
    for _ in range(height):
        line = read_input().strip()
        bits = []
        for c in line:
            v = index_func(c)
            for k in range(5, -1, -1):
                bits.append(1 if (v & (1 << k)) else 0)
        grid.append(bits)
    return grid

def solve():
    line = read_input()
    if not line:
        return False
    parts = line.strip().split()
    if not parts or len(parts) < 3:
        return False
    w, h, p = map(int, parts)
    if w == 0 and h == 0 and p == 0:
        return False
    idx = alphabet.index
    # Lire la grande grille
    big_grid = parse_grid(h, idx)
    # Lire le motif
    pat_grid = parse_grid(p, idx)
    orig_pat = [list(row) for row in pat_grid]
    pat_hashes = set()
    # 4 rotations
    for _ in range(4):
        htab = hash_table(pat_grid, p, p)
        pat_hashes.add(htab[-1][-1])
        pat_grid = rotate(pat_grid, p, p)
    # Miroir + 4 rotations
    pat_grid = mirror(orig_pat, p, p)
    for _ in range(4):
        htab = hash_table(pat_grid, p, p)
        pat_hashes.add(htab[-1][-1])
        pat_grid = rotate(pat_grid, p, p)
    # Hash de la grande grille
    big_hash = hash_table(big_grid, w, h)
    ans = 0
    for i in range(h - p + 1):
        for j in range(w - p + 1):
            if sub_hash(big_hash, j, i, j + p, i + p) in pat_hashes:
                ans += 1
    write_output(str(ans) + '\n')
    return True

while solve():
    pass