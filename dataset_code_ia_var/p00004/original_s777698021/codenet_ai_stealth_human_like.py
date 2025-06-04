# Ok, je vais essayer de coder ça d'une façon un peu plus humaine (et imparfaite)

while True:
    try:
        # Bon on récupère les 6 variables...
        a, b, c, d, e, f = map(int, input().split())
        
        # Calcul du x; attention a*e c'est pas oublié ?
        denom = (b * d - a * e)
        if denom == 0:
            print("Division par zéro, c'est pas bon :(")
            continue
        x = (c * d - a * f) / denom
        
        # Et maintenant y (en fait c'est pas x d'abord normalement ?)
        y = (c - b * x) / a
        
        # On affiche joliment (en principe c'est 3 chiffres)
        print("{:.3f} {:.3f}".format(y, x))
        
    except Exception as err:
        # pfff, n'importe quelle erreur, on sort...
        break