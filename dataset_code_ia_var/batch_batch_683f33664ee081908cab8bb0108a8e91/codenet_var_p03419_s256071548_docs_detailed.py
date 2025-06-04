def compute_free_cells(n: int, m: int) -> int:
    """
    Calcule le nombre de cases restant dans une grille n x m après suppression du périmètre.
    
    Si la grille est de 1x1, retourne 1.
    Si la grille a une dimension égale à 1 (ligne ou colonne), compte le retrait des cases du périmètre.
    Sinon, retire les cases des bords de la grille.
    
    Args:
        n (int): Nombre de lignes dans la grille.
        m (int): Nombre de colonnes dans la grille.
        
    Returns:
        int: Nombre de cases restant après suppression du périmètre.
    """
    peremeter = 0  # Initialise le compteur de cases de périmètre à supprimer

    # Cas particulier : grille 1x1, aucune suppression à effectuer
    if n == 1 and m == 1:
        pass  # Rien à supprimer, la case centrale existe seule
    # Si la grille ne possède qu'une ligne ou qu'une colonne
    elif n == 1 or m == 1:
        peremeter += 2  # On retire les deux extrémités (le cas 1x1 est traité au-dessus)
    else:
        peremeter += (n - 1) * 2  # On retire les cases du haut et du bas, sauf doublon aux coins
        peremeter += (m - 1) * 2  # On retire les cases de gauche et droite, sauf doublon aux coins

    ans = n * m - peremeter  # Calcule le nombre de cases restantes
    return ans

def main():
    """
    Lit l'entrée standard pour recevoir deux entiers n et m, puis affiche
    le nombre de cases restantes dans une grille n x m après suppression du périmètre.
    """
    # Lecture des dimensions de la grille depuis l'entrée standard
    n, m = map(int, input().split())
    
    # Calcul et affichage du résultat
    result = compute_free_cells(n, m)
    print(result)

if __name__ == "__main__":
    main()