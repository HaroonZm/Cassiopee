n, m = map(int, input().split())
flag = []
for _ in range(n):
    flag.append(list(input()))
ans = 10**9
for white in range(1, n-1):
    for blue in range(1, n-1):
        red = n - white - blue
        if red <= 0:
            continue
        cnt = 0
        i = 0
        while i < white:
            j = 0
            while j < m:
                if flag[i][j] != "W":
                    cnt += 1
                j += 1
            i += 1
        i = 0
        while i < blue:
            j = 0
            while j < m:
                if flag[white + i][j] != "B":
                    cnt += 1
                j += 1
            i += 1
        i = 0
        while i < red:
            j = 0
            while j < m:
                if flag[white + blue + i][j] != "R":
                    cnt += 1
                j += 1
            i += 1
        if cnt < ans:
            ans = cnt
print(ans)