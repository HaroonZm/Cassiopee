import bisect

# Boucle infinie pour traiter plusieurs entrées
while True:
    try:
        # Lecture de la ligne d'entrée utilisateur
        # input() récupère une chaîne de caractères saisie par l'utilisateur
        # split() découpe cette chaîne en une liste de sous-chaînes selon les espaces
        # map(float, ...) applique la fonction float à chaque élément de la liste pour les convertir en nombres à virgule flottante
        # On attribue ces deux valeurs converties aux variables n et m respectivement
        n, m = map(float, input().split())

        # Définition d'une liste de seuils pour la variable n
        # Ces seuils sont des nombres flottants représentant des points de coupure pour une classification
        m500 = [35.5, 37.5, 40, 43, 50, 55, 70]

        # Définition d'une liste de seuils pour la variable m
        m1000 = [71, 77, 83, 89, 105, 116, 148]

        # Utilisation de la fonction bisect_left pour trouver la position où insérer n+0.001 dans la liste m500
        # Afin de maintenir l'ordre croissant
        # bisect_left retourne l'index d'insertion à gauche qui garantit que la liste reste triée
        # L'ajout de 0.001 permet de traiter les valeurs limites de manière inclusive
        r1 = bisect.bisect_left(m500, n + 0.001)

        # De même, trouver la position pour insérer m+0.001 dans la liste m1000
        r2 = bisect.bisect_left(m1000, m + 0.001)

        # Définition de la liste des rangs correspondants aux indices trouvés
        # Chaque index correspond à un rang de qualité ou catégorie représenté par une chaîne de caractères
        rank = ["AAA", "AA", "A", "B", "C", "D", "E", "NA"]

        # Calcul de l'index final en prenant le maximum des deux indices r1 et r2
        # Cela signifie que la classification finale sera basée sur le pire classement entre les deux critères
        index = max(r1, r2)

        # Affichage du rang correspondant à l'index calculé
        print(rank[index])
    except:
        # En cas d'erreur (par exemple fin d'entrée, saisie invalide), sortir de la boucle infinie pour arrêter le programme
        break