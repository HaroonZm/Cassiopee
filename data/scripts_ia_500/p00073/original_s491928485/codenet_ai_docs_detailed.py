def calculate_area():
    """
    Fonction principale qui lit en boucle des paires de valeurs entières x et h,
    calcule une surface spécifique, puis affiche le résultat.
    La boucle s'arrête lorsque les deux valeurs saisies sont égales à zéro.

    La surface calculée correspond à la somme d'un carré de côté x et de deux triangles 
    isocèles de base x et hauteur t, où t est la longueur de la diagonale calculée par le théorème de Pythagore.
    """
    while True:
        # Lecture de la valeur entière x depuis l'entrée utilisateur
        x = int(input())
        # Lecture de la valeur entière h depuis l'entrée utilisateur
        h = int(input())

        # Condition d'arrêt : si x et h valent tous deux 0, on quitte la boucle
        if x == 0 and h == 0:
            break
        else:
            # Calcul de la longueur t correspondante à l'hypoténuse d'un triangle rectangle
            # où les côtés sont h (hauteur) et x/2 (moitié de la base)
            t = (h**2 + (x / 2)**2)**0.5

            # Calcul de la surface totale:
            # - x * x : aire d'un carré de côté x
            # - x * t * 2 : aire totale de deux triangles isocèles dont la base est x et la hauteur t
            total_area = x * x + x * t * 2

            # Affichage de la surface calculée
            print(total_area)



# Exécution de la fonction principale
calculate_area()