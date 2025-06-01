while True:
    try:
        line = input()
        if not line:
            break
        xA, yA, xB, yB, xC, yC, xD, yD = map(float, line.split())
        # vecteur AB
        ABx = xB - xA
        ABy = yB - yA
        # vecteur CD
        CDx = xD - xC
        CDy = yD - yC
        # produit scalaire
        dot = ABx * CDx + ABy * CDy
        # si produit scalaire proche de 0, les droites sont orthogonales
        if abs(dot) < 1e-10:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break