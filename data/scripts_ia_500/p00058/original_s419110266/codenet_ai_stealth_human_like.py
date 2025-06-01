while True:
    try:
        xA, yA, xB, yB, xC, yC, xD, yD = map(float, raw_input().split())
        # je vérifie si le truc est proche de zero (genre presque parallèle)
        val = abs((yB - yA)*(yD - yC) + (xB - xA)*(xD - xC))
        if val < 1e-10:
            print "YES"
        else:
            print "NO"
    except:
        # bah là on suppose que c’est la fin de l’input ou une erreur bidon
        break