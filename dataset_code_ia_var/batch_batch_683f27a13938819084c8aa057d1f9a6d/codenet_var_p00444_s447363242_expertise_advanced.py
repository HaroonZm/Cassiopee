from sys import stdin

def coin_change():
    denominations = (500, 100, 50, 10, 5, 1)
    for line in stdin:
        if not line.strip():
            continue
        p = int(line)
        if p == 0:
            break
        c = 1000 - p
        print(sum(divmod(c, d)[0] if divmod(c := divmod(c, d)[1] if c >= d else c, d) else 0 for d in denominations))

coin_change()