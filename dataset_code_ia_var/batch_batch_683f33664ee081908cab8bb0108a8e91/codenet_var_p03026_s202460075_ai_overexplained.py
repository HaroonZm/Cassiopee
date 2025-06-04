import sys  # Importation du module sys pour l'entrée standard
from collections import deque  # Importation de deque depuis collections, qui est une file doublement aboutie (FIFO/LIFO)

def solve():
    # Redéfinir 'input' pour lire les entrées ligne par ligne efficacement
    input = sys.stdin.readline
    
    # Lire un nombre entier 'N' qui représente le nombre de sommets/points dans un graphe/arbre
    N = int(input())
    
    # Créer une liste de listes pour représenter la structure des arêtes/connectivités
    # Chaque index de la liste 'Edge' représente un sommet, et sa valeur est la liste des sommets adjacents (voisins)
    Edge = [[] for _ in range(N)]
    
    # Boucle 'N-1' fois car pour un arbre avec N sommets il y a toujours N-1 arêtes
    for _ in range(N-1):
        # Lire deux entiers séparés symbolisant une arête entre deux sommets
        a, b = map(int, input().split())
        # Ajouter b-1 à la liste des voisins de a-1 (décrémenté de 1 car indexation commence à 0 en Python)
        Edge[a-1].append(b-1)
        # Ajouter a-1 à la liste des voisins de b-1, car le graphe est non orienté (arête bidirectionnelle)
        Edge[b-1].append(a-1)
    
    # Lire une liste d'entiers qui représentent des valeurs associées aux sommets (par exemple des couleurs, coûts, etc.)
    C = [int(c) for c in input().split()]
    
    # Trier la liste C en ordre décroissant (reverse=True) pour utiliser les plus grandes valeurs en premier
    C.sort(reverse=True)
    
    # Créer une liste 'Color' de longueur N où chaque élément sera initialisé à None (aucune valeur assignée)
    Color = [None] * N
    
    # Assigner la première valeur (la plus grande dans C) au sommet d'index 0 (la racine de l'arbre)
    Color[0] = C[0]
    
    # Initialiser une file (deque) pour effectuer un parcours BFS (parcours en largeur)
    q = deque()
    # Pour chaque voisin 'e' du sommet racine (sommet 0), ajouter un tuple (e, 0) à la file
    # 'e' est le sommet voisin, 0 est le sommet parent (ici la racine)
    for e in Edge[0]:
        q.append((e, 0))
    
    # Initialiser un accumulateur 'ans' à 0, pour stocker la somme des valeurs affectées exceptée la racine
    ans = 0
    
    # De 1 à N-1 (puisqu'on a déjà assigné la racine), on va parcourir tous les sommets restants
    for i in range(1, N):
        # Extraire le prochain élément dans la file (tuple): (nowN, preN)
        # 'nowN' est le sommet actuel auquel on va assigner une valeur
        # 'preN' est le sommet parent d'où on arrive à 'nowN'
        nowN, preN = q.popleft()
        
        # Ajouter la i-ième valeur de C à 'ans' (accumulateur), car c'est la valeur assignée à ce sommet
        ans += C[i]
        # Assigner C[i] (la prochaine plus grande valeur restante) au sommet current 'nowN'
        Color[nowN] = C[i]
        
        # Pour chaque voisin 'e' du sommet actuel 'nowN'
        for e in Edge[nowN]:
            # Vérifier que 'e' N'EST PAS le parent (pour éviter de revenir en arrière)
            if e != preN:
                # Ajouter le voisin 'e' (futur sommet à traiter) et 'nowN' (le parent) à la file
                q.append((e, nowN))
    
    # Afficher la somme totale des valeurs assignées aux sommets non racines (accumulateur 'ans')
    print(ans)
    # Afficher les valeurs attribuées à chaque sommet, sous forme de chaîne d'entiers séparés par espace
    print(" ".join(map(str, Color)))
    
    # Retourner 0 à la fin de la fonction pour signaler que tout s'est bien passé
    return 0

# Ce bloc vérifie si ce fichier est exécuté comme programme principal (et non importé)
if __name__ == "__main__":
    solve()  # Appeler la fonction principale pour lancer la résolution du problème