import queue

di = [0,1,0,-1]
dj = [1,0,-1,0]

h, w = map(int, input().split())
field = [input() for i in range(h)]
pdist = [[1000]*w for i in range(h)]
sdist = [[1000]*w for i in range(h)]

pque = queue.Queue()
sque = queue.Queue()
for i,row in enumerate(field):
    for j in range(w):
        if row[j] is '@':
            pque.put((i,j))
            pdist[i][j] = 0
            pi = i
            pj = j
        if row[j] is '$':
            sque.put((i,j))
            sdist[i][j] = 0
        if row[j] is '%':
            gi = i
            gj = j

while not sque.empty():
    i,j = sque.get()
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if ni >=0 and ni < h and nj >= 0 and nj < w:
            if (field[ni][nj] is not '#') and sdist[ni][nj] > sdist[i][j]+1:
                sdist[ni][nj] = sdist[i][j]+1
                sque.put((ni,nj))

while not pque.empty():
    i,j = pque.get()
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if ni >=0 and ni < h and nj >= 0 and nj < w:
            if (field[ni][nj] is not '#') and pdist[ni][nj] > pdist[i][j]+1 and pdist[i][j]+1 < sdist[ni][nj]:
                pdist[ni][nj] = pdist[i][j]+1
                pque.put((ni,nj))

if pdist[gi][gj] < 1000:
    print("Yes")
else:
    print("No")