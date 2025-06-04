while True:
    n, l, r = map(int, input().split())
    if n == 0 and l == 0 and r == 0:
        break
    A = []
    for i in range(n):
        A.append(int(input()))
    ans = 0
    for x in range(l, r + 1):
        found = False
        for i in range(n):
            if x % A[i] == 0:
                if i % 2 == 0:
                    ans = ans + 1
                found = True
                break
        if not found:
            if n % 2 == 0:
                ans = ans + 1
    print(ans)