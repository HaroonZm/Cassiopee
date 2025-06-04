# Débute une boucle while infinie. Ceci signifie que le code à l'intérieur sera répété sans fin,
# sauf si une commande 'break' ou une autre instruction d'arrêt est exécutée à l'intérieur de la boucle.
while 1:
    # Demande une entrée utilisateur sous forme de chaîne de caractères.
    # split() découpe la chaîne en une liste de sous-chaînes où il y a des espaces.
    # map(int, ...) transforme chaque chaîne obtenue en entier.
    # Les deux entiers extraits sont stockés dans n et m respectivement.
    n, m = map(int, input().split())

    # Vérifie si la valeur de n est exactement égale à 0.
    # Si c'est le cas, exécute l'instruction 'break' qui stoppe la boucle 'while' en cours.
    if n == 0:
        break

    # Demande une nouvelle entrée utilisateur, supposée être une série de nombres séparés par des espaces.
    # split() découpe cette nouvelle entrée en liste de chaînes.
    # map(int, ...) transforme chaque chaîne en un entier.
    # list(...) convertit l'objet map (un itérable) en une liste d'entiers et l'assigne à 'a'.
    a = list(map(int, input().split()))

    # Initialise la variable entière 'c' à 0.
    # Cette variable servira à accumuler un résultat tout au long de la boucle suivante.
    c = 0

    # Lance une boucle for sur la plage d'entiers de 0 à n-1 inclus.
    # range(n) crée une séquence d'entiers de 0 à n-1.
    # À chaque itération, 'i' prend la valeur de l'indice courant.
    for i in range(n):
        # Pour chaque élément, on exécute l'opération suivante :
        # calcule la division entière m//n, ce qui donne combien de fois n rentre dans m sans reste.
        # min(m//n, a[i]) renvoie la valeur la plus petite entre m//n et a[i].
        # Cette valeur est alors ajoutée au total accumulé 'c'.
        c += min(m // n, a[i])

    # Affiche la valeur totale accumulée 'c' à la fin de la boucle for.
    print(c)