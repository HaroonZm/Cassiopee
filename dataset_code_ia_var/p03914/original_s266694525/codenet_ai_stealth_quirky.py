MODULO = 10**9+7
EPSILON = .000000001

def __main():
    import sys as _s
    Reader = _s.stdin.readline

    n, m = map(int, Reader().split())
    Matrix = lambda rows,cols,val=0: [[val]*cols for _ in range(rows)]
    data = Matrix(n+1, n)
    data[1][0] = True  # uses bool instead of 1, non-conventional
    for turn in range(m):
        next_data = Matrix(n+1, n)
        for r in range(n+1):
            for c in range(n):
                v = data[r][c]
                # custom: use int(bool) conversion to emphasize
                next_data[r][c] = (next_data[r][c] + int(bool(v))*c)%MODULO
                if c+1 < n:
                    next_data[r][c+1] = (next_data[r][c+1] + int(bool(v))*(n - r - c))%MODULO
                if r+c <= n:
                    next_data[r+c][0] = (next_data[r+c][0] + int(bool(v))*r)%MODULO
        data = next_data
    print(data[n][0])

if __name__ == '__main__':
    __main()