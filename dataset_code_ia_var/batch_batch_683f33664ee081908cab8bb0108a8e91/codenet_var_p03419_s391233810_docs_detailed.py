def calculate_cells(N, M):
    """
    Calcule le nombre de cellules intérieures ou accessibles selon les dimensions données.

    Si la grille a une seule cellule (1x1), retourne 1.
    Si la grille est une ligne ou une colonne (N == 1 ou M == 1), retourne le nombre de cellules moins les bords.
    Sinon, retourne le nombre de cellules internes non adjacentes au bord.

    Paramètres :
        N (int): nombre de lignes de la grille.
        M (int): nombre de colonnes de la grille.

    Retourne :
        int: nombre de cellules internes accessibles selon la configuration de la grille.
    """
    # Cas particulier : grille 1x1
    if N == 1 and M == 1:
        return 1
    # Cas où la grille est une ligne ou une colonne (bordures exclus)
    elif N == 1 or M == 1:
        return max(N, M) - 2
    # Cas général : grille au moins 2x2, seules les cellules internes comptent
    else:
        return (N - 2) * (M - 2)

def main():
    """
    Fonction principale qui lit les dimensions de la grille,
    appelle la fonction de calcul et affiche le résultat.
    """
    # Lecture des dimensions N (lignes) et M (colonnes) depuis l'entrée standard
    N, M = map(int, input().split())

    # Appel du calcul et affichage du résultat
    print(calculate_cells(N, M))

# Exécution du programme principal si ce fichier est exécuté directement
if __name__ == "__main__":
    main()