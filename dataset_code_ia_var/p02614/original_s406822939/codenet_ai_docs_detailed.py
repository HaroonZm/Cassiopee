from itertools import combinations
import numpy as np

def main():
    """
    Lit les paramètres du problème, effectue le traitement et affiche le résultat final.
    L'utilisateur doit entrer trois entiers séparés par des espaces pour la taille de la grille et K, suivis de H lignes décrivant la grille composée de '.' (case vide) et '#' (case noire).
    """
    # Lecture des dimensions de la grille (H: lignes, W: colonnes) et du nombre cible K
    H, W, K = map(int, input().split())
    
    # Création de la grille C (H lignes, chacun une liste de caractères)
    C = [list(input()) for _ in range(H)]
    
    # Création d'une matrice numpy D pour stocker des 1 là où il y a des '#' et 0 ailleurs
    D = np.zeros((H, W), dtype=int)
    
    # Variable qui servira à compter le nombre de solutions valides
    a = 0

    # Remplit D avec 1 là où il y a une case noire ('#'), 0 sinon
    for h in range(H):
        for w in range(W):
            if C[h][w] == "#":
                D[h][w] = 1

    # Calcule le nombre total de cases noires initiales dans la grille
    T = np.sum(D)

    # Boucle sur tous les sous-ensembles de lignes à masquer
    for h in range(H + 1):  # de 0 à H lignes à masquer
        for I in combinations(range(H), h):  # Choix des lignes à masquer
            # Boucle sur tous les sous-ensembles de colonnes à masquer
            for w in range(W + 1):  # de 0 à W colonnes à masquer
                for J in combinations(range(W), w):  # Choix des colonnes à masquer
                    # Calcul du nombre total de cases noires supprimées
                    S = 0

                    # Ajoute les cases noires supprimées des lignes masquées
                    for i in I:
                        for ww in range(W):
                            S += D[i][ww]
                    
                    # Ajoute les cases noires supprimées des colonnes masquées
                    for j in J:
                        for hh in range(H):
                            S += D[hh][j]

                    # Soustrait les cases en double comptées (cellules à l'intersection des lignes et colonnes masquées)
                    for i in I:
                        for j in J:
                            S -= D[i][j]
                    
                    # Si le nombre de cases noires restantes est égal à K, incrémente la réponse
                    if K == T - S:
                        a += 1

    # Affiche le résultat final
    print(a)

if __name__ == "__main__":
    main()