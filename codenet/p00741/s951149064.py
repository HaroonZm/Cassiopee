import sys
sys.setrecursionlimit(10**7) 

dx = [1,0,-1,0,1,-1,1,-1]
dy = [0,1,0,-1,1,1,-1,-1]

def dfs(C,h,w):
    global seen
    seen[h][w] = True
    for dir in range(8):
        nh = h + dx[dir]
        nw = w + dy[dir]
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            continue
        if C[nh][nw] == 0:
            continue
        if seen[nh][nw]:
            continue

        dfs(C,nh,nw)
    
while True:
    W,H = map(int, input().split())
    if W==0 and H==0:
        break
    C = []
    for i in range(H):
        array = list(map(int, input().split()))
        C.append(array)
    
    count = 0
    seen = [[False]*W for _ in range(H)]
    for dh in range(H):
        for dw in range(W):
            if C[dh][dw] != 0 and seen[dh][dw] == False:
                dfs(C,dh,dw)
                count += 1
    
    print(count)