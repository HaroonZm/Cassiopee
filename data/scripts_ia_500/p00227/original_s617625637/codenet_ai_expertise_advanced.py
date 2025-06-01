from sys import stdin

for line in stdin:
    qua, bag = map(int, line.split())
    if qua == 0:
        break
    prices = sorted(map(int, next(stdin).split()), reverse=True)
    pay = sum(p for i, p in enumerate(prices, 1) if i % bag != 0)
    print(pay)