import math

# Fonction pour calculer l'aire de l'intersection entre le grand rectangle (donut) et le petit rectangle mangé le 1er jour
# Le donut est centré en (0,0) avec largeur W et hauteur H
# Le petit rectangle est centré en (x, y) avec largeur w et hauteur h
def eaten_area(W, H, w, h, x, y):
    # Coordonnées du grand rectangle
    left_big = -W/2
    right_big = W/2
    top_big = H/2
    bottom_big = -H/2

    # Coordonnées du petit rectangle mangé le 1er jour
    left_small = x - w/2
    right_small = x + w/2
    top_small = y + h/2
    bottom_small = y - h/2

    # Calcul de la zone d'intersection
    left_inter = max(left_big, left_small)
    right_inter = min(right_big, right_small)
    top_inter = min(top_big, top_small)
    bottom_inter = max(bottom_big, bottom_small)

    # Si pas d'intersection, aire = 0
    if right_inter <= left_inter or top_inter <= bottom_inter:
        return 0.0

    return (right_inter - left_inter) * (top_inter - bottom_inter)

# Fonction qui calcule l'aire relative du donut d'un côté de la droite d'équation y = slope * x
# On cherche a equilibrer l'aire restante du donut après avoir enlevé la partie mangée le 1er jour entre les deux côtés de la droite
def area_side(W, H, eaten, slope, side):
    # Le donut est un rectangle centré en (0,0)
    # On va approximer l'aire du donut d'un côté de la droite y = slope * x
    # Puis on enlève l'aire mangée du côté correspondant

    # On calcule l'aire totale du donut après retrait de la partie mangée
    total_area = W * H - eaten

    # Pour trouver l'aire d'un côté, on calcule l'aire du grand rectangle côté "side" selon la droite y = slope * x,
    # puis on enlève l'aire de la partie mangée de ce même côté.

    # Le donut est un rectangle centré, la droite passe par (0,0)
    # L'aire du donut d'un côté de la droite peut s'obtenir en intégrant la partie du rectangle où (y - slope*x)*side >= 0
    # On fait l'intégration sur x dans [-W/2, W/2]

    W_half = W/2
    H_half = H/2

    # On intégrera la hauteur limitée par le rectangle et la droite
    # Pour chaque x, le point sur la droite est y = slope * x
    # La zone d'un côté est limitée en y entre bottom_big = -H/2 et top_big = H/2, mais on ne prend que la partie où (y - slope*x)*side >= 0

    # On distingue 2 cas pour chaque x :
    # - si slope*x >= 0 et side=1, la zone est entre y = slope*x et y = top_big
    # - si slope*x < 0 et side=1, la zone est entre y = bottom_big et y = slope*x
    # idem inversé pour side = -1

    # Pour plus de simplicité, on définit une fonction qui donne l'aire d'un côté:

    # On utilise une fonction intégrale analytique pour éviter approximation numérique

    def f(x):
        y_line = slope * x
        if side == 1:
            if y_line >= 0:
                # Aire en y = [y_line, top_big]
                return max(0, top_big - y_line)
            else:
                # Aire en y = [bottom_big, y_line]
                return max(0, y_line - bottom_big)
        else:  # side == -1
            if y_line >= 0:
                # Aire en y = [bottom_big, y_line]
                return max(0, y_line - bottom_big)
            else:
                # Aire en y = [y_line, top_big]
                return max(0, top_big - y_line)

    # Calcul intégral sur x in [-W/2, W/2]
    # Aire côté = integrate f(x) dx de -W/2 à W/2

    # On calcule de façon analytique l'intégrale de f(x) dx :

    # Cas side = 1:
    # Si y_line >= 0 => f(x) = top_big - slope*x
    # Sinon f(x) = y_line - bottom_big = slope*x - bottom_big

    # On sépare l'intégrale aux x0 où y_line = 0 => slope * x0 = 0 => x0 = 0
    # Donc intégrer de -W/2 à 0 et de 0 à W/2 en deux parties

    # side==1
    if side == 1:
        # intégrale de -W/2 à 0 : f(x) = slope*x - bottom_big
        integral1 = (slope * (0**2 / 2 - (-W_half)**2 / 2) - bottom_big * (0 - (-W_half)))
        # intégrale de 0 à W/2 : f(x) = top_big - slope*x
        integral2 = (top_big * (W_half - 0) - slope * (W_half**2 / 2 - 0))
        # somme
        area = integral1 + integral2

    else:
        # side == -1
        # intégrale de -W/2 à 0 : f(x) = top_big - slope*x
        integral1 = (top_big * (0 - (-W_half)) - slope * (0 - (-W_half)**2 / 2))
        # intégrale de 0 à W/2 : f(x) = slope*x - bottom_big
        integral2 = (slope * (W_half**2 / 2 - 0) - bottom_big * (W_half - 0))
        area = integral1 + integral2

    # area est donc l'aire du donut d'un côté sur toute la surface sans tenir compte du rectangle mangé.

    # On doit enlever l'aire mangée d'un côté.
    # L'aire mangée est un rectangle centré en (x,y) avec largeur w et hauteur h.
    # On calcule l'aire de la partie mangée d'un côté de la droite.

    # Méthode: on découpe le rectangle mangé en 4 coins et on calcule la partie à droite/gauche de la droite

    # On approxime la partie mangée de droite = aire du rectangle mangé * fraction de points où (Y - slope*X)*side >= 0

    # Les quatre coins du petit rectangle mangé:
    W_small_half = w / 2
    H_small_half = h / 2

    corners = [
        (x - W_small_half, y - H_small_half),
        (x - W_small_half, y + H_small_half),
        (x + W_small_half, y - H_small_half),
        (x + W_small_half, y + H_small_half),
    ]

    # On compte combien de coins sont du côté considéré
    count_side = 0
    for cx, cy in corners:
        val = (cy - slope * cx) * side
        if val >= 0:
            count_side += 1

    # Fraction de coins du côté
    fraction_corners = count_side / 4

    # Comme le rectangle est convexe et la droite passant par (0,0), cette fraction approxime bien la fraction de la surface du rectangle de ce côté
    # Puisque la droite coupe le plan, on peut approximer par la fraction des coins pour trouver la fraction de l'aire

    eaten_side = eaten * fraction_corners

    # Aire du côté corrigée
    side_area = area - eaten_side

    return side_area

