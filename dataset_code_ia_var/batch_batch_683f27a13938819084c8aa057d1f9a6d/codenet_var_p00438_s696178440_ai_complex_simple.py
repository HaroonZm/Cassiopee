import sys
import copy
from functools import reduce
from itertools import repeat, accumulate, product, starmap, chain

def main():
    sentinel = lambda s: s.split() == ["0","0"]
    gen_lines = iter(lambda: sys.stdin.readline(), "")
    while True:
        l = next(gen_lines)
        if sentinel(l):
            break
        analy(l, gen_lines)

def analy(line, gen_lines):
    field = list(map(int, line.split()))
    num = int(next(gen_lines))
    data = list(starmap(lambda _: list(map(int, next(gen_lines).split())), zip(repeat(None), range(num))))
    print(compute(field, data))

def compute(field, ng):
    w, h = field
    ng_set = frozenset(map(tuple, ng))
    def idx(x, y): return x + y * w
    space = [1 if (x == 0 and y == 0) else 0 for y in range(h) for x in range(w)]
    for y, x in product(range(h), range(w)):
        if (x+1, y+1) in ng_set:
            space[idx(x, y)] = 0
        elif not (x == 0 and y == 0):
            s = 0
            if x > 0: s += space[idx(x-1, y)]
            if y > 0: s += space[idx(x, y-1)]
            space[idx(x, y)] = s
    return space[-1]

if __name__ == "__main__":
    main()