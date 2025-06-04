# Demande à l'utilisateur de saisir une valeur entière pour la variable A.
# La fonction raw_input() lit une chaîne de caractères depuis l'entrée standard (généralement le clavier).
# La fonction int() convertit cette chaîne de caractères en un nombre entier.
A = int(raw_input())

# Demande à l'utilisateur de saisir une valeur entière pour la variable B, de la même manière que ci-dessus.
B = int(raw_input())

# Demande à l'utilisateur de saisir une valeur entière pour la variable C.
C = int(raw_input())

# Calcule la valeur de S en multipliant la valeur saisie pour C par 3.
# L'opérateur '*' effectue la multiplication.
S = 3 * C

# Calcule X13 en soustrayant les valeurs de A et B du résultat de S.
# Cet opérateur '-' effectue la soustraction.
X13 = S - A - B

# Calcule X21 en multipliant S par 2, puis en soustrayant deux fois A, deux fois C, et une fois B.
# Les expressions arithmétiques sont évaluées de gauche à droite selon la priorité des opérateurs.
X21 = 2 * S - 2 * A - 2 * C - B

# Calcule X23 en additionnant deux fois la valeur de A, la valeur de B, et la valeur de C, puis en soustrayant S.
X23 = 2 * A + B + C - S

# Calcule X31 en ajoutant deux fois C, la valeur de A et B, puis en soustrayant S.
X31 = 2 * C + A + B - S

# Calcule X32 en soustrayant la valeur de B et de C à S.
X32 = S - B - C

# Calcule X33 en soustrayant la valeur de A et C à S.
X33 = S - A - C

# Affiche les résultats sur la première ligne.
# Le symbole % permet de formatter les valeurs dans une chaîne de caractères selon leur type.
# Ici, '%d' attend une valeur entière pour l'affichage.
# Les valeurs de A, B, et X13 sont affichées séparées par des espaces.
print "%d %d %d" % (A, B, X13)

# Affiche sur la deuxième ligne les valeurs de X21, C et X23, dans le même format.
print "%d %d %d" % (X21, C, X23)

# Affiche sur la troisième ligne les valeurs de X31, X32 et X33, toujours dans le même format.
print "%d %d %d" % (X31, X32, X33)