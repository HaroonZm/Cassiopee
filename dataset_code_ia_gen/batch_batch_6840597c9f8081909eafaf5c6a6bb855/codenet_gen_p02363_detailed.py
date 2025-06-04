# Programme Python complet pour le problème All Pairs Shortest Path avec détection de cycle négatif
import sys

def main():
    input = sys.stdin.readline
    V, E = map(int, input().split())  # Nombre de sommets et d'arêtes
    
    INF = 10**15  # Une constante grande pour représenter l'infini
    
    # Initialisation de la matrice des distances
    # D[i][j] représente la distance minimale de i à j.
    D = [[INF] * V for _ in range(V)]
    for i in range(V):
        D[i][i] = 0  # Distance de chaque sommet à lui-même est 0
    
    # Lecture des arêtes et mise à jour des distances initiales
    for _ in range(E):
        s, t, d = map(int, input().split())
        D[s][t] = d
    
    # Algorithme de Floyd-Warshall
    # On essaie d'améliorer les distances en passant par un sommet intermédiaire k
    for k in range(V):
        for i in range(V):
            # Une optimisation possible : passer à la ième ligne uniquement si D[i][k] != INF
            if D[i][k] == INF:
                continue
            for j in range(V):
                if D[k][j] == INF:
                    continue
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
    
    # Vérification de cycle négatif : si D[i][i] < 0 pour un i quelconque,
    # alors il existe un cycle de poids négatif accessible depuis i.
    for i in range(V):
        if D[i][i] < 0:
            print("NEGATIVE CYCLE")
            return
    
    # Sinon, affichage des distances, remplacer INF par "INF"
    for i in range(V):
        line = []
        for j in range(V):
            if D[i][j] == INF:
                line.append("INF")
            else:
                line.append(str(D[i][j]))
        print(" ".join(line))

if __name__ == "__main__":
    main()