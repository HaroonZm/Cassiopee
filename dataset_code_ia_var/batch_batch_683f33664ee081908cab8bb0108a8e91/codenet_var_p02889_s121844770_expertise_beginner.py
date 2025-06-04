import numpy as np
from scipy.sparse import csgraph, csr_matrix

def main():
    # Lire l'entrée standard et convertir en liste d'entiers
    t = list(map(np.int32, open(0).read().split()))

    # Extraire n, m, l
    n = t[0]
    m = t[1]
    l = t[2]
    data = t[3:]
    
    # Préparer les listes pour les arêtes
    weights = []
    rows = []
    cols = []
    
    # Lire les arêtes du graphe
    for i in range(m):
        from_node = data[i*3]
        to_node = data[i*3+1]
        weight = data[i*3+2]
        rows.append(from_node)
        cols.append(to_node)
        weights.append(weight)
    
    # Créer la matrice creuse du graphe
    graph = csr_matrix((weights, (rows, cols)), shape=(n+1, n+1))
    
    # Calculer les plus courts chemins pour tous les couples
    dist = csgraph.floyd_warshall(graph, directed=True)
    
    # On vérifie si la distance est <= l
    D = (dist <= l)
    
    # Récupérer les requêtes et afficher les résultats
    res = []
    num_queries = (len(data) - 3*m) // 2
    query_index = 3*m
    for i in range(num_queries):
        u = data[query_index + i*2]
        v = data[query_index + i*2 + 1]
        value = int(D[u][v])
        # Un traitement équivalent à celui avec %n -1 dans l'original
        value = (value % n) - 1
        res.append(str(value))
    
    print('\n'.join(res))

main()