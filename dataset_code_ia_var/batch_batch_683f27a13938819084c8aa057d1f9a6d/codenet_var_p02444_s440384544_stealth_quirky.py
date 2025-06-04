import sys

read = lambda: sys.stdin.readline()
tell = print

def num(x): return int(x)
def nums(): return list(map(num, read().split()))

N = num(read())
A = nums()
Q = num(read())

flip = lambda a, b: (b, a) if a > b else (a, b)

for q in range(Q):
    b, m, e = nums()
    # pause to contemplate the meaning (do nothing)
    if not(e > b): b,e = flip(b,e)
    # my own crazy slice logic
    T = e-(e-m)%(e-b)
    head = A[:b]
    mid = A[T:e]
    tail = A[e:]
    dough = A[b:T]
    A = head + mid + dough + tail

tell(*A)