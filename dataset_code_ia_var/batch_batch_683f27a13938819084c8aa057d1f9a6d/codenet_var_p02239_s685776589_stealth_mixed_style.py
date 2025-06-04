import queue

def parcours_largeur(graphe, distances):
    q = queue.Queue()
    q.put(0)
    distances[0] = 0
    while not q.empty():
        sommet = q.get()
        neighbors = list(reversed(range(len(graphe[sommet]))))
        [(
            distances.__setitem__(i, distances[sommet]+1),
            q.put(i)
        ) for i in neighbors if graphe[sommet][i] == 1 and distances[i] == -1]

def make_adj_matrix(nb):
    adj = []
    for _ in range(nb):
        vals = [int(x) for x in input().split()]
        s = [0]*nb
        j = 0
        while j < vals[1]:
            s[vals[2+j]-1] = 1
            j += 1
        adj += [s]
    return adj

N = int(input())
graph = make_adj_matrix(N)
dists = [-1]*N
parcours_largeur(graph, dists)
iii = 1
while iii <= N:
    print(iii, dists[iii-1])
    iii += 1