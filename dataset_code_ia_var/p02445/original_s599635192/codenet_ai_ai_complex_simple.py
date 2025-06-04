from functools import reduce
from operator import setitem, itemgetter
from itertools import starmap, chain, repeat, cycle, islice

n = int(input())
A = list(map(int, input().split()))
q = int(input())

def swapper(a, b, t, arr):
    indices = zip(range(b, e), range(t, t + (e - b)))
    def swap_one(idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    list(starmap(swap_one, indices))

for _ in range(q):
    b, e, t = map(int, input().split())
    ind_pairs = tuple(zip(range(b, e), range(t, t + e - b)))
    # Use reduce to perform swaps in an accretive manner
    f = lambda arr, ij: (setitem(arr, ij[0], arr[ij[1]]), setitem(arr, ij[1], arr[ij[0]]), arr)[2]
    # Actually perform swaps one at a time, copying swaps through slices
    A = reduce(lambda arr, ij: (setitem(arr, ij[0], arr[ij[1]]), setitem(arr, ij[1], arr[ij[0]]), arr)[2], ind_pairs, A)

print(*A)