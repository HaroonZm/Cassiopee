for _ in range(9):
    name, p, a = input().split()
    p, a = map(int, (p, a))
    print(name, p + a, p * 200 + a * 300)