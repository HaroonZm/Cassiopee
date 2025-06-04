from collections import deque  # Importe la classe deque (double-ended queue) du module collections pour permettre une file efficace

# Lit un entier N à partir de l'entrée standard, qui correspond au nombre de sommets d'un graphe
N = int(input())

# Crée une liste de listes qui sera utilisée pour représenter les arêtes (connexions) du graphe non orienté.
# Chaque élément to[i] sera une liste contenant les sommets adjacents au sommet i.
to = [[] for _ in range(N)]  # Génère N listes vides mises dans une liste (adjacency list)

# Boucle pour lire chaque arête (N-1, car un arbre de N sommets a N-1 arêtes)
for _ in range(N - 1):
    # Lit une ligne, la découpe en deux parties, convertit chacun en entier en soustrayant 1
    # pour que les indices commencent à 0. map applique la fonction lambda sur chaque élément obtenu avec split().
    a, b = map(lambda x: int(x) - 1, input().split())
    # Ajoute b comme voisin de a et vice-versa
    to[a].append(b)
    to[b].append(a)

# Lit une liste d'entiers à partir de l'entrée standard.
# map applique int en conversion sur chaque élément de input().split()
c = list(map(int, input().split()))
# Trie la liste c dans l'ordre croissant; pop() retirera donc les plus grands d'abord
c.sort()

def main():
    # Crée une liste de N zéros, qui va contenir la valeur attribuée à chaque sommet
    ans = [0] * N

    # Attribue à la racine (sommet 0) la valeur la plus grande restante dans la liste c
    # c.pop() supprime et renvoie le dernier élément de la liste c (temps constant)
    ans[0] = c.pop()

    # Initialise S à 0, il va accumuler la somme des valeurs assignées aux sommets autres que la racine
    S = 0

    # Initialise une liste seen de taille N remplie de 0, pour marquer les sommets déjà visités (0 = pas vu, 1 = vu)
    seen = [0] * N
    seen[0] = 1  # Marque la racine (0) comme déjà visitée

    # Initialise une file FIFO (deque) contenant pour l'instant uniquement la racine (0)
    que = deque([0])

    # Boucle tant qu'il y a des éléments dans la file (sommet à explorer)
    while que:
        # Retire et récupère un élément du début de la file, c'est le sommet courant
        v = que.popleft()
        # Parcourt tous les voisins (adjacents) de v selon la liste d'adjacence
        for nv in to[v]:
            # Si le voisin n'a pas encore été visité
            if not seen[nv]:
                seen[nv] = 1  # Marque le voisin comme visité
                # Retire la plus grande valeur restante dans c et l'affecte à ce sommet
                ans[nv] = c.pop()
                # Ajoute la valeur de ans[nv] à la somme S (omettant la racine car on ne l'ajoute pas à S)
                S += ans[nv]
                # Ajoute ce voisin à la file pour explorer ses propres voisins ultérieurement
                que.append(nv)

    # Affiche la somme S sur une ligne
    print(S)
    # Affiche toutes les valeurs attribuées dans l'ordre des sommets en les séparant par des espaces
    # Le * décompose la liste ans en arguments séparés pour print
    print(*ans)

# Point d'entrée du programme : exécute la fonction main uniquement si ce fichier est exécuté comme programme principal
if __name__ == "__main__":
    main()