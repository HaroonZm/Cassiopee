import sys

# Crée une plage de nombres de 0 à 1000 inclus
C = range(1001)
# Initialisation de l'indice de la ligne (0 ou 1)
m = 0
# Création d'une liste à deux dimensions contenant deux listes de 1001 zéros chacune
# Cette structure va compter la fréquence des entiers lus pour deux groupes différents
d = [[0 for i in C] for j in range(2)]

# Lecture de toutes les lignes depuis l'entrée standard
for s in sys.stdin.readlines():
    # Si la ligne est vide (contient seulement un saut de ligne),
    # on passe au groupe suivant en incrémentant m
    if s == "\n":
        m += 1
    else:
        # Sinon, la ligne contient deux entiers séparés par une virgule
        # On les convertit en entiers a et b
        a, b = map(int, s.split(','))
        # On incrémente le compteur d'apparitions de a dans le groupe m
        d[m][a] += 1

# Parcours de tous les entiers de 0 à 1000
for i in C:
    a = d[0][i]  # Nombre d'occurrences de i dans le premier groupe
    b = d[1][i]  # Nombre d'occurrences de i dans le deuxième groupe
    # Si l'entier i apparaît dans les deux groupes (au moins une fois dans chacun)
    if a and b:
        # On affiche l'entier i et la somme des occurrences dans les deux groupes
        print(i, a + b)