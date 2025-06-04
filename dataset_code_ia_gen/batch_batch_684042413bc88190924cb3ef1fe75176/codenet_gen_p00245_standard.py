import sys
from collections import deque
input=sys.stdin.readline

DIRS=[(0,1),(0,-1),(1,0),(-1,0)]

def bfs(startX,startY,mapc,X,Y):
    dist=[[-1]*Y for _ in range(X)]
    dist[startX][startY]=0
    q=deque()
    q.append((startX,startY))
    while q:
        x,y=q.popleft()
        for dx,dy in DIRS:
            nx,ny=x+dx,y+dy
            if 0<=nx<X and 0<=ny<Y and dist[nx][ny]==-1 and mapc[nx][ny]=='.':
                dist[nx][ny]=dist[x][y]+1
                q.append((nx,ny))
    return dist

def bfs_from_aisle_to_shelf(mapc,X,Y):
    # For each aisle cell, from it movement to adjacent shelf cell is cost 0
    # Because cannot enter shelf cell, must go adjacent aisle to pick product.
    # We need shortest distance from aisle to shelf by moving on aisles only,
    # but picking shelf adjacency counts as if at aisle cell adjacent to shelf.
    # So distances on aisles to aisle cells only.
    # Here shelves are walls for movement.
    pass

