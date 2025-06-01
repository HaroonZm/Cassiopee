while True:
    n = int(input())
    if n == 0:
        break
    magic = [[0]*n for _ in range(n)]
    r, c = 1, n//2
    for num in range(1, n*n+1):
        magic[r][c] = num
        nr, nc = r+1, c+1
        if nr == n:
            nr = 0
        if nc == n:
            nc = 0
        if magic[nr][nc]:
            r = r-1
            if r < 0:
                r = n-1
        else:
            r, c = nr, nc
    for row in magic:
        print(''.join(f'{x:4d}' for x in row).lstrip())