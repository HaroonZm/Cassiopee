from functools import reduce
from operator import add
from itertools import combinations

def weird_count(k, s):
    return sum(1 for combo in combinations(range(1, 10), k) if sum(combo) == s)

import sys
if sys.version_info[0] < 3:
    input_func = raw_input
else:
    input_func = input

while True:
    try:
        n, S = map(int, input_func().split())
        if n == 0 and S == 0:
            break
        print(reduce(add, map(lambda x: 1 if sum(x) == S else 0, combinations(range(1, 10), n)), 0))
    except EOFError:
        break