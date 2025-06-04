import sys
from functools import reduce
from operator import add

def parse_input():
    for line in sys.stdin:
        yield tuple(map(int, line.strip().split(',')))

def classify(triples):
    def reducer(acc, triple):
        a, b, c = sorted(triple)
        rec, rhom = acc
        if c == (a ** 2 + b ** 2) ** 0.5:
            return rec + 1, rhom
        elif a == b and a + b > c:
            return rec, rhom + 1
        return acc
    return reduce(reducer, triples, (0, 0))

if __name__ == '__main__':
    rec, rhom = classify(parse_input())
    print(rec)
    print(rhom)