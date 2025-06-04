w,d,n = map(int,input().split())
meas = [[None]*d for _ in range(w)]
for _ in range(n):
    x,y,z = map(int,input().split())
    meas[x-1][y-1]=z

from math import inf

# Initialize bounds: for each cell [low, high]
low = [[-inf]*d for _ in range(w)]
high = [[inf]*d for _ in range(w)]
for i in range(w):
    for j in range(d):
        if meas[i][j] is not None:
            low[i][j] = high[i][j] = meas[i][j]

changed = True
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

while changed:
    changed = False
    for i in range(w):
        for j in range(d):
            for dx,dy in dirs:
                ni,nj = i+dx,j+dy
                if 0<=ni<w and 0<=nj<d:
                    # low[i][j] >= low[ni][nj]-1
                    if low[i][j]<low[ni][nj]-1:
                        low[i][j] = low[ni][nj]-1
                        changed = True
                    # high[i][j] <= high[ni][nj]+1
                    if high[i][j]>high[ni][nj]+1:
                        high[i][j] = high[ni][nj]+1
                        changed = True
            if low[i][j]>high[i][j]:
                print("No")
                exit()

total = 0
for i in range(w):
    for j in range(d):
        # pick minimal possible altitude to minimize total
        val = low[i][j]
        if val== -inf:
            val = -10**9  # Large negative to simulate minimal?
        total += val
print(total)