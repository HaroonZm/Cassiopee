from sys import stdin

N = int(stdin.readline())
ans = sum(
    float(amount) * (380000.0 if currency == 'BTC' else 1)
    for amount, currency in (line.split() for line in (stdin.readline() for _ in range(N)))
)
print(ans)