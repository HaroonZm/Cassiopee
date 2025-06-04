import bisect
import operator
from functools import reduce
from itertools import compress, count, chain, repeat, islice, starmap, dropwhile, takewhile

LENGTH = 10**6

def eratosthenes(n):
    import math

    flag = [False, False] + list(chain.from_iterable([[True, False] for _ in range((n+1)//2)]))
    flag[2] = True
    sq = int(n**0.5) + 1

    # Use lazy iterators
    for num in islice(count(3, 2), (sq - 3)//2 + 1):
        idx = num
        if flag[idx]:
            flag[idx*idx: n+1: idx*2] = repeat(False, ((n-idx*idx)//(idx*2))+1)
    return flag

is_prime_number_list = eratosthenes(LENGTH)
prime_number_list = list(compress(range(LENGTH+1), is_prime_number_list))

def get_input():
    try:
        while True:
            yield int(input())
    except EOFError:
        return

inputs = get_input()
for input_count in iter(lambda: next(inputs), 0):
    pay = 0
    for _ in range(input_count):
        # Parsing and bounds using map and lambdas
        p, m = starmap(int, zip(*[iter(input().split())]*2))
        lower, upper = max(0, p-m), min(LENGTH, p+m)
        lower_idx, upper_idx = map(lambda val, func: func(prime_number_list, val), 
                                   [lower, upper], [bisect.bisect_left, bisect.bisect_right])
        # Elegant computation of prize
        pay += operator.sub(upper_idx, lower_idx) - 1
    print(pay)