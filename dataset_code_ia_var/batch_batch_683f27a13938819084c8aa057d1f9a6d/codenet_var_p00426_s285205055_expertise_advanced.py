import sys
from functools import lru_cache
from operator import or_
from itertools import islice

sys.setrecursionlimit(1 << 20)

def resolve():
    input_stream = iter(sys.stdin.readline, '')
    next_input = lambda: next(input_stream)

    @lru_cache(maxsize=None)
    def toC(A: int, B: int, C: int) -> int:
        if not (A or B):
            return 0
        if C & 1:
            return toC(A >> 1, B >> 1, C >> 1)
        if B & 1:
            return toC(C >> 1, B >> 1, A >> 1) + toC((A | B | C) >> 1, 0, 0) + 1
        if A & 1:
            return toC(A >> 1, B >> 1, C >> 1) + 2 * toC((A | B | C) >> 1, 0, 0) + 2

    while True:
        # Fast input parsing, ignore blank lines.
        line = ''
        while line.strip() == '':
            line = next_input()
        n, m = map(int, line.split())
        if n == 0:
            return
        cup = [0] * 3
        for i in range(3):
            line = ''
            while line.strip() == '':
                line = next_input()
            stacks = list(map(int, line.split()))
            for s in islice(stacks, 1, None):
                cup[i] |= 1 << (s - 1)
        res = min(toC(*cup), toC(*cup[::-1]))
        print(res if res <= m else -1)

if __name__ == "__main__":
    resolve()