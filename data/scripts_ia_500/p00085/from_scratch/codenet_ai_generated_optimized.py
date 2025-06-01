while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    res = 0
    for i in range(2, n + 1):
        res = (res + m) % i
    print(res + 1)