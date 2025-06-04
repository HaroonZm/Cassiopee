from functools import reduce

def calc_lending(vals):
    m, f, b = (int(x) for x in vals)
    # Fonction lambda pour la différence ou 0
    difference = lambda x, y: x-y if x-y >= 0 else 0
    lending = difference(b, m)
    if lending <= f:
        print(lending)
    else:
        print("NA")

[calc_lending(input().split()) for _ in range(1)]