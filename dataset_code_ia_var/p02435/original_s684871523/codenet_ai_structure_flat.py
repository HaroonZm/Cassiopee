from collections import deque

n, queries = map(int, input().split())

stack_dict = []
i = 0
while i < n:
    stack_dict.append(deque())
    i += 1

i = 0
while i < queries:
    parts = input().split()
    q = int(parts[0])
    t = int(parts[1])
    if q == 0:
        stack_dict[t].append(int(parts[2]))
    elif q == 1:
        if stack_dict[t]:
            print(stack_dict[t][-1])
    elif q == 2:
        if stack_dict[t]:
            stack_dict[t].pop()
    i += 1