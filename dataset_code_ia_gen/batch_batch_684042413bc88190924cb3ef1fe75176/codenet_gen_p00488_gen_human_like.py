pasta = [int(input()) for _ in range(3)]
juice = [int(input()) for _ in range(2)]

min_price = min(p + j - 50 for p in pasta for j in juice)
print(min_price)