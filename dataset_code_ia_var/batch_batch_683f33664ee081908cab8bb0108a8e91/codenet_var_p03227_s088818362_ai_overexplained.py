# Demande à l'utilisateur de saisir une chaîne de caractères à l'aide de la fonction input().
# La fonction input() affiche une invite vide (car aucune chaîne n'est passée en argument) et attend que l'utilisateur entre une valeur au clavier.
# Lorsque l'utilisateur appuie sur la touche Entrée, la chaîne saisie est renvoyée par la fonction input() et affectée à la variable 's'.
s = input()

# On vérifie ensuite la longueur de la chaîne 's' avec la fonction len().
# len(s) calcule le nombre de caractères dans la chaîne 's'.
# L'expression 'len(s)==2' vérifie si la longueur de 's' est égale à 2.
if len(s) == 2:
    # Si la condition est vraie, c'est-à-dire que 's' contient exactement deux caractères,
    # on affiche 's' sans modification à l'aide de la fonction print().
    print(s)
else:
    # Si la condition est fausse, c'est-à-dire que la longueur de 's' n'est pas égale à 2,
    # on affiche la chaîne 's' inversée.
    # Pour inverser la chaîne, on utilise la notation de tranchage (slicing) s[::-1].
    # L'opérateur de tranchage s[start:stop:step] permet de sélectionner une partie de la chaîne.
    # Ici, 'start' et 'stop' sont omis, donc on prend toute la chaîne.
    # Le 'step' de -1 signifie que l'on parcourt la chaîne à rebours, du dernier caractère au premier.
    print(s[::-1])