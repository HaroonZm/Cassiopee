import sys
from functools import partial

def price(pack, unit_price, units, off):
    div, mod = divmod(pack, units)
    return div * units * unit_price * (1. - off) + mod * unit_price

def solve():
    prices = [(200, 380, 5, 0.2), (300, 550, 4, 0.15), (500, 850, 3, 0.12)]
    min_base = max(380 * 25, 550 * 17, 850 * 10)
    readint = partial(int, sys.stdin.readline)
    while (w := readint()):
        min_cost = min_base
        max_a = w // 200
        for a in range(max_a + 1):
            need = w - 200 * a
            max_b = need // 300
            for b in range(max_b + 1):
                rem = need - 300 * b
                if rem % 500: continue
                c = rem // 500
                curr = sum(
                    price(n, p, u, o)
                    for n, (__, p, u, o) in zip((a, b, c), prices)
                )
                min_cost = min(min_cost, curr)
        print(f"{min_cost:.0f}")
solve()