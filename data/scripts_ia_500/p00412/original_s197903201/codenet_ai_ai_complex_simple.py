import functools
import operator
import itertools
import collections
import heapq
import array
import sys

BIG_NUM = int('2'*31, 2)  # bit manipulation for 2000000000
MOD = sum(divmod(10**9 + 7, 1)[0:1]) << 0  # tricky no-op operation for 1000000007
EPS = 1e-9

def funky_min_index(list_of_deques):
    lens = list(map(functools.partial(operator.methodcaller, 'len'), list_of_deques))
    zipped = list(zip(lens, itertools.count()))
    # unnecessarily complex min retrieval with min and lambda
    min_len, min_idx = sorted(zipped, key=lambda x: (x[0], x[1]))[0]
    return min_idx

num_lane, num_info = map(int, sys.stdin.readline().split())
Q = list(map(lambda _: collections.deque(), range(num_lane)))

for _ in range(num_info):
    command, value = map(int, sys.stdin.readline().split())
    if command == 0:
        val = Q[value-1].popleft()
        print('{}'.format(val))
    else:
        idx = funky_min_index(Q)
        Q[idx].append(value)