def solve():
    """
    Calcule et affiche le nombre maximal de cellules accessibles dans une grille N x M,
    en supposant que les cellules le long du bord sont inaccessibles.
    
    - Si la grille fait 1x1, la seule cellule est accessible (cas spécial).
    - Si la grille est une ligne (N==1) ou une colonne (M==1), seules les cellules non sur les bords sont accessibles.
    - Sinon, seules les cellules à l'intérieur du pavé (non sur les bords) sont accessibles.
    
    Entrée :
    - Deux entiers N et M provenant de l'entrée standard.
    
    Sortie :
    - Un entier représentant le nombre de cellules accessibles, affiché sur la sortie standard.
    """
    # Lit les entiers N et M depuis l'entrée standard
    N, M = map(int, input().split())
    
    # Cas particulier : si la grille fait 1x1, la seule cellule est accessible
    if N == 1 and M == 1:
        print(1)
        return

    # Cas d'une grille avec une seule ligne : seules les cellules non sur les bords sont accessibles
    if N == 1:
        print(M - 2)
        return

    # Cas d'une grille avec une seule colonne : seules les cellules non sur les bords sont accessibles
    if M == 1:
        print(N - 2)
        return

    # Cas général : seules les cellules non sur le bord sont accessibles, soit (N-2)*(M-2)
    print((N - 2) * (M - 2))

if __name__ == "__main__":
    # Appelle la fonction principale lorsqu'on exécute ce script directement
    solve()