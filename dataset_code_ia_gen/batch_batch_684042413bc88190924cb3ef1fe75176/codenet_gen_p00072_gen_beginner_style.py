def main():
    while True:
        n = int(input())
        if n == 0:
            break
        m = int(input())
        edges = []
        for _ in range(m):
            line = input()
            a, b, d = line.split(',')
            a = int(a)
            b = int(b)
            d = int(d)
            edges.append((a, b, d))
        # on va créer un graphe sous forme de liste d'adjacence
        graph = [[] for _ in range(n)]
        for a, b, d in edges:
            graph[a].append((b, d))
            graph[b].append((a, d))

        # On veut un sous-ensemble d'arêtes connectant tous les sommets avec la somme minimale de longueurs
        # On peut utiliser un algorithme de Kruskal ou Prim pour trouver un arbre couvrant minimal (MST)
        # Puis le nombre de lanternes est la somme sur chaque arête de (distance / 100) lanternes
        # On vérifie que chaque distance est multiple de 100

        # Kruskal
        parent = [i for i in range(n)]

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pb] = pa
                return True
            return False

        edges_sorted = sorted(edges, key=lambda x: x[2])
        total_lanterns = 0
        for a, b, d in edges_sorted:
            if union(a, b):
                total_lanterns += d // 100  # lanternes à 100m d'intervalle sur cette route
        print(total_lanterns)

main()