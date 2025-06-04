import sys
import math

def cubic_roots_sign_count(a, b, c, d):
    # Cette fonction calcule le nombre de racines réelles positives et négatives
    # d'une équation cubique : a*x^3 + b*x^2 + c*x + d = 0.

    # Nous allons utiliser la méthode classique de résolution des équations cubiques
    # basée sur la réduction de l'équation en une forme "déprimée" y^3 + p y + q = 0,
    # puis analyser le discriminant pour déterminer le nombre et la nature des racines.

    # Ensuite, on calcule les racines réelles exactes (en tenant compte des racines multiples)
    # et compte celles strictement positives et strictement négatives.

    # 1. Transformation en équation déprimée via un changement de variable :
    # x = y - b/(3a) pour supprimer le terme en y^2.
    p = (3*a*c - b**2) / (3 * a**2)
    q = (2*b**3 - 9*a*b*c + 27*(a**2)*d) / (27 * a**3)

    # Calcul du discriminant de l'équation déprimée y^3 + p y + q = 0
    discriminant = (q**2)/4 + (p**3)/27

    roots = []

    if abs(discriminant) < 1e-14:
        # Discriminant nul, racines réelles multiples
        if abs(q) < 1e-14:
            # Triple racine réelle
            y = 0
            roots = [y, y, y]
        else:
            # Une racine simple et une double racine
            u = (-q/2)**(1/3) if q <= 0 else - (q/2)**(1/3)
            y1 = 2*u
            y2 = -u
            roots = [y1, y2, y2]
    elif discriminant > 0:
        # Une racine réelle et deux racines complexes
        sqrt_disc = math.sqrt(discriminant)
        A = (-q/2) + sqrt_disc
        B = (-q/2) - sqrt_disc
        # Calcul des racines cubiques réelles de A et B
        A_cubrt = A**(1/3) if A >= 0 else -(-A)**(1/3)
        B_cubrt = B**(1/3) if B >= 0 else -(-B)**(1/3)
        y1 = A_cubrt + B_cubrt
        roots = [y1] # les deux autres sont complexes, ignorés
    else:
        # Trois racines réelles distinctes
        # paramètre pour cosinus
        r = math.sqrt(-p**3 / 27)
        phi = math.acos(-q/(2 * r))
        t = 2 * (-p/3)**0.5
        y1 = t * math.cos(phi / 3)
        y2 = t * math.cos((phi + 2*math.pi) / 3)
        y3 = t * math.cos((phi + 4*math.pi) / 3)
        roots = [y1, y2, y3]

    # Remise dans la variable x originale
    roots = [y - b/(3*a) for y in roots]

    # Comptage des racines strictement positives et négatives, en comptant les racines multiples
    pos_count = sum(root > 0 for root in roots)
    neg_count = sum(root < 0 for root in roots)

    return pos_count, neg_count

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    t = int(input_lines[0])
    for i in range(1, t+1):
        a,b,c,d = map(int, input_lines[i].split())
        pos, neg = cubic_roots_sign_count(a,b,c,d)
        print(pos, neg)

if __name__ == "__main__":
    main()