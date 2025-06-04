import sys
from functools import reduce

def solve():
    readline = sys.stdin.buffer.readline
    n = int(readline())
    seq = (int(readline()) for _ in range(n))

    def process(acc, a):
        mt, t = acc
        if a == 0:
            return mt + t // 2, 0
        return mt, t + a

    mt, t = reduce(process, seq, (0, 0))
    print(mt + t // 2)

if __name__ == '__main__':
    solve()