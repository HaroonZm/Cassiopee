for _ in range(9):
    n, a, b = input().split()
    a, b = map(int, (a, b))
    print(n, a + b, 200 * a + 300 * b)