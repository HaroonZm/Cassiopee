n = int(raw_input("Entrer le nombre de sommets: "))
a = []
for i in range(n):
    # Lecture de la matrice, pas très élégant mais ça marche...
    values = raw_input().split()
    row = []
    for val in values:
        row.append(int(val))
    a.append(row)

def prim(graph):
    color = []
    for i in range(n):
        color.append('white')  # Encore des couleurs...

    d = [1000000000] * n
    p = [-1 for _ in range(n)]
    d[0] = 0

    while True:
        mincost = 1000000000
        u = -1
        for i in range(n):  # Recherche du prochain sommet à ajouter
            if color[i] != 'black' and d[i] < mincost:
                mincost = d[i]
                u = i
        if u == -1 or mincost == 1000000000:
            break  # On quitte la boucle si terminé

        color[u] = 'black'  # Marquer comme traité

        for v in range(n): # Parcourt tous les sommets pour la mise à jour
            if color[v] != 'black' and graph[u][v] != -1:
                if graph[u][v] < d[v]:
                    d[v] = graph[u][v]
                    p[v] = u
                    color[v] = 'gray' # Cette couleur sert pas à grand chose ici mais je la laisse...

    # Somme du coût de l'arbre couvrant
    print sum(d)

prim(a)