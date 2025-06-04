"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0092

Ce programme lit une carte composée de caractères '.' et '#' et détecte la taille du plus grand carré possible composé uniquement de '.'.
"""

import sys

def find_square(data):
    """
    Trouve la taille du plus grand carré composé uniquement de '.' dans la grille donnée.
    
    Args:
        data (List[str]): Liste de chaînes représentant chaque ligne de la grille.
    
    Returns:
        int: Taille du côté du plus grand carré de '.' trouvé dans la grille.
    """
    max_size = 0  # Mémorise la taille maximale du carré trouvé
    lmap = []     # Carte convertie en 0 (pour '#') et 1 (pour '.')
    for row in data:
        temp = []
        for c in row:
            # Convertit chaque caractère en 1 (si point) ou 0 (si dièse)
            if c == '.':
                temp.append(1)
            else:
                temp.append(0)
        lmap.append(temp)

    prev_row = lmap[0]  # Ligne précédente dans la dynamique
    for curr_row in lmap[1:]:  # Parcourt toutes les lignes sauf la première
        for x in range(1, len(lmap[0])):  # Parcourt chaque colonne à partir de la deuxième colonne
            if curr_row[x] == 1:
                # Prend le minimum des cases en haut, à gauche et en haut à gauche puis ajoute 1
                if prev_row[x-1] != 0 and prev_row[x] != 0 and curr_row[x-1] != 0:
                    curr_row[x] = min(prev_row[x-1], min(prev_row[x], curr_row[x-1])) + 1
                    # Met à jour la taille maximale si besoin
                    if curr_row[x] > max_size:
                        max_size = curr_row[x]
        prev_row = curr_row  # Passe à la ligne suivante comme future 'précédente'
    return max_size


def find_square2(data):
    """
    Variante de la fonction de recherche d'un carré,
    optimisée pour une écriture plus concise mais avec la même logique que find_square.
    
    Args:
        data (List[str]): Liste des chaînes représentant la grille.
    
    Returns:
        int: Taille du plus grand carré composé de '.'.
    """
    max_size = 0  # Mémorise la taille maximale du carré trouvé
    lmap = []
    for row in data:
        temp = []
        for c in row:
            # 1 pour '.', 0 pour '#'
            if c == '.':
                temp.append(1)
            else:
                temp.append(0)
        lmap.append(temp)

    prev_row = lmap[0]
    # Parcourt toutes les lignes sauf la première
    for curr_row in lmap[1:]:
        # Parcourt à partir de la deuxième colonne
        for x, t in enumerate(curr_row[1:], start=1):
            if t == 1:
                # Règle dynamique : minimum autour + 1
                curr_row[x] = min(prev_row[x-1], min(prev_row[x], curr_row[x-1])) + 1
                # Mise à jour taille maximale
                if curr_row[x] > max_size:
                    max_size = curr_row[x]
        prev_row = curr_row
    return max_size


def main(args):
    """
    Fonction principale qui gère l'entrée et la sortie.
    Lit successivement des cartes et affiche la taille du plus grand carré pour chacune.
    
    Args:
        args (List[str]): Arguments de la ligne de commande (non utilisés ici, mais présents pour la compatibilité).
    
    Effet de bord:
        Affiche le résultat pour chaque carte entrée.
    """
    while True:
        n = int(input())  # Lit le nombre de lignes pour cette carte
        if n == 0:
            # Arrête le traitement si n==0
            break
        # Lit chaque ligne de la carte
        data = [input() for _ in range(n)]
        # Calcule le plus grand carré possible et affiche le résultat
        result = find_square2(data)
        print(result)


if __name__ == '__main__':
    main(sys.argv[1:])