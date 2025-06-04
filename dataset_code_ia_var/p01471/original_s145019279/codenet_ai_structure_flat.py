import heapq
N_W = input().split()
N = int(N_W[0])
W = int(N_W[1])
tmpw = 0
tmpv = 0
minheap = []
i = 0
while i < N:
    line = input().split()
    w = int(line[0])
    v = int(line[1])
    if w < 0:
        tmpw += w
        tmpv += v
        w = -w
        v = -v
    if v > 0:
        if w == 0:
            tmpv += v
        else:
            heapq.heappush(minheap, (-(v/w), w, v))
    i += 1
while W - tmpw > 1e-9 and minheap != []:
    p = heapq.heappop(minheap)
    w = p[1]
    v = p[2]
    x = min(1, (W-tmpw)/w)
    tmpw += x*w
    tmpv += x*v
print(tmpv)