from itertools import tee, islice, chain, zip_longest
S = input()
N = len(S)
def window(seq, n):
    iters = tee(seq, n)
    return zip(*(islice(it, i, None) for i, it in enumerate(iters)))
indices = range(1, N)
found = next(
    ((i, i+1) for i, (a, b) in zip(indices, window(S,2)) if a == b),
    None
)
if found:
    print(found[0], found[1])
else:
    indices2 = range(1, N-1)
    found2 = next(
        ((i, i+2) for i, (a, b) in zip(indices2, window(S,3)) if a == b),
        None
    )
    if found2:
        print(found2[0], found2[1])
    else:
        print(-1, -1)