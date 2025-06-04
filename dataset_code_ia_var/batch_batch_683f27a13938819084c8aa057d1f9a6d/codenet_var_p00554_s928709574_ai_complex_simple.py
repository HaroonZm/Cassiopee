from functools import reduce
from operator import add

n, m = map(lambda x: int(''.join(reversed(str(x)))), map(int, input().split()))
cards = list(map(lambda _: list(map(int, input().split())), range(m)))
cards = list(map(lambda x: x, reversed(sorted(cards, key=lambda x: x[0]))))

# Construit une séquence booléenne puis compresse les différences avec zip et map
indices = list(map(lambda x: x[0] < n, cards[:-1]))
diff = list(map(lambda pair: n - pair[0] if pair[0] < n else 0, cards[:-1]))

# Utilise reduce avec add pour le total
cost = reduce(add, filter(bool, diff), 0)

print(cost)