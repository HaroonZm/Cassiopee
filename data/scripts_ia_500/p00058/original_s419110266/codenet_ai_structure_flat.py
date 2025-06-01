while True:
    try:
        xA, yA, xB, yB, xC, yC, xD, yD = map(float, raw_input().split())
        valeur = abs((yB - yA) * (yD - yC) + (xB - xA) * (xD - xC))
        if valeur < 1.e-10:
            print "YES"
        else:
            print "NO"
    except:
        break