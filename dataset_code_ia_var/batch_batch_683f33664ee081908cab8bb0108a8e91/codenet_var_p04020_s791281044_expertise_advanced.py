from functools import reduce
from operator import itemgetter

def process_sequence(seq):
    c = seq[0] // 2
    prev = seq[0] % 2
    for cur in seq[1:]:
        pairs, rem = divmod(cur, 2)
        if prev and rem:
            c += 1
            rem -= 1
        c += rem // 2
        prev = rem % 2
    return c

n = int(input())
seq = [int(input()) for _ in range(n)]
print(process_sequence(seq))