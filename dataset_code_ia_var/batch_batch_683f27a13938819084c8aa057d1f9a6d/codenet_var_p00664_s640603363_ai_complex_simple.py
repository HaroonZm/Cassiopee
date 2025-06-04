from functools import reduce
from operator import xor, or_
from itertools import starmap, repeat, count, cycle
from collections import defaultdict
import sys

# Helper function to generate False bool array, via map and lambdas
def false_array(length):
    return list(map(lambda _: False, range(length)))

# Generate counters using generators
def counter(init):
    return [init]

def decrement(cnt):
    cnt[0] -= 1

def get(cnt):
    return cnt[0]

# Read all input at once
data = sys.stdin.read().split()
it = iter(data)
while True:
    r = int(next(it))
    c = int(next(it))
    q = int(next(it))
    if not r: break

    ql = [list(map(int, (next(it), next(it), next(it)))) for _ in range(q)]
    ql = list(reversed(ql))

    r_used = false_array(r)
    c_used = false_array(c)
    r_cnt = counter(c)
    c_cnt = counter(r)
    ans = [0]

    # Define action via nested functions and lambdas
    def do_query(a, b, o):
        (lambda
            ru, cu, rc, cc, res:
                [
                    (
                        [
                            ru.__setitem__(b, True),
                            decrement(cc),
                            res.__setitem__(0, res[0] + get(rc)) if o else None
                        ]
                        if not ru[b] else None
                    )
                    if a == 0 else
                    (
                        [
                            cu.__setitem__(b, True),
                            decrement(rc),
                            res.__setitem__(0, res[0] + get(cc)) if o else None
                        ]
                        if not cu[b] else None
                    )
                ][0]
        )(r_used, c_used, r_cnt, c_cnt, ans)

    # Run all queries
    list(starmap(do_query, ql))
    print(ans[0])