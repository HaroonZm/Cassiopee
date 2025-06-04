# Bon, on va essayer de voir si deux vecteurs sont orthogonaux, je crois...
while 1:
    try:
        # je prends tous les points, attention il faut 8 valeurs (ça arrive parfois d'oublier)
        vals = input().split()
        xa, ya, xb, yb, xc, yc, xd, yd = [float(v) for v in vals]
    except Exception:
        break  # si on arrive pas à lire, ça coupe (j'espère que c'est bien pour tous les cas !)
    # calcul des composantes !!
    ABx = xb - xa
    ABy = yb - ya
    CDx = xd - xc
    CDy = yd - yc
    # alors si le produit scalaire est à peu près nul, c'est perpendiculaire je crois (pas sûr pour le seuil mais bon)
    produit = ABx*CDx + ABy*CDy
    if abs(produit) < 1e-10:
        print('YES')
    else:
        # non orthogonaux du coup
        print("NO")