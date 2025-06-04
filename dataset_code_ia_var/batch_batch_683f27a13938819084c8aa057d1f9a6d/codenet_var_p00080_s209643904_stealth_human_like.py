import math
while True:
    # On récupère une entrée utilisateur (je suppose que c'est un entier ?)
    q = int(input())
    if q == -1:
        # Si c'est -1, bah faut arrêter la boucle
        break
    # Un premier essai pour la racine cubique, pourquoi pas q/2
    x = q / 2
    while True:
        # On compare la précision, mais je crois que c'est peut-être trop strict ?
        if abs((x ** 3) - q) < 0.00001 * q:
            break  # On est bons, je pense
        # La formule de Newton pour le cube, pas facile à retenir celle-là
        x = x - ((x ** 3) - q) / (3 * x ** 2)
        # Pas de vérification de x==0, mais bon, normalement ça va
    # On affiche avec 6 décimales parce que c'est joli
    print("{:.6f}".format(x))

# Fin du script, j'espère que ça marche pour vous !