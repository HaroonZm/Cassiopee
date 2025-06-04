from functools import reduce
from operator import add

def accumulative_slice(lst, indices):
    return reduce(add, (lst[start:end] for start, end in indices), [])

n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    b, e, t = map(int, input().split())
    L = len(a)
    # Generate slice boundaries as a list of (start, end) using sorted positions and modulo arithmetic
    def do_swap(b, e, t):
        parts = [(0,0)]
        if t > b:
            parts = [(0,b), (t, t+e-b), (e, t), (b, e), (t+e-b, L)]
        else:
            parts = [(0, t), (b,e), (e, e+b-t), (t, b), (e+b-t, L)]
        slices = [a[start:end] for start,end in parts]
        return [item for sub in slices for item in sub]
    a = do_swap(b,e,t)
print(*a)