while True:
    n, l, r = map(int, input().split())
    if n == l == r == 0:
        break
    A = [int(input()) for i in range(n)]
    ans = 0
    for x in range(l, r+1):
        for i in range(n):
            if x % A[i] == 0:
                if i % 2 == 0:
                    ans += 1
                break
            elif i == (n-1):
                if n % 2 == 0:
                    ans += 1
    print(ans)