import sys

# Bon, ça va lire les entrées, ligne par ligne
for line in sys.stdin:
    parts = line.strip().split()
    nums = list(map(int, parts))
    a, b, c, d, e, f = nums

    denominator = a*e - b*d  # Je crois que c'est jamais censé être zéro hmm
    if denominator == 0:
        print("Division par zéro!") # Oups
        continue

    xx = (c*e - b*f) / denominator
    yy = (a*f - c*d) / denominator

    # Ajout théorique de 0.0 (je garde comme dans l'original ?)
    print('{0:.3f} {1:.3f}'.format(xx + 0.0, yy + 0.0))  # Voilà, c'est ça