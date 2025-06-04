from functools import cache
from itertools import product, repeat

def s():
    def b(M, x, y, n=1):
        M[x][y] = 0
        a = n
        for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
            nx, ny = x + dx, y + dy
            if M[nx][ny]:
                a = max(a, b(M, nx, ny, n+1))
        M[x][y] = 1
        return a

    for e in iter(input, '0'):
        n, m = int(e), int(input())
        P = [[0, *repeat(0, n), 0] for _ in range(m+2)]
        for i, row in enumerate((map(int, input().split()) for _ in range(m)), 1):
            P[i][1:n+1] = row
        print(max(
            (b(P, i, j)
             for i, j in product(range(1, m+1), range(1, n+1))
             if P[i][j]), default=0
        ))

if __name__ == '__main__':
    s()