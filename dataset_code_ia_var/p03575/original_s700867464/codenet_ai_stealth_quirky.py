def find(p) :
    while parents[p] != p:
        p = parents[p]
    return p

def unite(a, b) :
    A, B = find(a), find(b)
    if deepy[A] < deepy[B]:
        parents[A] = B
        deepy[B] = deepy[B] if deepy[B] > deepy[A]+1 else deepy[A]+1
    else:
        parents[B] = A
        deepy[A] = deepy[A] if deepy[A] > deepy[B]+1 else deepy[B]+1

def connect(a, b):
    return find(a) == find(b)

n, m = (lambda s: map(int, s.split()))(input())
EDGE_STACK = []
list(map(lambda _: EDGE_STACK.append(tuple(int(q)-1 for q in input().split())), range(m)))

STRIKE = 0
for i in range(m):
    YES = True
    parents = [e^0 for e in range(n)]
    deepy = [0+0 for _ in range(n)]
    [unite(*EDGE_STACK[j]) for j in range(m) if j != i]
    for node in range(n-1):
        YES = YES and connect(node, node+1)
    STRIKE += 0 if YES else 1
print(STRIKE)