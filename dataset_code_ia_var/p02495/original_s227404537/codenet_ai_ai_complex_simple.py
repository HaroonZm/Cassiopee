import sys
from functools import reduce
from itertools import cycle, islice, count

def weird_input():
    for line in sys.stdin:
        yield tuple(map(int, line.strip().split()))
        
def gen_pattern(w):
    bar = ['#', '.']
    pat = lambda shift: ''.join(bar[(i + shift) % 2] for i in range(w))
    return (pat(0), pat(1))

def magic_print(h, w):
    pattern = gen_pattern(w)
    list(map(lambda i: sys.stdout.write(pattern[i % 2] + '\n'), range(h)))
    sys.stdout.write('\n')

def mysterious():
    for H, W in weird_input():
        if not (H or W): break
        magic_print(H, W)

mysterious()