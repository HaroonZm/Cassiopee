# Demande à l'utilisateur de saisir un nombre entier et convertit l'entrée (qui est toujours une chaîne de caractères) en un int.
# Cette valeur sera stockée dans la variable X.
X = int(input())

# Demande à l'utilisateur de saisir un deuxième nombre entier, puis convertit également cette entrée en un int.
# Cette valeur sera stockée dans la variable A.
A = int(input())

# Demande à l'utilisateur de saisir un troisième nombre entier, convertit la chaîne de caractères en int.
# Cette valeur sera stockée dans la variable B.
B = int(input())

# Calcule la différence entre la valeur de X et la valeur de A.
# Puis, applique l'opérateur modulo (%) avec la valeur de B, c'est-à-dire qu'on cherche le reste de la division euclidienne de (X - A) par B.
# Le résultat est alors envoyé à la fonction print(), qui affiche cette valeur dans la console.
print((X - A) % B)