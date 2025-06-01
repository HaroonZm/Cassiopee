import sys
sys.setrecursionlimit(10**7)

def is_path_graph(n, edges):
    # Si aucun arête, un seul point ou juste des points isolés => oui
    if n == 0:
        return True

    deg = [0]*(n+1)
    for u,v in edges:
        deg[u] +=1
        deg[v] +=1

    # Pour être un chemin simple :
    # - pas de sommet avec degré > 2
    # - exactement 0 ou 2 sommets avec degré 1
    # - tous les autres sommets ont degré 2 ou 0 (isolés)
    deg1 = sum(1 for d in deg if d==1)
    deg2 = sum(1 for d in deg if d==2)

    if deg1 != 0 and deg1 != 2:
        return False
    if any(d > 2 for d in deg):
        return False

    # Vérifions que l'on a une composante connexe composée de tous les sommets non isolés
    # (car les sommets isolés n'empêchent pas d'être sur une ligne)
    adj = [[] for _ in range(n+1)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False]*(n+1)

    # Trouvons un sommet de départ avec degré >=1
    start = 0
    for i in range(1,n+1):
        if deg[i]>=1:
            start = i
            break
    else:
        # Pas d'arêtes, donc tous isolés => oui
        return True

    stack = [start]
    count = 0
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        count +=1
        for w in adj[node]:
            if not visited[w]:
                stack.append(w)

    # Nombre de sommets avec degré >=1
    deg_plus = sum(1 for d in deg if d >=1)
    # On doit avoir une seule composante connexe pour cette partie
    return count == deg_plus


input = sys.stdin.readline

while True:
    line = input()
    if not line:
        break
    n,m = map(int,line.split())
    if n==0 and m==0:
        break
    edges = []
    for _ in range(m):
        u,v = map(int,input().split())
        edges.append((u,v))
    print("yes" if is_path_graph(n, edges) else "no")