from math import gcd  # Importe la fonction gcd (greatest common divisor = plus grand commun diviseur) du module math

s = input()  # Demande à l'utilisateur d'entrer une chaîne de caractères et la stocke dans la variable 's'
x, y = s.split(".")  # Sépare la chaîne d'entrée en deux parties autour du point (séparateur décimal) ; x = partie entière, y = partie décimale

# Vérifie si la chaîne contient un caractère '(' signifiant la présence d'une partie périodique dans le décimal
if "(" in s:
    # Trouve l'index où commence la partie périodique dans la partie décimale (c'est-à-dire la position du '(')
    da = y.index("(")
    # Trouve l'index où se termine la partie périodique dans la partie décimale (position du ')' - 1, car les index commencent à 0)
    db = y.index(")") - 1
    # Sépare la partie décimale en deux : avant la parenthèse et après
    ya, b = y.split("(")  # 'ya' contient la partie avant la parenthèse ; 'b' contient la partie périodique suivie de ')'
    # Calcule la longueur de la période (nombre de chiffres dans la partie périodique)
    lb = len(b) - 1  # On enlève 1 pour ne pas compter la parenthèse fermante ')'
    # Concatène la partie entière ('x') et la partie avant la parenthèse ('ya') puis convertit le résultat en entier
    a = int(x + ya)
    # Prend la partie périodique (sans la parenthèse fermante) et la convertit en entier
    b = int(b[:-1])
    # Calcule le numérateur selon la formule des nombres décimaux périodiques
    # (a * (10^{db} - 10^{db-lb})) permet
    # d'obtenir la partie jusqu'au début de la période multipliée par la différence de puissances de 10
    # + b * 10^{da} ajoute la partie périodique correctement positionnée
    deco = a * (10 ** db - 10 ** (db - lb)) + b * 10 ** da
    # Calcule le dénominateur selon la même logique
    # 10^{da} * (10^{db} - 10^{db-lb}) correspond à la positionnée correcte des chiffres périodiques
    nume = 10 ** da * (10 ** db - 10 ** (db - lb))
    # Trouve le plus grand commun diviseur de 'deco' et 'nume' afin de réduire la fraction au plus simple
    div = gcd(deco, nume)
    # Affiche le résultat final en simplifiant la fraction avec le séparateur '/'
    # (l'opérateur '//' effectue une division entière, c'est-à-dire sans reste)
    print(deco // div, nume // div, sep="/")
else:
    # Si la chaîne d'entrée ne contient pas de partie périodique (c'est-à-dire pas de '(')
    # Calcule la longueur de la partie décimale
    da = len(y)
    # Concatène la partie entière et la partie décimale et la convertit en entier pour faire le numérateur
    a = int(x + y)
    # Puisque le nombre n'a pas de période, le numérateur est juste la concaténation de la partie entière et décimale
    deco = a
    # Le dénominateur est 10 à la puissance du nombre de chiffres après la virgule (pour convertir le décimal en fraction)
    nume = 10 ** da
    # Trouve le plus grand commun diviseur des deux pour simplifier la fraction
    div = gcd(deco, nume)
    # Affiche la fraction simplifiée sous la forme numérateur/dénominateur
    print(deco // div, nume // div, sep="/")