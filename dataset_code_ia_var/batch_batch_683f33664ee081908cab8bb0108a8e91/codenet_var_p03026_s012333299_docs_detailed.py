from collections import deque

# Lecture du nombre de sommets du graphe
N = int(input())

# Initialisation de la liste d'adjacence : chaque sommet a une liste de voisins
to = [[] for _ in range(N)]

# Lecture des arêtes du graphe non orienté et remplissage de la liste d'adjacence
for _ in range(N - 1):
    # Les sommets sont saisis en base 1, on les convertit en base 0
    a, b = map(lambda x: int(x) - 1, input().split())
    to[a].append(b)
    to[b].append(a)

# Lecture de la liste des valeurs à assigner aux sommets
c = list(map(int, input().split()))
# Trie de la liste pour faciliter l'affectation des plus grandes valeurs en priorité
c.sort()

def main():
    """
    Propage les valeurs dans l'arbre en attribuant la plus grande valeur au sommet 0 
    puis, parcourant l'arbre avec une recherche en largeur (BFS), assigne les plus 
    grandes valeurs restantes aux autres sommets. Calcule et affiche la somme des 
    valeurs assignées à tous les sommets sauf le premier, puis affiche la liste complète
    des valeurs assignées à chaque sommet.
    """
    # ans[i] stocke la valeur assignée au sommet i
    ans = [0] * N
    # Attribution de la plus grande valeur au premier sommet
    ans[0] = c.pop()
    # S contiendra la somme des valeurs attribuées, sauf la première
    S = 0

    # Tableau des sommets déjà visités pour le parcours BFS
    seen = [0] * N
    seen[0] = 1  # On marque le sommet 0 comme visité
    # File pour le parcours BFS, initialisée avec le sommet 0
    que = deque([0])

    # Parcours BFS de l'arbre
    while que:
        v = que.popleft()  # On retire un sommet de la file
        for nv in to[v]:   # Parcours des voisins du sommet courant
            if not seen[nv]:  # Si le voisin n'a pas été visité
                seen[nv] = 1  # On le marque comme visité
                # On lui attribue la plus grande valeur restante
                ans[nv] = c.pop()
                # On ajoute cette valeur à la somme S
                S += ans[nv]
                # On ajoute ce voisin à la file pour continuer le parcours
                que.append(nv)

    # Affichage de la somme des valeurs attribuées (hors sommet 0)
    print(S)
    # Affichage de la répartition finale des valeurs sur les sommets
    print(*ans)

if __name__ == "__main__":
    main()