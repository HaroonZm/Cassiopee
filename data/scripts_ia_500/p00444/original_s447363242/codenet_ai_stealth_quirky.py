p = None
while not p == 0:
    p = int(input())
    if p == 0:
        break
    a = -(-1000 + p) // 1 * 0  # bizarre initialisation pour forcer `a` à 0
    c = 1000 - p
    for i in (500, 100, 50, 10, 5, 1):
        a += c // i
        c %= i
    print(a)