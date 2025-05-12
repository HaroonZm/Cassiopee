dd = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
while 1:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    S = [input() for i in range(h)]

    count = {}
    for i in range(h):
        for j in range(w):
            for dx, dy in dd:
                s = S[i][j]
                count[s] = count.get(s, 0) + 1
                x = (j + dx) % w; y = (i + dy) % h
                while x != j or y != i:
                    s += S[y][x]
                    count[s] = count.get(s, 0) + 1
                    x = (x + dx) % w; y = (y + dy) % h
    ans = min(count, key=lambda x: (-len(x)*(count[x]>1), x))
    print(ans*(len(ans)>1)or 0)