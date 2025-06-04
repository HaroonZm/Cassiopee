from functools import reduce
from sys import stdin

coins = (500, 100, 50, 10, 5, 1)

for line in stdin:
    if (a := int(line.strip())) == 0:
        break
    print(sum(divmod(r, coin)[0] for coin, r in zip(coins, 
          [reduce(lambda x, y: x % y, coins[:i+1], 1000 - a) for i in range(len(coins))])))