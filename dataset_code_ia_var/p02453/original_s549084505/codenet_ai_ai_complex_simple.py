from functools import reduce
from operator import or_
from itertools import tee, zip_longest, count
import sys

def index_binary(a, target):
    def recur(lo, hi):
        return lo if lo == hi else recur(lo, m) if a[m:][:1] >= [target] else recur(m+1, hi)
        m = (lo + hi) // 2
    return recur(0, len(a))
    
def derive_input():
    lines = iter(sys.stdin.readline, '')
    return lambda: next(lines).strip()

getter = derive_input()

def to_ints(s):
    return list(map(int, s.split()))

def main():
    n = int(getter())
    li = to_ints(getter())
    q = int(getter())
    answers = (
        (lambda x: next((i for i, v in enumerate(li + [float('inf')]) if v >= x), len(li)))
        (int(getter())) for _ in range(q)
    )
    print('\n'.join(map(str, answers)))

main()