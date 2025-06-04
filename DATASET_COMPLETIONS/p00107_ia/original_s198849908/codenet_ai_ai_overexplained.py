import math  # Importe le module math qui fournit des fonctions mathématiques avancées, ici utilisée pour calculer la racine carrée.

output = []  # Initialise une liste vide nommée 'output' qui va stocker les résultats ("OK" ou "NA") pour chaque test.

while True:  # Démarre une boucle infinie qui continuera jusqu'à ce qu'on utilise 'break' pour en sortir.

    # Lit une ligne de l'entrée standard, sépare la chaîne en plusieurs morceaux basés sur les espaces,
    # puis convertit chacun de ces morceaux en un entier. Ces entiers sont assignés aux variables depth, width et height.
    depth, width, height = [int(item) for item in input().split(" ")]

    # Vérifie si les trois dimensions lues sont toutes égales à zéro.
    # Cela sert de condition d'arrêt pour la boucle infinie.
    if depth == 0 and width == 0 and height == 0:
        break  # Si toutes les dimensions sont zéro, on sort immédiatement de la boucle 'while True'.

    # Calcule le rayon du fromage en utilisant la racine carrée de la somme des carrés de la moitié de la largeur et de la moitié de la hauteur.
    # Cette opération correspond à la distance du centre à un coin du rectangle (hypoténuse d'un triangle rectangle).
    cheeseRadius = math.sqrt((width / 2)**2 + (height / 2)**2)

    # Lit un entier de l'entrée standard qui représente le nombre d'entrées suivantes à traiter (nombre de rayons d'entrée).
    inputCount = int(input())

    # Démarre une boucle qui s'exécutera 'inputCount' fois, variable lp représentant l'index de cette boucle.
    for lp in range(inputCount):
        # Lit un entier depuis l'entrée standard qui représente le rayon de l'entrée actuelle.
        entranceRadius = int(input())

        # Compare le rayon du fromage calculé précédemment avec le rayon de l'entrée.
        # Si le rayon du fromage est inférieur à celui de l'entrée, cela signifie que l'entrée est suffisamment grande.
        if cheeseRadius < entranceRadius:
            output.append("OK")  # Ajoute la chaîne de caractères "OK" à la liste des résultats.
        else:
            output.append("NA")  # Ajoute la chaîne de caractères "NA" à la liste des résultats si l'entrée est trop petite.

# Après avoir traité toutes les entrées, imprime tous les résultats stockés dans la liste 'output',
# en séparant chaque résultat par un saut de ligne pour une meilleure lisibilité.
print("\n".join(output))