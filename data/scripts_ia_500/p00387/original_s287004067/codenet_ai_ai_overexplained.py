# Demander à l'utilisateur d'entrer deux nombres entiers séparés par un espace.
# input() est une fonction intégrée qui lit une ligne de texte depuis l'entrée standard (généralement le clavier).
# La chaîne de caractères résultante sera par exemple "3 7" si l'utilisateur tape ces chiffres.
# La méthode split() appliquée à cette chaîne découpe cette chaîne en une liste de sous-chaînes,
# selon l'espace par défaut comme séparateur. Par exemple "3 7".split() donne ["3", "7"].
# map(int, ...) applique la fonction int à chaque élément de la liste obtenue,
# transformant les sous-chaînes de caractères en entiers, par exemple 3 et 7.
# list(...) convertit l'objet itérable résultant de map en liste explicite afin de permettre l'affectation simultanée.
n, m = list(map(int, input().split()))

# Calculer le nombre de fois que n rentre dans m par division entière (//).
# L'opérateur // réalise une division entière qui donne la partie entière du quotient.
# m // n correspond donc au nombre entier de fois que n peut être contenu dans m.
# Ensuite on calcule le reste de la division de m par n avec l'opérateur modulo %.
# L'expression (m % n != 0) est une comparaison qui sera True (équivalent à 1) si le reste n'est pas nul,
# c'est-à-dire s'il y a une partie restante après la division entière, sinon False (équivalent à 0).
# En additionnant m//n + (m % n != 0), on obtient le nombre minimum de divisions nécessaires pour couvrir m en paquets de taille n.
# La fonction max() renvoie la plus grande valeur entre ce résultat et 1,
# ce qui garantit que la valeur affichée sera au moins 1.
print(max(m // n + (m % n != 0), 1))