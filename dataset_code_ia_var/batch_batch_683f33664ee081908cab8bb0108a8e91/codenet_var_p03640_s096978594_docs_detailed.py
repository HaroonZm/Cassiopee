def fill_grid(h, w, n, a):
    """
    Remplit une grille h x w avec n couleurs selon les instructions de la liste a.
    
    Chaque a[i] indique combien de cases consécutives doivent être colorées avec la couleur (i+1).
    Le remplissage se fait ligne par ligne mais l'affichage alterne l'ordre dans les lignes impaires.
    
    Args:
        h (int): Nombre de lignes de la grille.
        w (int): Nombre de colonnes de la grille.
        n (int): Nombre de couleurs.
        a (list[int]): Liste de tailles pour chaque couleur à appliquer.
    
    Returns:
        List[List[int]]: Grille complétée avec les couleurs appliquées.
    """
    # Initialisation de la grille (h lignes, w colonnes) avec des zéros.
    ans = [[0 for _ in range(w)] for _ in range(h)]
    nextColor = 0   # Indice de la prochaine couleur à utiliser (correspond à a)
    H = 0           # Indice de la ligne courante dans la grille
    W = 0           # Indice de la colonne courante dans la grille

    # Boucle jusqu'à ce que toutes les couleurs soient utilisées
    while nextColor < n:
        # Pour la couleur courante, remplir a[nextColor] cases dans la grille
        for j in range(a[nextColor]):
            # Affecte la couleur (indice + 1 car les couleurs sont numérotées de 1 à n)
            ans[H][W] = nextColor + 1
            W += 1   # Passe à la colonne suivante

            # Si on atteint la fin de la ligne, passer à la ligne suivante
            if W >= w:
                H += 1   # Ligne suivante
                W = 0    # Début de ligne

        # Passer à la couleur suivante après avoir rempli le nombre requis de cases
        nextColor += 1

    # Traitement pour alterner le sens de chaque ligne impaire lors de l'affichage
    for i in range(h):
        if i % 2 != 0:
            # Ligne impaire : on inverse l'ordre pour obtenir l'effet 'zigzag'
            ans[i] = ans[i][::-1]
    return ans

def main():
    """
    Point d'entrée du programme.
    Récupère les entrées utilisateurs, appelle la fonction de remplissage de grille,
    puis affiche chaque ligne de la grille formatée.
    """
    # Lecture des dimensions de la grille
    h, w = map(int, input().split())
    # Nombre de couleurs
    n = int(input())
    # Liste contenant le nombre de cases à remplir pour chaque couleur
    a = list(map(int, input().split()))

    # Remplir la grille avec les couleurs selon les instructions
    grid = fill_grid(h, w, n, a)

    # Affichage ligne par ligne
    for row in grid:
        print(*row)

if __name__ == "__main__":
    main()