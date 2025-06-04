from collections import deque

X = list()
Y = list()
for n in range(3):
    A = deque()
    [A.appendleft(input().split()[::-1]) for __ in range(8)]
    A = sorted(list(A))
    X += A[:2]
    Y.extend(A[2:4])
else:
    X += sorted(Y)[:2]

while X:
    elem = X.pop(0)
    print(' '.join(elem[::-1]))