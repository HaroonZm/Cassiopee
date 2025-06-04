# Demande à l'utilisateur de saisir une ligne de texte contenant deux nombres séparés par un espace.
# La fonction input() lit cette ligne en tant que chaîne de caractères.
# La méthode split() découpe la chaîne en une liste de sous-chaînes, en utilisant l'espace comme séparateur.
# L'expression [int(num) for num in input().split()] est appelée une compréhension de liste.
# Elle parcourt chaque sous-chaîne (num), convertit chaque sous-chaîne en un entier avec int(num),
# puis construit une nouvelle liste de deux entiers à partir du texte saisi par l'utilisateur.
# Par exemple, si l'utilisateur entre "5 3", l'entrée devient ["5", "3"], qui devient [5, 3] comme résultat final.
h, r = [int(num) for num in input().split()]

# Vérifie si h est exactement égal à l'opposé de r (donc h == -r).
# Si c'est le cas, cela signifie que la somme des deux nombres est nulle (h + r == 0).
if h == -r:
    # Affiche la valeur 0 dans la sortie standard si la condition précédente est vraie.
    print(0)
# Si la condition précédente est fausse, vérifie si h est strictement supérieur à l'opposé de r.
# Cela signifie que la valeur de h est numériquement supérieure à -r.
elif h > -r:
    # Affiche la valeur 1 dans la sortie standard si cette deuxième condition est vraie.
    print(1)
# Si aucune des conditions précédentes n'est vraie (donc h < -r), ce bloc est exécuté.
else:
    # Affiche la valeur -1 dans la sortie standard.
    print(-1)