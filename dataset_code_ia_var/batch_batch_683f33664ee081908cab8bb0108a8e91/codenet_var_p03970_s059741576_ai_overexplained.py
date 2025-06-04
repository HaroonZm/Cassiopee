import sys  # On importe le module sys, qui donne accès à des fonctionnalités spécifiques de l'interpréteur Python

# On lit une ligne entrée par l'utilisateur depuis l'entrée standard (standard input)
# sys.stdin.readline() lit la ligne avec le caractère de retour à la ligne à la fin
S = sys.stdin.readline().strip()  # .strip() enlève les espaces blancs (y compris le retour à la ligne) en début et fin de chaîne

# On définit une chaîne de caractères littérale appelée 'template'
# Cette chaîne représente le texte avec lequel on veut comparer l'entrée
template = 'CODEFESTIVAL2016'  # Chaîne de référence pour la comparaison

# On initialise une variable entière appelée 'res', qui servira à compter le nombre de différences entre S et template
res = 0  # Mettre à zéro car aucune différence détectée pour l'instant

# On initialise une variable d'indice, 'i', pour parcourir caractère par caractère les chaînes
i = 0  # Commence à indiquer le premier caractère (l'indice zéro, c'est-à-dire le début de la chaîne)

# On entre dans une boucle while, qui continuera tant que 'i' est strictement inférieur à la longueur de la chaîne S
# Cela permet de comparer chaque caractère de S et template position par position
while i < len(S):  # len(S) renvoie le nombre total de caractères dans S
    # À chaque itération, on compare le caractère à la position i de la chaîne S avec celui de la même position dans template
    if S[i] != template[i]:  # Si les deux caractères sont différents...
        res += 1  # ...on incrémente le compteur des différences (res) de 1

    i += 1  # N'oublie pas d'incrémenter l'indice pour passer au caractère suivant

# Une fois la boucle terminée, on affiche le résultat (le nombre total de différences entre S et template)
print res  # Affichage en sortie standard ('print' sans parenthèse car syntaxe Python 2)