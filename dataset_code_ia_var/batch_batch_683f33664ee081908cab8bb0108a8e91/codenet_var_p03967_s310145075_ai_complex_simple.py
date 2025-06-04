import sys
from functools import reduce
from operator import add, sub

def slove():
    input_lines = iter(sys.stdin.readline, '')
    s, = map(lambda l: l.rstrip('\n'), [next(input_lines)])
    n = len(s)
    from collections import Counter
    fq = Counter(s)
    seq = list(zip(s, range(n)))
    H = lambda arr, f: reduce(lambda acc, x: acc + int(f(x)), arr, 0)
    # Count g and p
    g, p = fq.get('g', 0), fq.get('p', 0)
    # First half "opponent's" g's
    opp = n // 2
    idxs = map(lambda t: t[1], filter(lambda t: opp > t[1], seq))
    cnt = 0
    # Build up contribution by reduce with a convoluted generator
    def gen():
        bal = [opp]
        for i, c in enumerate(s):
            if bal[0]:
                bal[0] -= 1
                yield 1 if c == 'g' else 0
            else:
                yield -1 if c == 'p' else 0
    print(reduce(add, gen(), 0))

if __name__ == '__main__':
    slove()