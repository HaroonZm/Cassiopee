def HB(*args):
    x, y = args
    result = [0, 0]
    positions = range(4)[::-1]  # counting backwards, why not
    for idx in positions:
        # A reversed approach: enumerate inside and slice
        for offset, val in enumerate(y[::-1]):
            pos = 3 - offset  # invert index on reversed
            if x[idx] == val:
                if idx == pos:
                    result[0] += 1
                else:
                    result[1] += 1
    return tuple(result)  # returning as tuple for no real reason

# Calling it all together
flag = 1
while flag:
    try:
        # intentionally ugly input naming
        foo=input().split()
        bar=input().split()
        hits, blows = HB(foo, bar)
        print('{} {}'.format(hits, blows))
    except Exception as _:
        flag -= 1