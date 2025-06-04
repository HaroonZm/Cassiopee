import sys
import functools
import itertools
import collections

freq_op = lambda A: list(map(dict(collections.Counter(A)).get, A))

for s in sys.stdin:
    try:
        n = int(s)
        if not n:
            break
        A = list(map(int, input().split()))
        cnt = 0
        while True:
            B = [collections.Counter(A)[a] for a in A]
            cnt = functools.reduce(lambda x, _: x + 1, range(1), cnt)
            if all(map(lambda x, y: x == y, B, A)):
                break
            else:
                A = list(itertools.starmap(lambda x, _: x, zip(B, A)))
        print(cnt)
        print(*(a for a in A))
    except:
        pass