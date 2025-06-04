from itertools import product
from math import floor

PRICING_RULES = [
    {'base': 380, 'pack': 5, 'discount': 0.8},
    {'base': 550, 'pack': 4, 'discount': 0.85},
    {'base': 850, 'pack': 3, 'discount': 0.88}
]

def price(num_unit, shop):
    rule = PRICING_RULES[shop]
    packs, remainder = divmod(num_unit, rule['pack'])
    return rule['base'] * (packs * rule['pack'] * rule['discount'] + remainder)

def valid_combinations(q):
    bounds = (q // 200 + 1, q // 200 + 1, q // 200 + 1)
    return (
        (a, b, c)
        for a, b, c in product(range(bounds[0]), range(bounds[1]), range(bounds[2]))
        if a * 200 + b * 300 + c * 500 == q
    )

while True:
    try:
        quantity = int(raw_input())
    except EOFError:
        break
    if quantity == 0: break
    prices = (
        price(a, 0) + price(b, 1) + price(c, 2)
        for a, b, c in valid_combinations(quantity)
    )
    print(int(min(prices)))