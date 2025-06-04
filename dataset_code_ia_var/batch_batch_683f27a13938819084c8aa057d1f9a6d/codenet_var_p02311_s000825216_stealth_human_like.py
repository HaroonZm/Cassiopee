# Bon bah, j'ai essayé de rendre ça plus... humain.
import math

# Alors on lit les données, je préfère demander comme ça,
# il faut juste entrer trois nombres séparés par des espaces, genre "1 2 3"
x1, y1, r1 = map(int, raw_input().split())
x2, y2, r2 = map(int, raw_input().split())

def tirs_de_cercles(xx1, yy1, rr1, xx2, yy2, rr2):
    res = []
    dx = xx2 - xx1
    dy = yy2 - yy1
    # distance au carré entre les centres
    dist2 = dx*dx + dy*dy
    # la racine alors
    dist = math.sqrt(dist2)
    # J'avoue, les conditions suivantes demandent de bien suivre...
    # Premier test avec différence de rayons
    if (rr1 - rr2)*(rr1 - rr2) <= dist2:
        truc = rr1 - rr2
        if dist2 == (rr1 - rr2)*(rr1 - rr2):  # Cas tangent?
            res.append((xx1 + rr1*truc*dx/dist2, yy1 + rr1*truc*dy/dist2))
        else:
            bidule = math.sqrt(dist2 - truc*truc)
            # deux points trouvés normalement, possible erreurs d'arrondis...
            res.append((xx1 + rr1*(truc*dx - bidule*dy)/dist2, yy1 + rr1*(bidule*dx + truc*dy)/dist2))
            res.append((xx1 + rr1*(truc*dx + bidule*dy)/dist2, yy1 + rr1*(-bidule*dx + truc*dy)/dist2))
    # Deuxième test, somme des rayons
    if (rr1 + rr2)**2 <= dist2:
        autre = rr1 + rr2
        if dist2 == (rr1 + rr2)*(rr1 + rr2):
            res.append((xx1 + rr1*autre*dx/dist2, yy1 + rr1*autre*dy/dist2))
        else:
            trucmuche = math.sqrt(dist2 - autre*autre)
            res.append((xx1 + rr1*(autre*dx - trucmuche*dy)/dist2, yy1 + rr1*(trucmuche*dx + autre*dy)/dist2))
            res.append((xx1 + rr1*(autre*dx + trucmuche*dy)/dist2, yy1 + rr1*(-trucmuche*dx + autre*dy)/dist2))
    # Bon, je retourne ce que j'ai trouvé, tant pis si vide
    return res

soluce = tirs_de_cercles(x1, y1, r1, x2, y2, r2)
soluce.sort()  # J'ai mis le sort là, pas très utile s'il y a peu de points mais tant pis

if soluce:
    for point in soluce:
        # Oula, les formattages, faut pas trop en abuser, mais allons-y.
        print "%.8f %.8f" % point
# Et voilà. Peut-être quelques imprécisions avec les floats... à vérifier.