def min_stroke_path():
    """
    Calcule le nombre minimal de traits requis pour parcourir une grille en partant du coin supérieur gauche,
    en ne changeant de trait que lorsque le caractère rencontré diffère du précédent.
    Les cases sont remplies de "." ou de "#". La fonction lit la hauteur (h) et la largeur (w) de la grille,
    puis la grille elle-même en entrée standard.

    La logique utilise une programmation dynamique sur la dernière ligne lue, 
    en stockant le nombre minimal de changements nécessaires pour chaque colonne lors du parcours.
    
    Entrée :
        Sur la première ligne : deux entiers h et w (hauteur et largeur de la grille)
        Puis h lignes, chacune de longueur w, ne contenant que les caractères "." ou "#"
        
    Sortie :
        Affiche le nombre minimal de "traits" à effectuer pour parcourir la grille (un entier)
    """
    # Lire les dimensions de la grille
    h, w = map(int, input().split())
    
    # d[j] : nombre minimal de changements/coups nécessaires pour atteindre la case (i, j)
    # Initialisé à 0 pour d[0] (garde-fou), puis à une valeur élevée (300) pour les autres
    d = [0] + [300] * w
    
    # a contiendra le caractère de la première case de la grille, utilisé ultérieurement
    for i in range(h):
        s = input()  # Lecture d'une ligne de la grille
        if i == 0:
            a = s[0]  # Caractère de départ (première case de la grille)
        for j in range(w):
            # On est sur une case dont le contenu est s[j]
            # t est True (1) si le caractère courant est égal au caractère de départ (a), sinon False (0)
            t = s[j] == a
            
            # On augmente d[j] si le nombre actuel d[j] est pair, selon la parité et la couleur désirée
            d[j] += t ^ (d[j] % 2 == 0)
            
            if j > 0:
                # Pour bouger à droite, on prend le minimum entre :
                # - continuer par le haut (d[j], déjà mis à jour)
                # - continuer par la gauche (coût d[j-1] + un éventuel changement selon la couleur)
                d[j] = min(d[j], d[j-1] + t ^ (d[j-1] % 2 == 0))
    
    # Calcul final :
    # - d[-2] correspond au coût d'arrivée dans la dernière case de la grille (en bas à droite)
    # - a == "#" : on ajoute 1 si la première case est un "#"
    # - le +1 et la division par 2 normalisent le nombre de changements
    print((d[-2] + (a == "#") + 1) // 2)

# Lancer la fonction principale
min_stroke_path()