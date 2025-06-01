data = [(n, int(a), int(b)) for n, a, b in (input().split() for _ in range(9))]
for n, a, b in data:
    print(n, a + b, a * 200 + b * 300)