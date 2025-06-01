a, b, x = map(int, input().split())
if a / 2 < b:
    q, r = divmod(x, 1000)
    cost = a * (q + (r > 0 if a < b or r > 500 else 0)) + (b if r and r <= 500 and a >= b else 0)
else:
    q, r = divmod(x, 500)
    cost = b * (q + (r > 0))
print(cost)