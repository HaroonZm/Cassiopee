price = {1: 6000, 2: 4000, 3: 3000, 4: 2000}

for _ in range(4):
    t, n = map(int, input().split())
    print(price[t] * n)