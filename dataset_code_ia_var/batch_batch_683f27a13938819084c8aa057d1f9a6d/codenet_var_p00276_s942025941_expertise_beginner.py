q = int(input())

for i in range(q):
    c, a, n = map(int, input().split())
    cnt = 0

    if n <= c and n <= a:
        cnt = n
        c = c - cnt
        a = a - cnt

        if a <= c:
            if 2 * a >= c:
                cnt = cnt + (c // 2)
            else:
                cnt = cnt + a
                c = c - 2 * a
                cnt = cnt + (c // 3)
        else:
            cnt = cnt + (c // 2)
    elif a <= c and a <= n:
        cnt = a + (c - a) // 3
    else:
        cnt = c

    print(cnt)