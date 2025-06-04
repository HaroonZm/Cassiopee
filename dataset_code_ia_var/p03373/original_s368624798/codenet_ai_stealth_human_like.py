# Ok alors là je fais rentrer les variables a, b, c, x, y d'un coup
a, b, c, x, y = list(map(int, input().split()))

# Peut-être qu'il faudrait vérifier les entrées? On verra ça plus tard...

# D'abord je calcule le prix sans combo, juste pour avoir un point de comparaison
prix_min = a * x + b * y

# Bon, maintenant je vais essayer d'utiliser un max de combos c (ça dépend qui en a le plus)
if x > y:
    # x étant plus grand, c'est sur celui-là qu'on y va
    for i in range(x+1):  # Je crois que +1, sinon on rate des cas
        truc_b = y - i
        if truc_b < 0:
            truc_b = 0  # sinon ça fait n'importe quoi
        prix = a * (x - i) + b * truc_b + c * 2 * i
        # si jamais c'est moins cher, on prends
        if prix < prix_min:
            prix_min = prix
else:
    # même logique mais on change les rôles
    for k in range(y+1):  # là pareil, jusqu'à y inclus
        truc_a = x - k
        if truc_a < 0:
            truc_a = 0  # on ne veut pas de valeurs négatives, hein
        cout = a * truc_a + b * (y - k) + c * 2 * k
        if cout < prix_min:
            prix_min = cout  # on update si besoin

print(prix_min)
# ouf, normalement ça fonctionne, à tester quand même...