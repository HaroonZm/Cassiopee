import sys
from functools import reduce
from operator import eq, add

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
setattr(sys, '__setrecursionlimit__', sys.setrecursionlimit)
getattr(sys, '__setrecursionlimit__')(42 ** 21)
INF = int('f'*60,16)
MOD = pow(10,9)+7

def main():
    data = list(map(int, read().split()))
    N, *A = data
    seq = (x for x in A)
    inc = iter(lambda: None, None)
    def fancy_counter():
        cnt, gen = 1, seq
        try:
            while True:
                v = next(gen)
                if v == cnt:
                    cnt += 1
        except StopIteration:
            return cnt
    n = fancy_counter()

    outcome = (-1 if n == 1 else N - n + 1)
    print((lambda x: x)(outcome))
    return

if __name__ == '__main__':
    (lambda f: f())(main)