from collections import deque

q = deque()
for i in range(int(input())):
    req = list(map(int, input().split()))
    if req[0] == 0:
        if req[1] == 0:
            q.appendleft(req[2])
        else:
            q.append(req[2])
    elif req[0] == 1:
        print(q[req[1]], end='\n')
    else:
        if req[1] == 0:
            q.popleft()
        else:
            q.pop()