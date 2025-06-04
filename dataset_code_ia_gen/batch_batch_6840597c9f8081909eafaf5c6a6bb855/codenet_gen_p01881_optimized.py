from collections import deque
import sys
input=sys.stdin.readline
H,W=map(int,input().split())
grid=[list(input().rstrip()) for _ in range(H)]
dcs=[(-1,0),(1,0),(0,-1),(0,1)]

# Initialize
princess=None
soldiers=[]
exit_pos=None

for i in range(H):
    for j in range(W):
        c=grid[i][j]
        if c=='@':
            princess=(i,j)
            grid[i][j]='.'
        elif c=='$':
            soldiers.append((i,j))
            grid[i][j]='.'
        elif c=='%':
            exit_pos=(i,j)
            grid[i][j]='.'

INF=10**9
soldier_dist=[[INF]*W for _ in range(H)]
q=deque()
for r,c in soldiers:
    soldier_dist[r][c]=0
    q.append((r,c))
while q:
    r,c=q.popleft()
    for dr,dc in dcs:
        nr,nc=r+dr,c+dc
        if 0<=nr<H and 0<=nc<W and grid[nr][nc]=='.' and soldier_dist[nr][nc]>soldier_dist[r][c]+1:
            soldier_dist[nr][nc]=soldier_dist[r][c]+1
            q.append((nr,nc))

princess_dist=[[INF]*W for _ in range(H)]
pr,q=princess
princess_dist[pr][q]=0
q=deque()
q.append((pr,q))
while q:
    r,c=q.popleft()
    if (r,c)==exit_pos:
        # Check timing constraint: princess must arrive strictly before any soldier
        if princess_dist[r][c]<soldier_dist[r][c]:
            print("Yes")
            break
    for dr,dc in dcs+[(0,0)]:
        nr,nc=r+dr,c+dc
        nd=princess_dist[r][c]+1
        if 0<=nr<H and 0<=nc<W and grid[nr][nc]=='.' and princess_dist[nr][nc]>nd:
            # princess cell must be reachable earlier than soldier or no soldier at all
            if nd < soldier_dist[nr][nc]:
                princess_dist[nr][nc]=nd
                q.append((nr,nc))
else:
    print("No")