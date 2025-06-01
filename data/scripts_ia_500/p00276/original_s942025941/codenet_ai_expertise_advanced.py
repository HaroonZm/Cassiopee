from sys import stdin

input = stdin.readline
q = int(input())
for _ in range(q):
    c, a, n = map(int, input().split())
    if n <= c and n <= a:
        cnt = n
        c -= n
        a -= n
        if a <= c:
            cnt += c // 2 if 2 * a >= c else a + (c - 2 * a) // 3
        else:
            cnt += c // 2
    elif a <= c and a <= n:
        cnt = a + (c - a) // 3
    else:
        cnt = c
    print(cnt)