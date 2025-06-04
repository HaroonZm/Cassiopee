import math  # Importe le module math, permettant d'accéder à des fonctions mathématiques standards. Ici, il n'est pas nécessaire mais c'est conservé.

# Prend l'entrée utilisateur sous forme d'une chaîne de caractères, 
# divise cette chaîne à chaque espace, transforme chaque partie en entier grâce à map(int, ...),
# puis assigne ces deux entiers respectivement à n et l.
n, l = map(int, input().split())

# Initialise la variable all_taste à zéro. 
# Cette variable va contenir la somme totale des goûts de toutes les pommes,
# c'est-à-dire la somme de la saveur de chaque pomme prise une fois.
all_taste = 0  # au début la somme est zéro

# Cette boucle for itère sur tous les index (i) allant de 1 jusqu'à (y compris) n.
# Cela permet de calculer le goût de chaque pomme basée sur l'ordre (i).
for i in range(1, n + 1):  # commence à 1, finit à n inclus. Le premier argument de range est inclus, le deuxième est exclu.
    # Calcule la saveur actuelle de la pomme numéro i.
    # La saveur est définie comme l + i - 1. Cela signifie que la première pomme a la saveur l,
    # la seconde pomme est l + 1, etc.
    tmp = l + i - 1

    # Ajoute la valeur de tmp à la variable all_taste pour accumuler la somme totale.
    all_taste = all_taste + tmp

# Après la boucle précédente, all_taste contient maintenant la somme de toutes les saveurs, 
# c'est-à-dire le total de tous les goûts possibles si on mange toutes les pommes.

# Initialise la variable act_taste à 0. 
# Cette variable contiendra la somme effective de saveurs après avoir retiré la pomme optimale à ne pas manger.
act_taste = 0

# Initialisation de la variable eat_apple avec la saveur de la première pomme, 
# c'est-à-dire l + 1 - 1. Cela équivaut à l.
eat_apple = l + 1 - 1  # soit l

# Cette nouvelle boucle for parcourt chaque pomme pour déterminer laquelle il faut retirer pour
# minimiser la différence absolue du goût rejeté, c'est-à-dire celle dont la saveur (positive ou négative)
# est la plus proche possible de zéro. Cela permet de conserver un goût total le plus proche possible 
# de la somme totale originale.
for i in range(1, n + 1):  # itère sur chaque pomme pour déterminer laquelle ne pas manger
    # Calcule la saveur de la pomme en cours de vérification.
    cmp_apple = l + i - 1

    # Si la valeur absolue de cmp_apple (la saveur candidate) est plus petite ou égale que celle de eat_apple,
    # alors met à jour eat_apple, car on préfère supprimer une pomme dont la saveur est plus proche de zéro.
    if abs(cmp_apple) <= abs(eat_apple):
        eat_apple = cmp_apple  # met à jour la pomme à retirer

        # Calcule le goût total effectif (après avoir retiré la pomme eat_apple).
        act_taste = all_taste - eat_apple

# Affiche la valeur de act_taste, c'est-à-dire la somme des saveurs des n-1 pommes restantes,
# après avoir retiré la pomme ayant une saveur la plus proche de zéro.
print(act_taste)  # sortie finale du résultat