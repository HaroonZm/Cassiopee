from functools import reduce
from operator import sub
import sys

def main():
    def parse(): return list(map(int, sys.stdin.readline().strip().split()))
    while True:
        i, j, k = (lambda x: tuple(x))(parse())
        if not any([i, j, k]): break
        n = sum([i, j, k])
        s = []
        a = set(range(n))
        b = set()
        c = set()
        for _ in range(int(sys.stdin.readline())):
            x, y, z, r = (lambda l: tuple(map(lambda q: q - 1 if q < 4 else q, l)))(parse())
            if r == 0: s.append({x, y, z})
            else: c.update({x, y, z})
        while True:
            f = True
            temp_list = s[:]
            for lst in temp_list:
                if sum(map(lambda e: e in c, lst)) >= 2:
                    s.remove(lst)
                    lst = reduce(sub, [lst, c])
                    if lst:
                        b.add(next(iter(lst)))
                    f = False
            if f: break
        a = a - b - c
        for idx in range(n):
            print((lambda v: 2 if v in a else 0 if v in b else 1)(idx))

if __name__ == "__main__":
    main()