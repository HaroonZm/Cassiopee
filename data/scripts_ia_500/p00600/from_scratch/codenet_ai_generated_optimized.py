import sys
import heapq

def main():
    input = sys.stdin.readline
    while True:
        s,d = map(int,input().split())
        if s==0 and d==0:
            break
        n = s+d
        edges = [[] for _ in range(n)]

        # Read hot spring to district distances
        for i in range(s):
            dist_list = list(map(int,input().split()))
            for j,dist in enumerate(dist_list):
                if dist !=0:
                    # edges between node i and s+j
                    edges[i].append((dist,s+j))
                    edges[s+j].append((dist,i))
        # Read district to district distances
        for i in range(d-1):
            dist_list = list(map(int,input().split()))
            for j,dist in enumerate(dist_list):
                if dist !=0:
                    u = s + j
                    v = s + i + 1 + j
                    edges[u].append((dist,v))
                    edges[v].append((dist,u))

        # Prim's algorithm for MST
        used = [False]*n
        hq = []
        used[0] = True
        for dist,to in edges[0]:
            heapq.heappush(hq,(dist,to))
        res = 0
        cnt = 1
        while hq and cnt < n:
            dist,u = heapq.heappop(hq)
            if used[u]:
                continue
            used[u] = True
            res += dist
            cnt += 1
            for w,to in edges[u]:
                if not used[to]:
                    heapq.heappush(hq,(w,to))
        print(res)

if __name__=="__main__":
    main()