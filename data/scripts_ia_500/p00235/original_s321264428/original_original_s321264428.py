def tree_walk_1(start, parent=None):
    for i, t in adj[start]:
        if i != parent:
            P[i] = (start, t)
            C[start].append((i, t))
            tree_walk_1(i, start)

def tree_walk_2(start):
    global time
    notVisited[start] = False
    for c, t1 in C[start]:
        if notVisited[c]:
            time += 2 * t1
            tree_walk_2(c)
    p, t2 = P[start]
    if notVisited[p]:
        time += t2
        tree_walk_2(p)

from sys import stdin
f_i = stdin

while True:
    N = int(f_i.readline())
    if N == 0:
        break
    
    adj = [[] for i in range(N)]
    for i in range(N - 1):
        a, b, t = map(int, f_i.readline().split())
        a -= 1
        b -= 1
        adj[a].append((b, t))
        adj[b].append((a, t))
    
    # leaf cutting
    lf = []
    for i, a in enumerate(adj[1:], start=1):
        if len(a) == 1:
            lf.append(i)
    for l in lf:
        i, t = adj[l].pop()
        adj[i].remove((l, t))
    
    # root candidate
    rc = [i for i, a in enumerate(adj[1:], start=1) if len(a) == 1]
    if not rc:
        print(0)
        continue
    
    time_rec = []
    for r in rc:
        P = [None] * N
        P[r] = (r, 0)
        C = [[] for i in range(N)]
        tree_walk_1(r) #making a tree
        
        time = 0
        notVisited = [True] * N
        tree_walk_2(0)
        time_rec.append(time)
    
    print(min(time_rec))