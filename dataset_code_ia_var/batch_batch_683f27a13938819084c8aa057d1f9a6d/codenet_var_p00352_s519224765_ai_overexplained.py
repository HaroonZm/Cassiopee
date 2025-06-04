# On demande une entrée à l'utilisateur avec la fonction input().
# L'utilisateur doit saisir deux nombres entiers séparés par un espace.
# La méthode split() découpe la chaîne d'entrée en une liste de chaînes à chaque espace rencontré.
# La fonction map(int, ...) applique la conversion en entier (int) à chaque élément de la liste générée par split().
# Les deux valeurs converties en entiers sont ensuite affectées respectivement aux variables a et b grâce à l'opérateur d'affectation multiple (=).
a, b = map(int, input().split())

# On additionne les deux nombres (a et b) à l'aide de l'opérateur +.
# Le résultat (a + b) est ensuite divisé par 2 à l'aide de l'opérateur de division entière // pour obtenir un entier (cette opération arrondit à l'entier inférieur si nécessaire).
# La fonction print() affiche le résultat sur la sortie standard (en général à l'écran), c'est-à-dire l'entier qui est la moyenne arithmétique arrondie à l'inférieur des deux nombres saisis.
print((a + b) // 2)