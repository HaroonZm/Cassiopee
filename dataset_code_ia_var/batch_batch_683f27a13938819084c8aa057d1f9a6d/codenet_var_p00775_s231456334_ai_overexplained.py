# Début d'une boucle infinie : cette boucle continuera de s'exécuter sans interruption
# jusqu'à ce qu'une instruction break soit rencontrée à l'intérieur.
while True:
    # Lecture d'une ligne de l'entrée standard (typiquement l'utilisateur ou un fichier),
    # découpage de cette ligne en morceaux selon les espaces, conversion de chaque morceau
    # en entier. Le résultat est affecté à deux variables : R et N.
    R, N = map(int, input().split())
    
    # Vérification si R et N sont tous les deux nuls.
    # L'opérateur "|" est un OU inclusif en binaire, donc (R | N) est nul seulement si
    # R == 0 ET N == 0. Si c'est le cas, cela signifie qu'il faut arrêter la boucle.
    # L'opérateur "not" inverse le booléen, donc l'instruction break s'exécute si R et N sont nuls.
    if not (R | N):
        break  # Sort de la boucle infinie pour terminer le programme.

    # Définition d'un décalage (offset) de 20 unités appelé "geta".
    # Ce décalage est utilisé pour décaler les indices et éviter des indices négatifs dans le tableau.
    geta = 20

    # Création d'une liste "buildings" initialisée à 0, contenant (geta * 2) éléments.
    # Cette liste simulera la hauteur maximale pour chaque position horizontale prise en compte.
    buildings = [0] * (geta * 2)

    # Boucle sur le nombre N d'immeubles à traiter.
    for _ in range(N):
        # Lecture d'une ligne de l'entrée standard, séparation des trois valeurs,
        # conversion en entiers : xl (début de l'immeuble), xr (fin de l'immeuble), h (hauteur).
        xl, xr, h = map(int, input().split())

        # Boucle sur chaque position comprise entre xl et xr (non inclus),
        # en ajoutant le décalage geta pour indexer la liste 'buildings' sans sortir des bornes
        for i in range(xl + geta, xr + geta):
            # On met à jour la hauteur maximale rencontrée à cette position. Si la hauteur
            # courante dans la liste est inférieure à h, on la remplace.
            buildings[i] = max(buildings[i], h)

    # Initialisation de la variable de réponse 'ans' à 20, valeur élevée fixée arbitrairement.
    # Cette variable stockera finalement la hauteur minimale sur la section considérée.
    ans = 20

    # Boucle sur chaque position i allant de -R + geta à R + geta (exclu).
    # Cela permet de parcourir les positions sur un segment symétrique centré sur 0 (avec décalage).
    for i in range(-R + geta, R + geta):
        # Vérification si l'indice i se situe à gauche du point central (avant le décalage geta).
        if i < geta:
            # Si c'est à gauche, on réduit la hauteur à cette position dans 'buildings' d'une valeur.
            # pow(R * R - (i - geta + 1) * (i - geta + 1), 0.5) calcule la racine carrée,
            # soit la hauteur du cercle de rayon R à la position i.
            # On enlève cette valeur de R pour obtenir la différence avec la base.
            buildings[i] -= pow(R * R - (i - geta + 1) * (i - geta + 1), 0.5) - R
        else:
            # Sinon, c'est à droite ou au centre : même logique mais calculée différemment.
            buildings[i] -= pow(R * R - (i - geta) * (i - geta), 0.5) - R

        # Mise à jour de la valeur minimale : ans prend la plus petite valeur entre son état actuel
        # et la hauteur à cette position (potentiellement réduite par les calculs précédents).
        ans = min(ans, buildings[i])
    
    # Affichage du résultat final : la hauteur minimale trouvée sur la section analysée.
    print(ans)