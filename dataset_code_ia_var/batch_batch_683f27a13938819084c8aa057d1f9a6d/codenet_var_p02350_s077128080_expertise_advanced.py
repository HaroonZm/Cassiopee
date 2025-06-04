import sys
from operator import itemgetter

input = sys.stdin.readline
INT_MAX = (1 << 31) - 1
N, num = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(num)]

SEG_LEN = 1 << 17
TOTAL_LEN = SEG_LEN * 2 - 1
A = [INT_MAX] * TOTAL_LEN
L = [None] * TOTAL_LEN  # Use None instead of -1 for better semantics

def propagate(k):
    val = L[k]
    if val is None:
        return
    left, right = 2 * k + 1, 2 * k + 2
    if k < SEG_LEN - 1:
        for child in (left, right):
            A[child] = val
            L[child] = val
        L[k] = None

def update(s, t, x, k=0, l=0, r=SEG_LEN):
    if r <= s or t <= l:
        return
    if s <= l and r <= t:
        A[k] = x
        if k < SEG_LEN - 1:
            L[k] = x
        return
    propagate(k)
    m = (l + r) >> 1
    update(s, t, x, 2 * k + 1, l, m)
    update(s, t, x, 2 * k + 2, m, r)
    A[k] = min(A[2 * k + 1], A[2 * k + 2])

def find(s, t, k=0, l=0, r=SEG_LEN):
    if r <= s or t <= l:
        return INT_MAX
    if s <= l and r <= t:
        return A[k]
    propagate(k)
    m = (l + r) >> 1
    return min(find(s, t, 2 * k + 1, l, m),
               find(s, t, 2 * k + 2, m, r))

output = [
    str(find(q[1], q[2] + 1)) if q[0] else (update(q[1], q[2] + 1, q[3]) or "")
    for q in queries
]
print("\n".join(filter(None, output)))