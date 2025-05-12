from collections import deque

n, queries = map(int, input().split())

stack_dict = []
for i in range(n):
    stack_dict.append(deque())

for i in range(queries):
    q, t, *x = map(int, input().split())
    if q == 0:
        stack_dict[t].append(x[0])
    elif q == 1:
        if stack_dict[t]:
            print(stack_dict[t][-1])
    elif q == 2:
        if stack_dict[t]:
            stack_dict[t].pop()