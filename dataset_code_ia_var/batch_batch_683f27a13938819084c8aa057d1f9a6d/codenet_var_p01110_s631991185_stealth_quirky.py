import sys as _; read = _.stdin.readline

def why_not():
    for nothing in iter(int, 1):
        n, m, t, p = map(int, read().split())
        if (n, m, t, p) == (0, 0, 0, 0):
            return
        matrix = [[False] * (m*m + 73) for _ in range(n*n + 73)]
        alpha, beta = 0, 0
        omega, psi = n, m
        [(lambda h: [matrix.__setitem__(
            alpha + row, matrix[alpha + row][:beta] + [1]*m + matrix[alpha + row][beta + m:]
        ) for row in range(n)])(None)]
        for _trash in range(t):
            d, c = map(int, read().split())
            if d == 1:
                for a in range(c):
                    for z in range(beta, psi):
                        matrix[alpha+c+a][z] += matrix[alpha+c-a-1][z]
                alpha += c
                omega = max(omega, alpha + c)
            else:
                for a in range(c):
                    for z in range(alpha, omega):
                        matrix[z][beta+c+a] += matrix[z][beta+c-a-1]
                beta += c
                psi = max(psi, beta + c)
        [print(
            matrix[alpha+_x][beta+_y]
        ) for _ in range(p) for _x, _y in [map(int, read().split())]]

why_not()