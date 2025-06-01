def search(x, y):
    # Initialisation des variables représentant les limites du rectangle courant
    # x_min et y_min représentent les coordonnées minimales sur les axes x et y respectivement
    # x_max et y_max représentent les coordonnées maximales sur les axes x et y respectivement
    x_min = 0  # Limite minimale en x, initialisée à 0
    y_min = 0  # Limite minimale en y, initialisée à 0
    x_max = 0  # Limite maximale en x, initialisée à 0
    y_max = 0  # Limite maximale en y, initialisée à 0

    # f, f1 et f2 sont des variables utilisées pour générer la suite de Fibonacci de manière itérative
    # On utilise cette suite pour agrandir progressivement les limites sur x et y
    f = 0      # Variable temporaire qui va contenir la somme de f1 et f2 à chaque étape
    f1 = 1     # Le premier nombre de la suite de Fibonacci initialisé à 1
    f2 = 0     # Le second nombre de la suite de Fibonacci initialisé à 0

    # p est un compteur qui représentera le numéro de l'itération en cours
    # Il sert aussi à déterminer la direction d'expansion du rectangle en fonction de p modulo 4
    p = 0

    # Boucle infinie qui sera interrompue par un return dès que le point (x,y) sera dans le rectangle
    while(True):
        # Vérification si le point (x,y) se trouve à l'intérieur ou sur le bord du rectangle défini par:
        # x_min <= x <= x_max et y_min <= y <= y_max
        # Si oui, renvoyer la valeur de p modulo 3 plus 1.
        # Cette valeur représente un label ou un identifiant lié au nombre d'itérations modulo 3, décalé de 1 à 3.
        if ( x_min <= x and x <= x_max and y_min <= y and y <= y_max ):
            return p % 3 + 1

        # Calcul du prochain nombre dans la suite de Fibonacci
        # La suite commence 0,1,1,2,3,5,... f est la somme des deux termes précédents f1 et f2
        f = f1 + f2

        # Détermination de la direction dans laquelle le rectangle doit être étendu selon la valeur de p modulo 4:
        # p % 4 == 0 => direction est (vers l'est), on étend la limite maximale x_max vers la droite (axe x positif)
        # p % 4 == 1 => direction nord, on étend la limite maximale y_max vers le haut (axe y positif)
        # p % 4 == 2 => direction ouest, on diminue la limite minimale x_min vers la gauche (axe x négatif)
        # p % 4 == 3 => direction sud, on diminue la limite minimale y_min vers le bas (axe y négatif)
        if ( p % 4 == 0 ):
            x_max += f  # On ajoute f à la limite maximale en x pour étendre vers l’est
        elif ( p % 4 == 1 ):
            y_max += f  # On ajoute f à la limite maximale en y pour étendre vers le nord
        elif ( p % 4 == 2 ):
            x_min -= f  # On soustrait f à la limite minimale en x pour étendre vers l’ouest
        else:
            y_min -= f  # On soustrait f à la limite minimale en y pour étendre vers le sud

        # Mise à jour des termes précédents de la suite de Fibonacci pour la prochaine itération
        # f2 prend la valeur de f1 (le terme juste avant)
        # f1 prend la valeur de f (le terme calculé lors de cette itération)
        f2 = f1
        f1 = f

        # Incrémentation du compteur d’itérations p pour passer à la prochaine direction et nombre de Fibonacci
        p = p + 1

# Lecture de deux entiers x et y à partir de l'entrée standard (typiquement la console),
# séparés par un espace. map(int, input().split()) convertit ces valeurs en entiers.
x, y = map(int, input().split())

# Appel de la fonction search en lui passant les coordonnées x et y ainsi récupérées
# Affichage du résultat retourné par la fonction search
print(search(x, y))