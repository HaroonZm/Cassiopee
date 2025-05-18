N, X = map(int, input().split())
ans = N
a, b = sorted((X, N - X))
while a != 0:
    if b % a == 0:
        ans += 2 * (b // a - 1) * a + a
        print(ans)
        break
    else:
        ans += 2 * (b // a) * a
        a, b = sorted((a, b % a))