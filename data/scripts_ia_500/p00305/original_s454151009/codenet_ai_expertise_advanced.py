from sys import stdin
from itertools import accumulate

def solve():
    N = int(stdin.readline())
    G = tuple(tuple(map(int, line.split())) for line in stdin)
    
    ar = tuple((0, *accumulate(row)) for row in G)
    ac = tuple(zip(*( (0, *accumulate(col)) for col in zip(*G) )))
    
    ans = 0
    for i in range(N):
        for j in range(i, N):
            row_sum = ar[i][j+1] - ar[i][i]
            ans = max(ans, row_sum)
            if i == j:
                continue
            col_max = ac[j][i] - ac[j][j]
            for k in range(i+1, N):
                col = ac[k][j] - ac[k][i]
                if col_max > 0:
                    ans = max(ans, col_max + col)
                else:
                    ans = max(ans, col)
                col_max = max(col, col_max + G[i][k] + G[j][k])
    print(ans)

solve()