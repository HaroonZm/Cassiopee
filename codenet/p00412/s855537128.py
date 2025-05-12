from collections import deque
N,M = [int(x) for x in input().split(" ")]
qs = []
for i in range(N):
    qs.append(deque())
lens = [0]*N
for i in range(M):
    info,num = [int(x) for x in input().split(" ")]
    if info == 0:
        print(qs[num-1].popleft())
        lens[num-1] -= 1
    elif info == 1:
        index = 0
        for j in range(N):
            if lens[index] > lens[j]:
                index = j
        qs[index].append(num)
        lens[index] += 1