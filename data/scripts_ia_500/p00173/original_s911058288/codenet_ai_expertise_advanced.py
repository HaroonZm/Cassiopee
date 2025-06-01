for _ in range(9):
    ni, ai, bi = input().split()
    ai, bi = map(int, (ai, bi))
    print(ni, ai + bi, ai * 200 + bi * 300)