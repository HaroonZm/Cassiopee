from collections import deque

n = int(input())
lst = deque(map(int, input().split()))
count = [0]
flip = [False]

def up(idx, val):
    if not flip[0]:
        if val == idx + 1:
            count[0] += 1
            flip[0] = True
    else:
        flip[0] = False

dummy = [up(i, lst.popleft()) for i in range(n)]

print(count[0])