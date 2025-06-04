for _ in range(int(input())):
    n, d = map(int, input().split())
    if n % 2 == 0:
        print(n * 127 - d)
    else:
        print((n - 1) * 127 + d)