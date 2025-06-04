# Demande à l'utilisateur de saisir une chaîne de caractères depuis le clavier.
# La fonction input() attend que l'utilisateur tape quelque chose et appuie sur entrée.
tmp = input()

# Utilise la fonction len() qui retourne le nombre de caractères dans la chaîne 'tmp'.
# Vérifie si la longueur de la chaîne entrée par l'utilisateur est exactement égale à 3.
if len(tmp) == 3:
    # Si la longueur de la chaîne 'tmp' est de 3 caractères,
    # on va afficher la chaîne à l'envers.
    # L'opérateur de tranchage [::-1] signifie que l'on parcourt la chaîne de la fin vers le début,
    # en utilisant un pas de -1, ce qui retourne une nouvelle chaîne inversée.
    print(tmp[::-1])
else:
    # Si la longueur de la chaîne n'est pas de 3 caractères (c'est-à-dire si elle est inférieure ou supérieure à 3),
    # alors on affiche simplement la chaîne comme elle a été saisie, sans la modifier.
    print(tmp)