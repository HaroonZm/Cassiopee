# Démarre une boucle infinie qui ne s'arrêtera que si on rencontre un 'break' explicite
while True:
    # Lecture de l'entrée utilisateur sous forme de chaîne de caractères, contenant deux entiers séparés par un espace
    # La méthode 'input()' lit une ligne au clavier
    # 'split()' sépare la chaîne en une liste de sous-chaînes (par défaut sur des espaces)
    # 'map(int, ...)' convertit chaque sous-chaîne en entier
    # a et b reçoivent ces deux entiers respectivement via unpacking
    a, b = map(int, input().split())

    # Vérifie s'il s'agit du cas d'arrêt où les deux valeurs saisies sont nulles
    # La comparaison 'a == b == 0' vérifie que a vaut 0 ET que b vaut 0
    if a == b == 0:
        # Sortir la boucle 'while', ce qui arrête le programme
        break

    # Calcul de la valeur entière de la division de b par a (division entière)
    # Cela donne le quotient sans virgule, car // signifie division entière dans Python
    h = b // a

    # Demande à l'utilisateur de saisir une liste d'entiers sur une ligne, séparés par des espaces
    # 'map(int, input().split())' crée un itérable d'entiers à partir de la saisie utilisateur
    # 'list(...)' transforme cet itérable d'entiers en une vraie liste pour permettre plusieurs parcours
    for c in list(map(int, input().split())):
        # Pour chaque valeur entière 'c' dans la liste saisie
        # La condition 'c < h' vérifie si la valeur c est strictement inférieure à h
        if c < h:
            # Si oui, effectuer une soustraction sur b :
            # Soustraire de b la différence entre h et c
            # Cela revient à retirer du total b la quantité que c a en moins par rapport à h
            b -= h - c  # b = b - (h - c)

    # Affiche la valeur finale de b après tous les ajustements
    # 'print()' affiche son argument suivi d'un saut de ligne
    print(b)