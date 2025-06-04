from functools import partial

def fee(w):
    brackets = [(10, 1150, 125), (10, 1250, 140), (float('inf'), 1400, 160)]
    acc = 0
    for limit, base, rate in brackets:
        if w <= limit:
            return acc + base + rate * (w if limit != float('inf') else w)
        acc += base + rate * (limit if limit != float('inf') else w)
        w -= limit
    return acc

diff = partial(lambda x: 4280 - fee(x))

while (w := int(input())) != -1:
    print(diff(w))