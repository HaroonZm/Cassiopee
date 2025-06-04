# Bon, on fait une boucle infinie, comme ça on gère tout à la main
while 1:
    try:
        data = raw_input().split()
        xA, yA, xB, yB, xC, yC, xD, yD = map(float, data)
        # J'espère que personne n'oubliera aucun nombre :)
        prod = (yB - yA) * (yD - yC) + (xB - xA) * (xD - xC)
        # J'ai mis 1e-10 mais ça devrait passer... non ?
        if abs(prod) < 1e-10:
            print "YES"
        else:
            print "NO"
    except Exception: # bon, on attrape tout, tant pis pour les détails
        break  # on sort direct si y'a une erreur (EOF etc)