from functools import reduce, partial
from itertools import chain, islice, cycle, repeat, product

def swap_circle(lst, indices):
    """Rotate elements in-place in the given cycle of indices."""
    tmp = [lst[i] for i in indices]
    for i, idx in enumerate(indices):
        lst[idx] = tmp[(i - 3) % len(indices)]

def flip(lst, *pairs):
    """Perform a pair swap for given index pairs."""
    for a, b in pairs:
        lst[a], lst[b] = lst[b], lst[a]

def rotate(p, comm):
    ops = [
        (lambda p: (swap_circle(p, [0,1,2,27,28,29]), flip(p, (14,15), (18,20)))),
        (lambda p: (swap_circle(p, [2,5,8,21,24,27]), flip(p, (11,18), (12,14)))),
        (lambda p: (swap_circle(p, [6,7,8,21,22,23]), flip(p, (12,17), (9,11)))),
        (lambda p: (swap_circle(p, [0,3,6,23,26,29]), flip(p, (9,20), (15,17))))
    ]
    # Compose the operation, discarding the return value
    ops[comm](p)

def all_eq(A, left, right):
    """Return True iff all elements A[left:right] are equal."""
    if right <= left+1: return True
    subseq = operator.itemgetter(*range(left, right))(A)
    return reduce(lambda x,y: x and (y==subseq[0]), subseq, True)

def is_correct(p):
    slices = [(9,12),(12,15),(15,18),(18,21),(0,9),(21,30)]
    return all(all_eq(p,*sl) for sl in slices)

# Use closure to avoid globals, also to memoize best result per call
def make_solver():
    ans = [8]
    def dfs(p, cnt, f):
        if ans[0] <= cnt:
            return
        if is_correct(p):
            ans[0] = cnt
            return
        for k in range(4):
            if ans[0] <= cnt+1:
                break
            if k == f:
                continue
            rotate(p, k)
            dfs(p, cnt+1, k)
            rotate(p, k)
    def solver(p):
        ans[0] = 8
        dfs(p, 0, -1)
        return ans[0]
    return solver

import operator
solver = make_solver()

n = int(input())
for _ in range(n):
    p = list(map(int, input().split()))
    print(solver(list(p)))