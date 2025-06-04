import sys
from collections import deque

def can_assign(g, l, h, n, edges):
    # Build flow network
    # Nodes: 
    # 0: source
    # 1..m: edge nodes
    # m+1..m+n: student nodes
    # m+n+1: sink
    m = len(edges)
    s = 0
    t = m + n +1
    size = t +1
    capacity = [[0]*size for _ in range(size)]
    
    # source to each edge node: capacity 1
    for i in range(m):
        capacity[s][i+1] = 1
    # Each edge node to its two student nodes: capacity 1
    for i,(u,v) in enumerate(edges):
        capacity[i+1][m+u] = 1
        capacity[i+1][m+v] = 1
    # student nodes to sink: capacity h
    for i in range(1,n+1):
        capacity[m+i][t] = h
    
    # We must guarantee each student has at least l gifts
    # To do that, check if it's possible to have at least l incoming
    # This is equivalent to demands or lower bound on the edges.
    # Use standard reduction: demands on sink arcs to guarantee at least l inflow
    # Instead of that, check after max flow if each student receives >= l:
    # To guarantee min l gifts, check max flow after "demand" removal:
    # Instead, to test feasiblity, try to see if there's a flow of m (all edges assigned)
    # with per student capacity h and count the incoming flow per student,
    # if any student receives < l, fail.
    
    flow = 0
    parent = [-1]*size
    
    def bfs():
        nonlocal parent
        parent = [-1]*size
        queue = deque()
        queue.append(s)
        parent[s] = s
        while queue:
            u = queue.popleft()
            for v in range(size):
                if capacity[u][v]>0 and parent[v]==-1:
                    parent[v] = u
                    if v == t:
                        return True
                    queue.append(v)
        return False
    
    while bfs():
        path_flow = 10**9
        v = t
        while v!=s:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u
        v = t
        while v!=s:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u
        flow += path_flow
    if flow < m:
        return False,0,0
    # count gifts received by each student from flow graph
    in_deg = [0]*(n+1)
    for i in range(m):
        # edge node i+1
        # find which student got the gift:
        for v in (m + edges[i][0], m + edges[i][1]):
            # if capacity[v][i+1] > 0 => flow from i+1 to v is 1 (edge directed to v-n)
            if capacity[v][i+1]>0:
                in_deg[v - m] +=1
    min_g = min(in_deg[1:])
    max_g = max(in_deg[1:])
    if min_g < l:
        return False,0,0
    return True, min_g, max_g

input = sys.stdin.readline
while True:
    line = input()
    if not line:
        break
    n,m = map(int,line.split())
    if n==0 and m==0:
        break
    edges = [tuple(map(int,input().split())) for _ in range(m)]
    # binary search on difference d = h-l smallest
    # l can be from 0 to m//n (at most)
    # h = l + d
    ans_l, ans_h = 0, m
    # We want:
    # minimize (h-l)
    # among minimal, maximize l
    left_d = 0
    right_d = m
    res_l, res_h = 0, m
    while left_d <= right_d:
        d = (left_d + right_d)//2
        feasible = False
        tmp_l, tmp_h = -1,-1
        # for fixed d, try to find l maximal
        # l between 0 and m
        l_left = 0
        l_right = m
        while l_left <= l_right:
            l_mid = (l_left + l_right)//2
            h_mid = l_mid + d
            if h_mid > m:
                l_right = l_mid -1
                continue
            ok,min_g,max_g = can_assign(d,l_mid,h_mid,n,edges)
            if ok:
                feasible = True
                tmp_l, tmp_h = min_g,max_g
                l_left = l_mid +1
            else:
                l_right = l_mid -1
        if feasible:
            right_d = d -1
            res_l, res_h = tmp_l, tmp_h
        else:
            left_d = d +1
    print(res_l,res_h)