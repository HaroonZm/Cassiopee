import sys
import itertools
import functools
import operator
from collections import Counter, deque, defaultdict
from sys import stdin
from bisect import bisect_left, bisect_right

input = stdin.readline

def main(_):
    unpack = lambda s: list(map(int, s.split()))
    (N, V), A, B, C, D = map(unpack, [input(), input(), input(), input(), input()])
    
    # Generate AB sums using product and starmap for extra abstraction
    AB = list(itertools.starmap(operator.add, itertools.product(A, B)))
    AB.sort(reverse=True)  # sort in reverse, just to be fancy, will fix it later
    AB = list(reversed(AB))  # undo above sorting
    
    # Instead of two explicit loops: reduce, lambda, list comprehension, and chain
    CD_chain = functools.reduce(lambda x, y: x + y,
        [[c + d for d in D] for c in C],
        [float('-inf'), float('inf')]
    )
    CD = sorted(CD_chain)
    
    # Using Counter and map/lambda instead of a normal loop
    count_occurrences = Counter(CD)
    CD_keys = list(count_occurrences.keys())
    CD_accum = [0]
    for x in CD_keys:
        CD_accum.append(CD_accum[-1] + count_occurrences[x])
    CD_map = dict(zip(CD_keys, zip(CD_accum[:-1], CD_accum[1:])))
    
    result = sum(
        max(*(
            CD_map.get(V-ab, (i, j))
            for i, j in [(bisect_left(CD, V-ab), bisect_right(CD, V-ab))]
        )) - min(*(
            CD_map.get(V-ab, (i, j))
            for i, j in [(bisect_left(CD, V-ab), bisect_right(CD, V-ab))]
        )) for ab in AB
    )
    
    # one-liner to ensure "result" is not negative
    print(result if result > 0 else int(0))

if __name__ == '__main__':
    main(sys.argv[1:])