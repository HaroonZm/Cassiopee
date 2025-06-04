import sys  # Importe le module sys, qui fournit des fonctions pour interagir avec l'interpréteur Python, notamment pour l'entrée et la sortie standard

readline = sys.stdin.readline  # Associe la fonction sys.stdin.readline à la variable readline pour lire les lignes de l'entrée standard
write = sys.stdout.write       # Associe la fonction sys.stdout.write à la variable write pour écrire sur la sortie standard

# Création d'une liste 'dp' de 601 éléments, chacun initialisé à 0. 
# 'dp' va servir à la programmation dynamique pour stocker des résultats intermédiaires.
dp = [0]*601  # Multiplie la liste [0] par 601 pour obtenir une liste de longueur 601, remplie de 0

dp[0] = 1  # Définit dp[0] à 1. Cela signifie qu'il existe exactement 1 façon d'obtenir une somme de 0, c'est-à-dire en ne choisissant rien.

# Liste des valeurs possibles de "pièces" (ici, des carrés parfaits de 1 à 17)
# Chaque élément représente la valeur d'une pièce disponible pour faire la somme.
V = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]

# Pour chaque valeur de pièce 'v' dans la liste V
for v in V:
    # On parcourt tous les entiers 'k' de 300 jusqu'à 0 (inclus) par pas de -1
    # On commence par les valeurs élevées pour ne pas double compter les combinaisons avec la même valeur de pièce
    for k in range(300, -1, -1):
        x = dp[k] # On stocke dans 'x' le nombre de façons d'obtenir la somme 'k' avec les pièces utilisées jusque là
        w = v     # On initialise 'w' avec la valeur de la nouvelle pièce 'v'
        # On utilise une boucle while pour ajouter plusieurs fois la pièce 'v' tant que la somme n'excède pas 300
        # Cela permet de compter toutes les combinaisons qui utilisent plusieurs fois la pièce 'v'
        while k+w <= 300:
            dp[k+w] += x  # On ajoute à dp[k+w] le nombre de façons d'obtenir 'k' car on ajoute 'v' à toutes les combinaisons de 'k'
            w += v        # On ajoute 'v' à 'w' pour considérer une combinaison supplémentaire avec une pièce 'v' en plus

# Boucle de traitement de l'entrée et affichage des résultats
while 1:  # Boucle infinie, qui sera arrêtée par le mot-clé break à l'intérieur
    N = int(readline())  # Lecture d'une ligne en entrée, puis conversion de la chaîne de caractères reçue en entier, stockée dans 'N'
    if not N:            # Si N vaut 0 (faux en contextes booléens)
        break            # On interrompt la boucle while infinie avec 'break'
    # On affiche le résultat correspondant, qui est dp[N]
    # On utilise l'opérateur de formatage % pour insérer la valeur de dp[N] dans l'emplacement %d de la chaîne
    # On ajoute un saut de ligne (\n) pour afficher chaque résultat sur une ligne séparée
    write("%d\n" % dp[N])