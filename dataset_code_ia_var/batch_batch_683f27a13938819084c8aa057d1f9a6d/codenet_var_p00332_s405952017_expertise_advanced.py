from functools import partial

def wa(y):
    eras = [
        (1912, 'M', 1867),
        (1926, 'T', 1911),
        (1989, 'S', 1925),
        (float('inf'), 'H', 1988)
    ]
    for end, prefix, offset in eras:
        if y < end:
            return f"{prefix}{y - offset}"
        
def sei(e, y):
    offsets = [1867, 1911, 1925, 1988]
    return y + offsets[e-1]

e, y = map(int, input().split())
print(wa(y) if e == 0 else sei(e, y))