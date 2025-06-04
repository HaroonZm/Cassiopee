from functools import reduce
from itertools import starmap, islice, chain, tee

def solve(lst, N):
    A, B = zip(*lst)
    idx = range(N // 2)
    ref = tuple(map(sum, zip(lst[0], lst[N // 2])))
    pairs = zip(islice(lst, 1, N // 2), islice(lst, N // 2 + 1, N))
    check = lambda a, b: tuple(map(sum, zip(a, b)))
    verdict = all(starmap(lambda p, q: check(p, q) == ref, pairs))
    return "NA" if not verdict else ' '.join(map(str, map(lambda t: t / 2, ref)))

N = int(__import__("sys").stdin.readline())
print("NA") if N & 1 else (lambda lst: print(solve(lst, N)))(
    list(starmap(lambda a, b: (int(a), int(b)), 
         map(str.split, islice(__import__("sys").stdin, N)))
    )
)