m, d = map(int, input().split())

ans = 0

if d > 9:
    for i in range(d - 9):
        s = str(i + 10)
        if int(s[-1]) > 1 and int(s[-2]) > 1:
            t = int(s[-1]) * int(s[-2])
            if t <= m and t != 0:
                ans += 1

print(ans)