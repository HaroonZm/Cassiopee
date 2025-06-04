from functools import reduce
from itertools import accumulate, islice, tee, chain
from operator import mul, eq, ge

mod = 10**9 + 7
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# Compute a and b using accumulator and functools
def left_scan(arr):
    s = arr[0]
    res = [None] * n
    for i, x in enumerate(arr):
        if x == 1:
            res[i] = 1
        else:
            if s != x:
                s = x
            res[i] = s if i == 0 or x != 1 else res[i]
    return res

def right_scan(arr):
    s = arr[-1]
    res = [None] * n
    for i, x in enumerate(reversed(arr)):
        idx = n-1-i
        if x == 1:
            res[idx] = 1
        else:
            if s != x:
                s = x
            res[idx] = s if i == 0 or x != 1 else res[idx]
    return res

a = list(map(lambda x: -1 if x is None else x, left_scan(arr1)))
b = list(map(lambda x: -1 if x is None else x, right_scan(arr2)))

# Compose c using a functional but arcane approach
def combine(a, b):
    c = []
    xs = zip(a, b, arr1, arr2)
    for ai, bi, arri, arri2 in xs:
        if ai == -1 and bi == -1:
            c.append(-1)
        elif ai == -1:
            c.append(bi if arri >= bi else float('nan'))
        elif bi == -1:
            c.append(ai if arri2 >= ai else float('nan'))
        else:
            c.append(ai if ai == bi else float('nan'))
    return c

c = combine(a, b)
if any(isinstance(x, float) for x in c):
    print(0)
else:
    # Find the ranges where c == -1 using tee and enumerate
    indices = list(range(n))
    grouped = []
    current = []
    for idx, val in zip(indices, c):
        if val == -1:
            current.append(idx)
        else:
            if current:
                grouped.append(current)
                current = []
    if current:
        grouped.append(current)
    # Now calculate the product of min(l, r) for each such range
    ans = 1
    for segment in grouped:
        l = c[segment[0]-1] if segment[0] > 0 else 0
        r = c[segment[-1]+1] if segment[-1] < n-1 else 0
        val = min(l, r)
        ans = pow(val, len(segment), mod) * ans % mod if val > 0 else 0
    print(ans)