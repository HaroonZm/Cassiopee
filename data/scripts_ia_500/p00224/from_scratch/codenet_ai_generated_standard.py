import sys
import heapq

def solve():
    input = sys.stdin.readline
    while True:
        m,n,k,d = map(int,input().split())
        if m==0 and n==0 and k==0 and d==0:
            break
        cake = list(map(int,input().split()))
        nodes = {'H':0,'D':1}
        idx = 2
        for i in range(m):
            nodes['C'+str(i+1)] = idx
            idx+=1
        for i in range(n):
            nodes['L'+str(i+1)] = idx
            idx+=1
        graph = [[] for _ in range(idx)]
        for _ in range(d):
            s,t,e = input().split()
            e = int(e)
            u,v = nodes[s],nodes[t]
            graph[u].append((v,e))
            graph[v].append((u,e))
        INF = 10**9
        max_mask = 1<<m
        dist = [[INF]*max_mask for _ in range(idx)]
        dist[0][0] = 0
        hq = [(0,0,0)]
        while hq:
            cost,u,mask = heapq.heappop(hq)
            if dist[u][mask]<cost:
                continue
            if u==1:
                print(cost)
                break
            for v,e in graph[u]:
                nmask = mask
                cals = k*e
                if 2<=v<2+m:
                    bit = v-2
                    if (mask & (1<<bit))==0:
                        nmask |= 1<<bit
                        cals -= cake[bit]
                ncost = cost + cals
                if dist[v][nmask]>ncost:
                    dist[v][nmask]=ncost
                    heapq.heappush(hq,(ncost,v,nmask))

if __name__=="__main__":
    solve()