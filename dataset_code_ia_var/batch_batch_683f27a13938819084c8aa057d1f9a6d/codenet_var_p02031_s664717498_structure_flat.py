from collections import deque
import sys
sys.setrecursionlimit(10**7)

N = int(input())
P = list(map(int, input().split()))

Q = [-1] * N
for i in range(N):
    Q[P[i] - 1] = i

S = ''
a = 1
l_stack = []
r_stack = []
state_stack = []
# Stack simule la récursion : state = 0 (descend), 1 (remonte)
l_stack.append(0)
r_stack.append(N)
state_stack.append(0)
while l_stack:
    l = l_stack[-1]
    r = r_stack[-1]
    state = state_stack[-1]
    if state == 0:
        # début du "rec"
        if l == r:
            l_stack.pop()
            r_stack.pop()
            state_stack.pop()
            continue
        while l < r:
            ai = Q[a - 1]
            if ai >= r:
                print(':(')
                exit()
            a += 1
            S += '('
            # préparer retour de la récursion (revenir après "rec(l, ai)")
            l_stack[-1] = ai + 1
            r_stack[-1] = r
            state_stack[-1] = 1
            l_stack.append(l)
            r_stack.append(ai)
            state_stack.append(0)
            break
        else:
            l_stack.pop()
            r_stack.pop()
            state_stack.pop()
    else:
        S += ')'
        l_stack.pop()
        r_stack.pop()
        state_stack.pop()

print(S)