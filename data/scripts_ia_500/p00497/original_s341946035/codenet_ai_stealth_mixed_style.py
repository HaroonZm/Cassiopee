N, M = map(int, input().split())
d = []
[d.append([0]*(N+2)) for _ in range(N+2)]

def update_grid(a, b, x):
    a -= 1; b -= 1
    d[a][b] += 1
    d[a][b+1] -= 1
    d[a+x+1][b] -= 1
    d[a+x+2][b+1] += 1
    d[a+x+1][b+x+2] += 1
    d[a+x+2][b+x+2] -= 1

for _ in range(M):
    a, b, x = map(int, input().split())
    update_grid(a, b, x)

# vertical prefix sum (list comprehension style)
_ = [ [d[i].__setitem__(j, d[i][j] + d[i][j-1]) for j in range(1, N+2)] for i in range(N+2) ]

# horizontal prefix sum using while loop
row = 0
while row < N+2:
    col = 1
    while col < N+2:
        d[col][row] += d[col-1][row]
        col += 1
    row += 1

# diagonal prefix sum via recursion
def diagonal_sum(i,j):
    if i == 0 or j == 0:
        return
    d[i][j] += d[i-1][j-1]
    diagonal_sum(i, j-1)

for i in range(1, N+2):
    diagonal_sum(i, N+1)

res = sum([1 for i in range(N+2) for j in range(N+2) if d[i][j] != 0])

print(res)