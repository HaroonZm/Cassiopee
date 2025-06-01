mv = [(-1,0),(0,1),(1,0),(0,-1)]

while True:
    n = int(input())
    if n == 0:
        break
    t1, t2, t3 = input().split()
    start = ord(t1) - ord('A')
    target = ord(t2) - ord('A')
    blocked = ord(t3) - ord('A')

    f = []
    for _ in range(n+1):
        rows = []
        for _ in range(3):
            cols = []
            for _ in range(3):
                cols.append(0.0)
            rows.append(cols)
        f.append(rows)

    f[0][start // 3][start % 3] = 1.0

    for step in range(1, n+1):
        for r in range(3):
            for c in range(3):
                for move in mv:
                    nr = r + move[0]
                    nc = c + move[1]
                    if nr < 0 or nr >= 3 or nc < 0 or nc >= 3 or (nr*3+nc) == blocked:
                        nr = r
                        nc = c
                    f[step][nr][nc] += f[step -1][r][c] / 4.0

    print(f[n][target // 3][target % 3])