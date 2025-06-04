import math
import sys
from math import gcd

def reduce_fraction(num, den):
    # Réduit la fraction num/den en divisant par leur PGCD.
    g = gcd(num, den)
    return num // g, den // g

def generate_Qn(n):
    # Génère l'ensemble Q_n des rationnels irréductibles a/b avec 1 <= a,b <= n
    # Utilise un set pour éviter les duplicata.
    Qn = set()
    for b in range(1, n+1):
        for a in range(1, n+1):
            g = gcd(a, b)
            if g == 1:
                Qn.add((a, b))
    return Qn

def rational_value(num, den):
    # Calcule la valeur décimale de la fraction num/den.
    return num / den

def main():
    # Lecture des lignes d'entrée jusqu'à la ligne 0 0
    for line in sys.stdin:
        line=line.strip()
        if line == "0 0":
            break
        p_str, n_str = line.split()
        p = int(p_str)
        n = int(n_str)
        sqrt_p = math.sqrt(p)

        # Générer toutes les fractions irréductibles à dénominateur et numérateur <= n
        # Nous chercherons deux fractions u/v et x/y dans Q_n telles que u/v < sqrt_p < x/y
        # et qu'aucune autre fraction de Q_n ne soit dans cet intervalle.
        Qn = []
        # Plutôt que générer puis trier et chercher, on peut générer et garder celles proches de sqrt_p
        # mais ici on suit la méthode complète.
        for b in range(1, n+1):
            # Pour chaque dénominateur, on cherche a approcher sqrt_p*b
            # Les candidats ne peuvent être que les entiers proches.
            # On calcule la partie entière de sqrt_p * b comme pivot
            a_floor = int(math.floor(sqrt_p * b))
            # Tester a_floor et a_floor+1 si <= n
            for a in [a_floor, a_floor+1]:
                if 1 <= a <= n:
                    if gcd(a, b) == 1:
                        Qn.append( (a, b) )

        # Trier les fractions par valeur décimale croissante
        Qn.sort(key=lambda frac: frac[0]/frac[1])

        # Trouver la première paire (u/v, x/y) dans Qn telle que u/v < sqrt_p < x/y
        # et que x/y est le successeur de u/v dans la liste (donc aucun élément entre eux)
        # On parcours la liste triée et pour chaque paire consécutive on regarde si sqrt_p est entre eux
        u, v = 0, 1
        x, y = 0, 1
        for i in range(len(Qn)-1):
            a1, b1 = Qn[i]
            a2, b2 = Qn[i+1]
            val1 = a1/b1
            val2 = a2/b2
            if val1 < sqrt_p < val2:
                # condition trouvée
                u, v = a1, b1
                x, y = a2, b2
                break

        # Sortie au format demandé : x/y u/v avec x/y > u/v
        # fraction irréductible déjà garantie par sélection
        print(f"{x}/{y} {u}/{v}")

if __name__ == "__main__":
    main()