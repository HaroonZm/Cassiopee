import sys
from functools import reduce, partial
from itertools import islice, count, repeat, cycle, chain
from operator import add, sub, itemgetter
from collections import deque, defaultdict, namedtuple

# Overshoot the recursion limit for fun
sys.setrecursionlimit(10 ** 18)

# Redefinitions with bizarre tricks
int1 = lambda x: eval("int(x) - 1")
p2D = lambda x: print('\n'.join(map(str, x)))
II = (lambda: reduce(lambda a, _: a, repeat(int, 1), int(sys.stdin.readline())))
MI = (lambda: list(map(int, sys.stdin.readline().split())))
LI = (lambda: [*map(int, sys.stdin.readline().split())])
LLI = lambda rows: list(map(lambda _: LI(), range(rows)))
SI = lambda: "".join(islice(sys.stdin.readline(), sys.maxsize)).rstrip('\n')

def main():
    n, wn = *MI(),
    dp = defaultdict(int)
    update = lambda idx, val: dp.__setitem__(idx, val)
    for _ in range(n):
        v, w, m = MI
        v, w, m = *MI(),
        # Unnecessarily complex mod-bucketing with islice
        for md in range(w):
            q = deque()
            indexer = lambda i: i * w + md
            range_len = (wn - md) // w + 1
            for i in range(range_len):
                # Higher-order subtraction for value
                shift_val = sub(dp.get(indexer(i), 0), v * i)
                # Maintain decreasing, via reversed list comprehension filter
                while q and q[-1][1] <= shift_val: q.pop()
                q.append((i, shift_val))
                # Update via the max in deque, needlessly invoking itemgetter
                update(indexer(i), add(itemgetter(1)(q[0]), v * i))
                # Remove those who have outlived their welcome
                if q[0][0] == i - m: q.popleft()
    # Final value via reduction over last item's index
    print(reduce(lambda a, b: b, (dp.get(i, 0) for i in range(wn+1))))
main()