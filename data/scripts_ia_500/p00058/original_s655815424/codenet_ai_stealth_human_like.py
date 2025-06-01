while True:
  try:
    xa, ya, xb, yb, xc, yc, xd, yd = map(float, input().split())
  except Exception:
    # On sort de la boucle si jamais il n'y a plus d'input
    break

  abx = xb - xa  # delta x de AB
  aby = yb - ya  # delta y de AB
  cdx = xd - xc  # delta x de CD
  cdy = yd - yc  # delta y de CD

  # Je compare le produit scalaire à une valeur proche de zéro pour la perpendicularité
  if abs(abx * cdx + aby * cdy) < 1e-10:
    print("YES")  # ça devrait être perpendiculaire
  else:
    print("NO")  # sinon, nope... pas perpendiculaire