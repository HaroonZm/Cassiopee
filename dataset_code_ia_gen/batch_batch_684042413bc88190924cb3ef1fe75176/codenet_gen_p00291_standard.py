c = list(map(int, input().split()))
coins = [1, 5, 10, 50, 100, 500]
total = sum(c[i]*coins[i] for i in range(6))
print(1 if total >= 1000 else 0)