from math import sqrt  # On importe la fonction sqrt du module math pour calculer la racine carrée

# Définition de la fonction calc qui calcule les points d'intersection de deux cercles
def calc(x1, y1, rr1, x2, y2, rr2):
    # rr0 représente le carré de la distance entre les centres des deux cercles
    rr0 = (x2 - x1)**2 + (y2 - y1)**2
    # xd est la différence entre les abscisses des centres
    xd = x2 - x1
    # yd est la différence entre les ordonnées des centres
    yd = y2 - y1
    # cv est une variable temporaire calculée à partir de rr0, rr1 et rr2 et utilisée dans la résolution analytique
    cv = (rr0 + rr1 - rr2)
    
    # Si les cercles ne se coupent pas (condition pour qu'il n'y ait pas de points d'intersection réels)
    if 4*rr0*rr1 < cv**2:
        return tuple()  # Retourner un tuple vide signifie aucun point d'intersection
    
    # Si les cercles sont tangents (un seul point d'intersection)
    if 4*rr0*rr1 == cv**2:
        # Calculs pour trouver le point d'intersection tangent
        return ((x1 + cv*xd/(2.*rr0), y1 + cv*yd/(2.*rr0)),)
    
    # Si les cercles se coupent en deux points
    # sv est la racine carrée d'une expression positive indiquant deux intersections réelles
    sv = sqrt(4*rr0*rr1 - cv**2)
    # Retourne les coordonnées des deux points d'intersection
    return (
        (x1 + (cv*xd - sv*yd)/(2.*rr0), y1 + (cv*yd + sv*xd)/(2.*rr0)),
        (x1 + (cv*xd + sv*yd)/(2.*rr0), y1 + (cv*yd - sv*xd)/(2.*rr0)),
    )

# Définition de la fonction solve qui vérifie s'il existe un point commun dans tous les cercles de rayon réduit de mid
def solve(mid):
    ps = []  # Liste qui va contenir les points candidats qui peuvent être dans tous les cercles
    # Parcourir chaque cercle identifié par son indice i
    for i in xrange(n):
        x1, y1, l1 = P[i]  # On récupère les coordonnées du centre et le rayon du cercle i
        # Si le rayon du cercle i est inférieur à mid, impossible de placer un disque de rayon mid
        if l1 < mid:
            return 0  # Retourne 0 : impossible
        # On calcule rr1 qui est (l1^2 - mid^2), nouvelle puissance du cercle, c'est un rayon effectif carré réduit
        rr1 = l1**2 - mid**2
        # On va comparer ce cercle à tous les précédents (j < i)
        for j in xrange(i):
            x2, y2, l2 = P[j]  # On récupère les coordonnées et rayon du cercle j
            rr2 = l2**2 - mid**2  # Calcul de la puissance effective pour le cercle j
            # Si la distance entre les centres des deux cercles est supérieure à la somme de leurs nouveaux rayons, il n'y a pas d'intersection possible
            if (x1 - x2)**2 + (y1 - y2)**2 > (sqrt(rr1)+sqrt(rr2))**2:
                return 0  # Retourne 0, impossible
            # On ajoute les points d'intersection potentiels à la liste ps
            ps.extend(calc(x1, y1, rr1, x2, y2, rr2))
        # On ajoute également le centre du cercle courant comme point candidat de recouvrement
        ps.append((x1, y1))
    # Cas particulier où il n'y a qu'un seul cercle, il est toujours possible de placer un disque de rayon mid
    if n == 1:
        return 1
    # Pour chaque point candidat (px, py)
    for px, py in ps:
        # On vérifie si ce point est à une distance inférieure au rayon effectif pour tous les cercles
        # Il doit donc appartenir à tous les cercles réduits
        if all((px-x)**2 + (py-y)**2 < l**2 - mid**2 + 1e-8 for x, y, l in P):
            return 1  # Si trouvé, retourne 1 (possible)
    # Sinon, aucun point commun n'a été trouvé
    return 0

# Boucle principale pour lire les données de tous les cas de test
while 1:
    n = input()  # On lit le nombre de cercles pour ce cas de test
    if n == 0:
        break  # Si n vaut 0, il n'y a plus de cas de test à traiter, on quitte la boucle
    # On lit les données associées à chaque cercle
    # Pour chaque cercle, on lit trois entiers en entrée (coordonnées x, y et rayon l)
    P = [map(int, raw_input().split()) for i in xrange(n)]
    
    # On initialise notre recherche dichotomique entre left et right
    left = 1.  # Bord inférieur de la recherche (le rayon minimum possible)
    right = min(l for x, y, l in P)+1e-8  # Bord supérieur : le plus petit rayon parmi les cercles plus une petite marge d'erreur
    # On va effectuer une recherche binaire pour trouver la plus grande valeur de mid telle que solve(mid) soit vraie
    while left+1e-8 < right:
        mid = (left + right) / 2.  # On prend la moyenne de left et right comme nouvelle valeur candidate
        if solve(mid):  # Si possible de placer un disque de rayon mid
            left = mid  # On essaie plus grand en remontant la borne basse
        else:
            right = mid  # Sinon, on diminue la borne haute
    # Affichage du résultat formaté à 8 décimales
    print "%.08f" % left  # On affiche la plus grande valeur de mid trouvée, qui est la solution recherchée