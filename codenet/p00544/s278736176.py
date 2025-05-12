n, m = map(int, input().split())

flag = []
for _ in range(n):
    string = list(input())
    flag.append(string)

ans = 10**9
for white in range(1, n-1):
    for blue in range(1, n-1):
        red = n - white - blue
        if red <= 0:
            continue

        cnt = 0
        for i in range(white):
            for j in range(m):
                if flag[i][j] != "W":
                    cnt += 1

        for i in range(blue):
            for j in range(m):
                if flag[white+i][j] != "B":
                    cnt += 1

        for i in range(red):
            for j in range(m):
                if flag[white+blue+i][j] != "R":
                    cnt += 1

        if ans > cnt:
            ans = cnt

print(ans)