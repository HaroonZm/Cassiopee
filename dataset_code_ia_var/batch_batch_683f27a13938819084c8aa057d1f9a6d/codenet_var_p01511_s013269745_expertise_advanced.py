from functools import reduce, partial
import sys

MOD = 10**9 + 9
readline = sys.stdin.readline
write = sys.stdout.write

def matmul(A, B):
    N = len(A)
    # Use list comprehensions and zip for cleaner/faster code
    return [[sum(ai * bj % MOD for ai, bj in zip(a_row, b_col)) % MOD 
             for b_col in zip(*B)] 
            for a_row in A]

def mat_eye(n):
    # Generator-based identity matrix
    return [[int(i==j) for j in range(n)] for i in range(n)]

def mat_pow(mat, power):
    # Fast matrix exponentiation
    n = len(mat)
    result = mat_eye(n)
    while power:
        if power & 1:
            result = matmul(result, mat)
        mat = matmul(mat, mat)
        power >>= 1
    return result

def prepare(N):
    # Build transition matrix
    mat = mat_eye(N)
    for i in range(N-1):
        mat[i][i+1] = mat[i+1][i] = 1
    return mat

def matvecmul(mat, vec):
    # Matrix-vector multiplication
    return [sum(m*v % MOD for m, v in zip(row, vec)) % MOD for row in mat]

def solve_case():
    W, H, N = map(int, readline().split())
    if not (W or H or N):
        return False
    from collections import defaultdict

    obstacles = defaultdict(list)
    for _ in range(N):
        x, y = map(int, readline().split())
        if y > 1:
            obstacles[y-1].append(x-1)
    
    trans = prepare(W)
    X = [0]*W
    X[0] = 1
    prev_y = 0
    obs_seq = sorted(obstacles.items())
    for y, blocked in obs_seq:
        if y - prev_y > 0:
            T = mat_pow(trans, y - prev_y)
            X = matvecmul(T, X)
        for j in blocked:
            X[j] = 0
        prev_y = y
    if prev_y < H-1:
        T = mat_pow(trans, H-1 - prev_y)
        X = matvecmul(T, X)
    solve_case.cnt += 1
    write(f"Case {solve_case.cnt}: {X[W-1]}\n")
    return True
solve_case.cnt = 0

while solve_case():
    pass