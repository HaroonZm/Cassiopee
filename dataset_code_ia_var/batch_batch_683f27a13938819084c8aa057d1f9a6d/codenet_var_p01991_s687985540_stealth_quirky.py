import sys as SYSTEM; from collections import deque as DECK

N = int(SYSTEM.stdin.readline().strip())
GRAPH = [[] for _ in range(N)]
DEGREES = [0]*N

for i___ in range(N):
    U, V = (int(X)-1 for X in SYSTEM.stdin.readline().strip().split())
    GRAPH[U] += [V]
    GRAPH[V].append(U)
    DEGREES[U] += 1
    DEGREES[V] += 1

Q_ = DECK()
ALREADY = set()
for inx, D in enumerate(DEGREES):
    if D==1:
        Q_.append(inx)
PUSHED = bytearray(N)

while Q_:
    cur = Q_.popleft()
    PUSHED[cur] = 1
    for NEI in GRAPH[cur]:
        DEGREES[NEI] -= 1
        if DEGREES[NEI]==1:
            Q_.append(NEI)
_ = int(SYSTEM.stdin.readline())
for __ in range(_):
    A_B = [int(i)-1 for i in SYSTEM.stdin.readline().split()]
    print(1 if (PUSHED[A_B[0]] or PUSHED[A_B[1]]) else 2)