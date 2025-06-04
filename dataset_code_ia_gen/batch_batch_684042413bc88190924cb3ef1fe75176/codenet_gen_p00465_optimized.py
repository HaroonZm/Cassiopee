import sys
from collections import deque
input=sys.stdin.readline

def bfs(W,H,X,Y,levels,auth):
    if auth==0:
        return 0
    visited=[[False]*W for _ in range(H)]
    q=deque()
    x,y=X-1,Y-1
    if levels[y][x]>auth:
        return 0
    visited[y][x]=True
    q.append((x,y))
    count=1
    while q:
        cx,cy=q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny=cx+dx,cy+dy
            if 0<=nx<W and 0<=ny<H and not visited[ny][nx] and levels[ny][nx]<=auth:
                visited[ny][nx]=True
                count+=1
                q.append((nx,ny))
    return count

def possible(W1,H1,X1,Y1,levels1,W2,H2,X2,Y2,levels2,R,s):
    res=0
    la1=[l for l in s[0]]
    la2=[l for l in s[1]]
    # auth level range from minimal 0 to max 10^8 or max needed
    # We'll binary search auth separately for each office
    # But we want minimal sum of auth1+auth2 so we binary search sum and greedily choose auth levels

    # We can try all auth1 from 0 to maxA1 max levels in office1, and check if auth2 satisfies rooms>=R
    # To optimize, precompute sorted unique levels for each office
    # Then do two pointers approach

def main():
    while True:
        R=int(input())
        if R==0:
            break
        W1,H1,X1,Y1=map(int,input().split())
        levels1=[list(map(int,input().split())) for _ in range(H1)]
        W2,H2,X2,Y2=map(int,input().split())
        levels2=[list(map(int,input().split())) for _ in range(H2)]

        # get unique levels + 0
        levs1 = set()
        for row in levels1:
            levs1.update(row)
        levs1.add(0)
        levs1=list(levs1)
        levs1.sort()

        levs2 = set()
        for row in levels2:
            levs2.update(row)
        levs2.add(0)
        levs2=list(levs2)
        levs2.sort()

        # precompute number of rooms reachable for each auth level in each office
        # BFS for each distinct auth level? For large input, too costly
        # Optimization: Because levels are integers and auth level is cutoff, BFS reachable rooms are monotonic increasing with auth

        # We'll do BFS only for distinct auth levels in sorted order, using binary search on levels

        def precompute(W,H,X,Y,levels,levs):
            res = []
            prev = 0
            for auth in levs:
                if auth==0:
                    res.append(0)
                else:
                    c=bfs(W,H,X,Y,levels,auth)
                    res.append(c)
                    if c==prev:
                        # if no improvement, could skip but keep for index
                        pass
                    prev=c
            return res

        arr1=precompute(W1,H1,X1,Y1,levels1,levs1)
        arr2=precompute(W2,H2,X2,Y2,levels2,levs2)

        # Now we want minimal sum of auth1+auth2 with arr1[i]+arr2[j]>=R
        # Use two pointers on levs1, levs2 to find minimal sum

        i,j=0,len(levs2)-1
        ans=10**15
        while i<len(levs1) and j>=0:
            c=arr1[i]+arr2[j]
            if c>=R:
                v=levs1[i]+levs2[j]
                if v<ans:
                    ans=v
                j-=1
            else:
                i+=1
        print(ans)

if __name__=="__main__":
    main()