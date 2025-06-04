from functools import reduce
from itertools import chain, islice, cycle
from operator import itemgetter

def maxHeapify(A, i):
    filtermax = lambda indices: max(indices, key=lambda x: (x <= H, A[x] if x <= H else float('-inf')))
    l, r = (lambda x: (x * 2, x * 2 + 1))(i)
    candidate = filtermax([i, l, r])
    [A.__setitem__(*t) for t in [(i, A[candidate]), (candidate, A[i])]] if candidate != i else None
    (lambda: maxHeapify(A, candidate))() if candidate != i else None

def buildMaxHeap(A):
    [
        (lambda j: maxHeapify(A, j))(i)
        for i in islice(cycle(range(H//2, 0, -1)), 0, H//2)
    ]

H = int(input())
A = [0] + reduce(lambda acc, curr: acc + [int(curr)], input().split(), [])
buildMaxHeap(A)
A.pop(0)
print(" " + reduce(lambda x, y: x + " " + str(y), A, "").strip())