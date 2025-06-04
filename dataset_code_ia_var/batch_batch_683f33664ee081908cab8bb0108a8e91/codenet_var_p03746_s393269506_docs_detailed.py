import sys

# Augmente la limite de récursion pour supporter des graphes plus larges
sys.setrecursionlimit(100005)

# Lecture du nombre de sommets N et d'arêtes M depuis l'entrée standard
N, M = map(int, input().split())

# Construction de la liste d'adjacence pour représenter le graphe non orienté
E = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    # On décrémente de 1 pour passer d'un index 1-based (dans l'entrée) à 0-based (Python)
    A -= 1
    B -= 1
    E[A].append(B)
    E[B].append(A)

# Table des sommets visités pour éviter les cycles ou doubles visites
visited = [False for _ in range(N)]

# Liste pour enregistrer l'ordre des visites de sommets (réponse finale)
ans = []

def dfs(p, one):
    """
    Parcours en profondeur (DFS) sur le graphe à partir du sommet p.

    Args:
        p (int): Index du sommet de départ (0-based).
        one (bool): Si True, ajoute le sommet à la liste 'ans' après l'appel récursif.
                    Si False, l'ajoute avant l'appel récursif.

    Returns:
        bool: True si le sommet p peut être atteint pour la première fois,
              False sinon (déjà visité).
    """
    # Si déjà visité, pas besoin de continuer sur ce sommet
    if visited[p]:
        return False

    # Marque le sommet courant comme visité
    visited[p] = True

    # Ajoute le sommet à la réponse avant la récursion si 'one' est False
    if not one:
        ans.append(p + 1)  # Conversion en 1-based pour l'affichage

    # Parcours récursivement tous les voisins du sommet courant
    for i in E[p]:
        if dfs(i, one):
            # On arrête dès que l'on parcourt un nouveau sommet (si le but est de trouver un chemin)
            break

    # Ajoute le sommet à la réponse après la récursion si 'one' est True
    if one:
        ans.append(p + 1)  # Conversion en 1-based

    # Retourne True pour indiquer que le sommet a bien été visité pour la première fois
    return True

# Début du parcours en profondeur à partir du sommet 0 (0-based), avec ajout après récursion (one=True)
dfs(0, True)

# Pour chaque voisin du sommet de départ, on lance DFS avec ajout avant récursion (one=False)
for i in E[0]:
    if dfs(i, False):
        # On arrête dès qu'un parcours réussi est trouvé
        break

# Affichage de la taille de la réponse (nombre d'étapes/visites)
print(len(ans))

# Affichage, un par ligne, de l'ordre des sommets visités (indices 1-based)
for i in ans:
    print(i)