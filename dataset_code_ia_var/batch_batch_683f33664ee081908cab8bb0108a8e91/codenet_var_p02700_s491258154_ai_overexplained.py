# Le code commence par lire une ligne de l'entrée standard (typiquement le clavier).
# La fonction input() attend que l'utilisateur saisisse une ligne de texte et appuie sur "Entrée".
# split() divise cette ligne en une liste de morceaux (des chaînes de caractères), en séparant sur les espaces par défaut.
# map(int, ...) convertit chaque chaîne de caractères résultante en un entier (type int).
# Enfin, on utilise l'affectation multiple pour stocker chaque entier dans les variables A, B, C et D respectivement.
A, B, C, D = map(int, input().split())

# Calcule le nombre minimal de fois que l'on peut soustraire D à A avant d'atteindre ou de dépasser zéro, en arrondissant vers le haut.
# Autrement dit, ceci calcule le plafond de A / D.
# En mathématiques, cela revient à faire ceil(A / D).
# L'expression (A + D - 1) // D est un moyen courant d'obtenir ce plafond sans utiliser la fonction math.ceil().
# On stocke le résultat dans la variable 't'.
t = (A + D - 1) // D

# Calcule le nombre minimal de fois que l'on peut soustraire B à C avant d'atteindre ou de dépasser zéro, toujours en arrondissant vers le haut.
# Même principe que précédemment, mais avec C et B.
# On stocke ce résultat dans la variable 'a'.
a = (C + B - 1) // B

# On compare maintenant t et a.
# Si le nombre de tours t est supérieur ou égal au nombre de tours a, alors la condition est vérifiée.
if t >= a:
    # Si la condition t >= a est vraie, on affiche "Yes".
    # print() écrit la chaîne de caractères donnée dans la sortie standard (typiquement l'écran).
    print("Yes")
else:
    # Si la condition t >= a est fausse, donc t < a, on affiche "No".
    print("No")