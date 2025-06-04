"""
AOJ 1059 Mysterious Onslaught

Ce script résout un problème de grille de taille NxN (N <= 5), où l'objectif est de recouvrir toutes les cases marquées avec un nombre minimal de rectangles alignés avec la grille. Le code utilise la programmation dynamique avec mémoïsation pour minimiser le nombre de coups (rectangles) nécessaires.

Fonctionnalités principales :
- Génération préalable de masques de rectangles possibles pour une grille 5x5.
- Encodage de la grille en entier pour permettre l’utilisation efficace comme clé de mémoïsation.
- Recherche du nombre minimal de coups pour vider la grille.

Auteur original : bal4u, 2018.7.7
Ce code inclut des commentaires détaillés et des docstrings complètes.

"""

# Initialisation des mémos pour mémoriser les sous-problèmes déjà résolus
# memo[b] mémorise le nombre minimal de coups pour vider le bitmask b (état de la grille)
memo = [-1] * (1 << 25)

# Pré-calcul de tous les rectangles possibles sur une grille 5x5
# arr[r1][c1][r2][c2] correspond au masque binaire du rectangle allant de (r1, c1) à (r2, c2)
arr = [[[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(5)]
for r1 in range(5):
    for c1 in range(5):
        for r2 in range(r1, 5):
            for c2 in range(c1, 5):
                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        arr[r1][c1][r2][c2] |= (1 << (r * 5 + c))


def calc(b):
    """
    Calcule récursivement et avec mémoïsation le nombre minimal de coups
    nécessaires pour nettoyer toutes les cases '1' du bitmask b via des
    rectangles pleins alignés sur la grille.

    Args:
        b (int): Un entier représentant l'état actuel de la grille (bitmask sur 25 bits).

    Returns:
        int: Le nombre minimal de coups nécessaires pour vider la grille.
    """
    if b == 0:
        # Si la grille est déjà vide, aucun coup n'est nécessaire
        return 0
    if memo[b] >= 0:
        # Si ce cas a déjà été résolu, renvoyer la solution mémorisée
        return memo[b]

    # Trouver la première case encore marquée (la moins indexée en ligne/colonne)
    found = False
    for r1 in range(n):
        for c1 in range(n):
            if b & (1 << (5 * r1 + c1)):
                found, rr, cc = True, r1, c1
                break
        if found:
            break
    if not found:
        # Ne devrait pas arriver, mais sécurité
        memo[b] = 0
        return 0

    ans = 25  # Valeur maximale (impossible de dépasser 25 coups)
    # Tester tous les rectangles possibles partant de (rr, cc) jusqu'à fin de la grille
    for r2 in range(rr, n):
        for c2 in range(cc, n):
            # Appliquer le rectangle : on efface toutes les cases couvertes
            k = b ^ arr[rr][cc][r2][c2]
            ans = min(ans, calc(k) + 1)

    memo[b] = ans  # Mémorisation du résultat
    return ans


def main():
    """
    Fonction principale. Lit les entrées, construit l'état initial de la grille,
    appelle la fonction de résolution et affiche le résultat conformément au problème.
    """
    while True:
        # Lecture de la taille de la grille (n)
        global n
        n = int(input())
        if n == 0:
            break

        # Lecture de la grille -- 1 représente une case à nettoyer, 0 une case déjà propre
        a = [list(map(int, input().split())) for _ in range(n)]
        b = 0  # Encodage de la grille sous forme d'entier (bitmask)
        for r in range(n):
            for c in range(n):
                if a[r][c]:
                    b |= 1 << (5 * r + c)

        # Appel de la fonction principale et affichage du résultat
        # 'myon' doit être écrit autant de fois qu'il faut de coups
        print("myon" * calc(b))


if __name__ == "__main__":
    main()