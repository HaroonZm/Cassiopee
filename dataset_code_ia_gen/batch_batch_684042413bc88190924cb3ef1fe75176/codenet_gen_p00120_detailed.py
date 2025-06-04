import math
import sys
from itertools import permutations

def calc_width(order):
    """
    Calcule la largeur totale nécessaire pour placer les rouler cakes
    dans un certain ordre donné, en les plaçant côte à côte au sol sans 
    qu'ils ne se superposent verticalement.

    La distance horizontale minimale entre deux cercles de rayons r_i et r_j,
    posés au sol, est calculée par :
      d = sqrt((r_i + r_j)^2 - (r_i - r_j)^2) = 2 * sqrt(r_i * r_j)

    Args:
        order (list of int): Ordre des rayons des gâteaux.

    Returns:
        float: Largeur totale occupée dans cet ordre.
    """
    if not order:
        return 0

    # Position x du centre du premier gâteau
    positions = [order[0]]
    for i in range(1, len(order)):
        # distance horizontale minimale entre gâteau i-1 et i
        dist = 2 * math.sqrt(order[i-1] * order[i])
        positions.append(positions[-1] + dist)
    # La largeur totale est la position du dernier centre plus son rayon
    return positions[-1] + order[-1]

def main():
    # Lecture des données depuis l'entrée standard (plusieurs datasets)
    for line in sys.stdin:
        if not line.strip():
            continue
        data = list(map(int, line.strip().split()))
        # W = longueur de la boîte
        W = data[0]
        # rayons des gâteaux
        radii = data[1:]
        n = len(radii)

        # Si on place les gâteaux dans l'ordre donné, calcule largeur
        # On doit vérifier toutes les permutations car l'ordre peut réduire la longueur nécessaire
        can_fit = False
        # Étant donné n ≤ 12, nous ne testons que permutations uniques (il n'y a pas de changement d'ordre signifiant si radii sont égaux)
        # Mais on teste tous les ordres pour être sûr.
        # Pour optimisation, on peut tester permutations sans répétition si souhaité.
        # Vu contraintes (max 12), on peut faire ça sans soucis dans un temps raisonnable.
        for perm in permutations(radii):
            width = calc_width(perm)
            if width <= W + 1e-9:  # marge numérique
                can_fit = True
                break

        # Affichage résultat
        print("OK" if can_fit else "NA")

if __name__ == "__main__":
    main()