def main():
    # Lecture des données
    W, H, w, h, x, y = map(int, input().split())

    # Aire mangée le 1er jour
    eaten = eaten_area(W, H, w, h, x, y)

    # Aire totale du donut avant removal
    total_area = W * H

    # Sur le donut restant, on veut diviser en 2 parts égales en traçant une droite passant par (0,0)
    # y = slope * x

    # On cherche slope tel que:
    # area_side(W,H,eaten,slope,1) = area_side(W,H,eaten,slope,-1)
    # --> aire du côté 1 égale aire côté -1
    # soit area_side(W,H,eaten,slope,1) = total_area_after_eaten / 2

    total_area_after_eaten = total_area - eaten

    # On utilise une méthode de dichotomie sur slope entre lower et upper bounds pour trouver la racine

    # Intervalle initial, on teste dans [-1e6, 1e6], on double si besoin
    low = -1e6
    high = 1e6

    # Fonction qui renvoie différence = area_side(slope,1) - half_total_area
    def f(slope):
        return area_side(W, H, eaten, slope, 1) - total_area_after_eaten / 2

    # On cherche un intervalle [low, high] tel que f(low)*f(high) <= 0
    # On ajuste high si besoin
    if f(low) > 0:
        # On veut f(low) < 0 < f(high)
        while f(low) > 0:
            low /= 2
    if f(high) < 0:
        while f(high) < 0:
            high *= 2

    # Recherche dichotomique
    for _ in range(100):
        mid = (low + high) / 2
        val = f(mid)
        if abs(val) < 1e-14:
            break
        if val > 0:
            high = mid
        else:
            low = mid

    slope = (low + high) / 2

    # Affichage avec la précision demandée
    print(slope)


if __name__ == "__main__":
    main()