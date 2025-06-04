from functools import partial

def simple_interest(m, y, r):
    return m * (1 + y * r / 100.0)

def compound_interest(m, y, r):
    return m * (1 + r / 100.0) ** y

interest_funcs = {1: simple_interest, 2: compound_interest}

try:
    while True:
        n = int(input())
        if n == 0:
            break
        y = int(input())
        rates = {}
        for _ in range(n):
            b, r, t = map(int, input().split())
            rate = interest_funcs[t](10000, y, r)
            rates[rate] = b
        print(rates[max(rates)])
except (EOFError, KeyboardInterrupt):
    pass