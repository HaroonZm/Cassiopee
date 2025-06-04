from sys import stdin

n_w = stdin.readline().split()
n = int(n_w[0])
w = int(n_w[1])

def create_3d_table(dim1, dim2, dim3):
    return [[[-1 for _ in range(dim3)] for __ in range(dim2)] for ___ in range(dim1)]

table = create_3d_table(n+1, n+1, 4*n)
table[0][0][0] = 0

first_weight = 0
for idx in range(n):
    x, y = [int(v) for v in stdin.readline().split()]
    if idx == 0:
        first_weight = x
    x = x - first_weight
    # style: functional for k
    for j in range(idx+2):
        for k in range(4*n):
            prior = table[idx][j][k]
            updated = -1
            if j-1 >= 0 and k-x >= 0:
                candidate = table[idx][j-1][k-x]
                if candidate >= 0:
                    updated = candidate + y
            # style: imperative
            table[idx+1][j][k] = max(prior, updated) if max(prior, updated) != -1 else prior

answer = 0
l = 0
while l <= n:
    # style: list comprehension for max search but keep imperative outer loop
    possible = [table[-1][l][p] for p in range(4*n) if first_weight*l + p <= w and table[-1][l][p] != -1]
    if possible:
        answer = answer if answer > max(possible) else max(possible)
    l += 1
print(answer)