# Demande à l'utilisateur de saisir un nombre entier, puis convertit l'entrée utilisateur (qui est initialement une chaîne de caractères) en un entier.
# La valeur saisie représentera la longueur maximale autorisée pour la chaîne de caractères suivante.
n = int(input())

# Demande à l'utilisateur de saisir une chaîne de caractères.
# Cette chaîne de caractères sera peut-être tronquée selon sa longueur par rapport à la valeur de n.
s = input()

# Vérifie si la longueur de la chaîne de caractères (c'est-à-dire le nombre de caractères dans la variable 's')
# est strictement supérieure à la valeur de 'n' entrée précédemment par l'utilisateur.
if len(s) > n:
    # Si la chaîne de caractères est trop longue, cette instruction sera exécutée.
    # 's[:n]' signifie extraire une sous-chaîne de 's' allant du début (index 0) jusqu'à l'index n exclus (donc n caractères).
    # On ajoute ensuite le texte littéral '...' (points de suspension) à la fin de la sous-chaîne extraite
    # pour indiquer que la chaîne originale a été coupée/tronquée.
    print(s[:n] + '...')
else:
    # Si la longueur de la chaîne 's' est inférieure ou égale à 'n',
    # alors la chaîne originale est affichée telle quelle, sans modification.
    print(s)