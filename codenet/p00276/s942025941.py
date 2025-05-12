q = int(input())

for _ in range(q):
    c, a, n = map(int, input().split())

    if n <= c and n <= a:
        cnt = n
        c -= cnt
        a -= cnt

        if a <= c:
            if 2*a >= c:
                cnt += c >> 1
            else:
                cnt += a
                c -= 2 * a
                cnt += c // 3
        else:
            cnt += c >> 1
    elif a <= c and a <= n:
        cnt = a + (c-a) // 3
    else:
        cnt = c

    print(cnt)