def main():
    while True:
        X,Y=map(int,input().split())
        if X==0 and Y==0:
            break
        mapc=[[] for _ in range(X)]
        shelves_pos={}
        start=(-1,-1)
        for y in range(Y):
            line=list(input().split())
            for x in range(X):
                c=line[x]
                mapc[x].append(c)
                if c=='P':
                    start=(x,y)
                elif c!='.' and c!='P':
                    shelves_pos[(x,y)]=int(c)
        n=int(input())
        sale_info=[{} for _ in range(10)]
        # storing [discount,s,e] per product number; only one per g per input assumed
        product_info_list=[]
        for _ in range(n):
            g,d,s,e=map(int,input().split())
            product_info_list.append((g,d,s,e))
        # map aisles and shelves
        # aisles: '.','P'; shelves: digits
        # movement allowed only on aisles except initial at P
        # need distances from each aisle cell to aisles adjacent shelf cells.
        # Calculate distance from aisles to aisles (BFS from P)
        dist_from_start=bfs(start[0],start[1],mapc,X,Y)
        # find for each shelf cell the aisles adjacent to it (neighbors)
        shelf_aisle_pos={}
        for (x,y),g in shelves_pos.items():
            aisles_adj=[]
            for dx,dy in DIRS:
                nx,ny=x+dx,y+dy
                if 0<=nx<X and 0<=ny<Y and mapc[nx][ny]=='.':
                    aisles_adj.append((nx,ny))
            shelf_aisle_pos[(x,y)]=aisles_adj
        # For each shelf cell, determine minimal dist from start to one of its adjacent aisles
        shelf_min_dist={}
        for (x,y) in shelves_pos.keys():
            min_d=10**9
            for ax,ay in shelf_aisle_pos[(x,y)]:
                if dist_from_start[ax][ay]>=0 and dist_from_start[ax][ay]<min_d:
                    min_d=dist_from_start[ax][ay]
            # impossible to access shelf if min_d remains large
            shelf_min_dist[(x,y)]=min_d
        # For each product number g, list its shelf positions
        prod_shelves=[[] for _ in range(10)]
        for (x,y),g in shelves_pos.items():
            prod_shelves[g].append((x,y))
        # For each product, need minimal distance to reach it from current position or other products picked
        # Since cannot step into shelf cells, movement cost calculation between products done between their aisle adjacents
        # Precompute shortest paths on aisles between shelves adjacency aisles:
        # prepare list of aisle positions relevant: starting position + all aisles adjacent shelf positions
        aisle_points=[]
        aisle_points.append(start)
        for g in range(10):
            for (x,y) in prod_shelves[g]:
                # multiple aisles adjacent to shelf; we store all
                for ax,ay in shelf_aisle_pos[(x,y)]:
                    aisle_points.append((ax,ay))
        # remove duplicates
        aisle_points=list(set(aisle_points))
        # Map point to idx
        point_idx={p:i for i,p in enumerate(aisle_points)}
        # Compute all pairs shortest distances on aisles using BFS per point
        adj=[[10**9]*len(aisle_points) for _ in range(len(aisle_points))]
        for i,(x,y) in enumerate(aisle_points):
            dist=[[-1]*Y for _ in range(X)]
            dist[x][y]=0
            q=deque()
            q.append((x,y))
            while q:
                cx,cy=q.popleft()
                for dx,dy in DIRS:
                    nx,ny=cx+dx,cy+dy
                    if 0<=nx<X and 0<=ny<Y:
                        if dist[nx][ny]==-1 and mapc[nx][ny]=='.':
                            dist[nx][ny]=dist[cx][cy]+1
                            q.append((nx,ny))
            for j,(tx,ty) in enumerate(aisle_points):
                if dist[tx][ty]>=0:
                    adj[i][j]=dist[tx][ty]
        # For each product g, determine minimal distance to pick from current position or another product position
        # Build a list of "nodes" for each product: minimal access cost from start or from other products
        # We'll represent picks by bits of length n (number of sales)
        # Each sale: product g[i], discount d[i], start s[i], end e[i]
        # For each sale, find minimal distance from start aisle or another shelf aisle adjacency with product picked, to each shelf adjacency of that product
        # We will pick one shelf position with minimal arrival time per product to maximize chance of buying within sale time.
        # Prepare a list for easier indexing:
        # For each sale i, store (g,d,s,e)
        # Build dist matrix between sales and start: dist_start[i] minimal distance from start point to product i shelf
        # dist_p2p[i][j]: minimal distance from product i shelf to product j shelf on aisles
        def dist_min_between_products(pi,pj):
            g_i,d_i,s_i,e_i=product_info_list[pi]
            g_j,d_j,s_j,e_j=product_info_list[pj]
            res=10**9
            for (x1,y1) in prod_shelves[g_i]:
                idx1s=[point_idx[p] for p in shelf_aisle_pos[(x1,y1)] if p in point_idx]
                for (x2,y2) in prod_shelves[g_j]:
                    idx2s=[point_idx[p] for p in shelf_aisle_pos[(x2,y2)] if p in point_idx]
                    for u in idx1s:
                        for v in idx2s:
                            d=adj[u][v]
                            if d<res:
                                res=d
            return res
        def dist_min_start_product(i):
            g_i,d_i,s_i,e_i=product_info_list[i]
            res=10**9
            stidx=point_idx[start]
            for (x,y) in prod_shelves[g_i]:
                idxs=[point_idx[p] for p in shelf_aisle_pos[(x,y)] if p in point_idx]
                for v in idxs:
                    d=adj[stidx][v]
                    if d<res:
                        res=d
            return res
        n=len(product_info_list)
        dist_start=[dist_min_start_product(i) for i in range(n)]
        dist_p2p=[[10**9]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j:
                    dist_p2p[i][j]=dist_min_between_products(i,j)
        # DP for bitmask picking products
        # state: dp[mask][last]: minimal time to have picked set mask with last picked product last
        # store time as minimum arrival time at product last product's shelf aisle adjacency (arbitrary adjacency with minimal arrival)
        # initial from start to product i at dist_start[i]
        # we must check feasibility of picking i: that arrival_time between s_i (sale start) and e_i(sale end)
        dp=[[10**9]*(n) for _ in range(1<<n)]
        for i in range(n):
            g,d,s,e=product_info_list[i]
            t=dist_start[i]
            if t>=s and t<=e and t!=10**9:
                dp[1<<i][i]=t
        for mask in range(1<<n):
            for last in range(n):
                if dp[mask][last]==10**9:
                    continue
                for nxt in range(n):
                    if (mask>>nxt)&1==0:
                        g,d,s,e=product_info_list[nxt]
                        cost=dist_p2p[last][nxt]
                        if cost==10**9:
                            continue
                        arrival_time=dp[mask][last]+cost
                        if arrival_time>=s and arrival_time<=e:
                            if arrival_time<dp[mask|(1<<nxt)][nxt]:
                                dp[mask|(1<<nxt)][nxt]=arrival_time
        ans=0
        for mask in range(1<<n):
            val=0
            for i in range(n):
                if (mask>>i)&1:
                    val+=product_info_list[i][1]
            for i in range(n):
                if dp[mask][i]!=10**9:
                    if val>ans:
                        ans=val
        print(ans)
main()