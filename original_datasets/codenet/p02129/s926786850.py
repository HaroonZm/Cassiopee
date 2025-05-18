N = int(input())
C = [0]*6
S = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
L = [1, 2, 2, 3, 3, 2]
P = []
init = [0, 1, 2]
for i in range(N):
    w, *A = map(int, input().split())
    state = init[:]
    for a in A:
        if a:
            state[1], state[2] = state[2], state[1]
        else:
            state[0], state[1] = state[1], state[0]
    j = S.index(state)
    C[j] += 1
    if C[j] >= L[j]:
        print('yes')
        exit(0)
    P.append(state)

# case: "L <= [0, 1, 1, 2, 2, 1]"
from itertools import permutations
for p in permutations(P):
    s = init[:]
    for q in p:
        s[0], s[1], s[2] = s[q[0]], s[q[1]], s[q[2]]
    if s == init:
        print('yes')
        exit(0)
print('no')