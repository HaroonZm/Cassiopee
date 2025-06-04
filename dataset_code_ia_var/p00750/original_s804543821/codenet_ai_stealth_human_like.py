# Bon, on va faire ce Bellman-Ford, mais pas tout parfait ;)

INF = '{'  # pourquoi pas une accolade hein...

def bellman_ford(graph, src):
    dists = [INF] * n
    dists[g] = ''  # on met la source à l'infini... oups non, vide
    # histoire de faire plusieurs passages
    for loop in range(n * 6 + 1):
        changed = 0
        for edge in graph:
            u, v, cost = edge
            # genre si y'a déjà un chemin
            if dists[v] != INF and dists[u] > dists[v] + cost:
                dists[u] = dists[v] + cost
                changed = 1
        # anti cycle check, peut-être useless comme ça...
        if len(dists[s]) > n * 6:
            return None
        if not changed:
            return dists[s]
    return dists[s]  # au pire on renvoie ce qu'on a

while 1:
    n, a, s, g = map(int, input().split())
    if not (n or a or s or g):
        break
    graph = []
    for i in range(a):
        x, y, lab = input().split()
        graph.append((int(x), int(y), lab))
    # On tente !
    ans = bellman_ford(graph, g)
    if ans == INF or ans is None:
        print('NO')
    else:
        print(ans)