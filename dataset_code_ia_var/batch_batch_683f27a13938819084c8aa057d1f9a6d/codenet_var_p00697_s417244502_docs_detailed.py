"""
Ce script résout un puzzle où neuf pièces aux bords colorés doivent être placées sur une grille 3x3 avec des contraintes d'adjacence de couleurs.
Le script utilise une recherche en profondeur (DFS) pour essayer toutes les combinaisons possibles et compter le nombre de dispositions valides.
"""

# Liste pour suivre les pièces déjà utilisées (True = disponible, False = placée)
p_ch = [True] * 9

# Définition des différentes rotations possibles d'une pièce (0 = top, 1 = right, 2 = bottom, 3 = left)
rot = (
    (0, 1, 2, 3),
    (1, 2, 3, 0),
    (2, 3, 0, 1),
    (3, 0, 1, 2)
)

# Tableau représentant les couleurs actuellement en bordure de chaque case, 13 emplacements pour toutes les arêtes
# adjacentes (c = couleur de contrôle, initialement)
adj = ['c'] * 13

# Tableau associant à chaque position de la grille les indices, dans adj, des arêtes droite et basse
# 12 signifie que l'arête n'a pas d'adjacence (hors grille)
rec_adj = [
    [0, 2],   # case 0: right = 0,  bottom = 2
    [1, 3],   # case 1: right = 1,  bottom = 3
    [12, 4],  # case 2: droite inexistante, bottom = 4
    [5, 7],   # case 3: right = 5,  bottom = 7
    [6, 8],   # case 4: right = 6,  bottom = 8
    [12, 9],  # case 5: pas de droite, bottom = 9
    [10, 12], # case 6: right = 10, pas de bottom
    [11, 12], # case 7: right = 11, pas de bottom
    [12, 12]  # case 8: pas de droite, pas de bottom
]

# Tableau associant à chaque position de la grille les indices, dans adj, des arêtes supérieure et gauche d'adjacence
# 12 signifie pas d'adjacence (en lisière)
ref_adj = [
    [12, 12], # case 0: pas d'adjacence
    [12, 0],  # case 1: pas de top, left = 0
    [12, 1],  # case 2: pas de top, left = 1
    [2, 12],  # case 3: top = 2, pas de left
    [3, 5],   # case 4: top = 3, left = 5
    [4, 6],   # case 5: top = 4, left = 6
    [7, 12],  # case 6: top = 7, pas de left
    [8, 10],  # case 7: top = 8, left = 10
    [9, 11]   # case 8: top = 9, left = 11
]

# Dictionnaire permettant de convertir les couleurs en leurs opposés (utilisé pour vérifier la compatibilité)
tr = dict(zip("RGBWrgbw", "rgbwRGBW"))

def dfs(i=0, a=[]):
    """
    Fonction récursive de recherche en profondeur pour essayer toutes les dispositions possibles des pièces.

    Args:
        i (int): L'indice de la case à remplir actuellement (de 0 à 8).
        a (list): Liste des pièces placées (inutile dans ce code, vestige d'une version précédente).

    Effets de bord:
        Met à jour la variable globale 'ans' à chaque solution complète trouvée.
        Modifie temporairement 'adj' et 'p_ch' lors du parcours récursif.
    """
    if i == 9:
        # Tous les emplacements sont remplis, donc une solution a été trouvée
        global ans
        ans += 1
    else:
        for j, p in enumerate(pieces):
            if p_ch[j]:  # Si la pièce n'a pas encore été utilisée
                ati, ali = ref_adj[i] # Indices des arêtes supérieure et gauche
                # On tente les 4 rotations de la pièce
                for t, r, b, l in rot:
                    # Vérification de la compatibilité sur le bord supérieur (top)
                    if ati == 12 or tr[p[t]] == adj[ati]:
                        # Vérification de la compatibilité sur le bord gauche (left)
                        if ali == 12 or tr[p[l]] == adj[ali]:
                            ari, abi = rec_adj[i] # Indices des arêtes droite et basse à remplir
                            adj[ari] = p[r]       # Mise à jour avec la couleur du bord droit
                            adj[abi] = p[b]       # Mise à jour avec la couleur du bord bas
                            p_ch[j] = False       # Marquer la pièce comme utilisée
                            dfs(i + 1)            # Passer à la case suivante
                            p_ch[j] = True        # Rétablir la pièce comme disponible
    # Les couleurs de adj seront réécrasées lors du backtracking

from sys import stdin
file_input = stdin

# Lire le nombre de cas à traiter (N)
N = int(file_input.readline())

for line in file_input:
    # Lecture des 9 pièces pour un cas
    pieces = line.split()
    # Réinitialisation de la variable réponse pour ce cas
    ans = 0
    # Lancer la recherche récursive
    dfs()
    # Afficher le nombre de configurations valides pour ce cas
    print(ans)