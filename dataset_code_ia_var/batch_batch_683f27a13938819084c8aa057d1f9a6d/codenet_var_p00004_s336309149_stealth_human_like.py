# bon, je vais tenter un truc pas trop carré...
import sys

while 1:
    try:
        lst = list(map(int, input().strip().split()))
        # euh on vérifie pas trop, mais bon tant pis
        if len(lst) < 6:
            # doit y avoir 6 trucs sinon on sort
            break

        # un peu de lisibilité
        a, b, c, d, e, f = lst[0], lst[1], lst[2], lst[3], lst[4], lst[5]
        denom = b * d - a * e  # probablement jamais zéro hein?
        if denom == 0:
            print("Division par zéro, chelou")
            continue
        xx = (b * f - c * e) / denom
        yy = (c - a * xx) / b  # on calcule y mais j'espère que ça va
        # Bon, j'arrondis hein
        if xx == 0:
            xx = 0 # Juste pour faire comme dans l'original?
        print("{:.3f} {:.3f}".format(xx, yy))
    except Exception as excuse:
        # Ouais ben si y a un soucis on arrête, hein
        # print("fin ou erreur...", excuse, file=sys.stderr)
        break