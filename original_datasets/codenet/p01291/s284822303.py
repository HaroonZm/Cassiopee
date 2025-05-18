def solve():
    from itertools import combinations
    from heapq import heappush, heappop
    
    def dot(c1, c2):
        return c1.real * c2.real + c1.imag * c2.imag
    
    def cross(c1, c2):
        return c1.real * c2.imag - c1.imag * c2.real
    
    # get distance between segment and point
    def d_sp(sp1, sp2, p):
        a = sp2 - sp1
        b = p - sp1
        if dot(a, b) < 0:
            return abs(b)
        c = sp1 - sp2
        d = p - sp2
        if dot(c, d) < 0:
            return abs(d)
        return abs(cross(a, b) / a)
    
    # get distance between two segments
    def d_s(p1, p2, p3, p4):
        return min(d_sp(p1, p2, p3), d_sp(p1, p2, p4), d_sp(p3, p4, p1), \
                   d_sp(p3, p4, p2))

    from sys import stdin
    
    file_input = stdin
    
    while True:
        W, N = map(int, file_input.readline().split())
        
        if W == 0:
            break
        if N == 0:
            print(W)
            continue
        
        polygons = []
        adj = [[] for i in range(N + 1)]
        adj_s = adj[0]
        goal = N + 1
        
        for i in range(1, N + 1):
            M = int(file_input.readline())
            p = [i]
            s_d = W
            g_d = W
            for j in range(M):
                x, y = map(int, file_input.readline().split())
                p.append(x + y * 1j)
                s_d = min(s_d, x)
                g_d = min(g_d, W - x)
            adj_s.append((i, s_d))
            adj[i].append((goal, g_d))
            p.append(p[1])
            polygons.append(p)
        
        for p1, p2 in combinations(polygons, 2):
            i = p1[0]
            j = p2[0]
            d = [d_s(v1, v2, v3, v4) for v3, v4 in zip(p2[1:], p2[2:]) \
                 for v1, v2 in zip(p1[1:], p1[2:])]
            
            d = min(d)
            adj[i].append((j, d))
            adj[j].append((i, d))
        
        # Dijkstra's algorithm
        PQ = [(0, 0)]
        isVisited = [False] * (N + 2)
        distance = [W] * (N + 2)
        
        distance[0] = 0
        
        while PQ:
            u_cost, u = heappop(PQ)
            
            if u == goal:
                print(u_cost)
                break
            
            if u_cost > distance[u]:
                continue
            
            isVisited[u] = True
            
            for v, v_cost in adj[u]:
                if isVisited[v]:
                    continue
                
                t_cost = distance[u] + v_cost
                if t_cost < distance[v]:
                    distance[v] = t_cost
                    heappush(PQ, (t_cost, v))

solve()