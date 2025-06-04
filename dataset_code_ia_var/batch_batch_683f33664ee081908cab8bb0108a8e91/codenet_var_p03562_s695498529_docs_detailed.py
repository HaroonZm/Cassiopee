import sys
from functools import reduce

# Lis le flux d'entrée en mode binaire pour performance sur concours
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 998244353  # Modulo imposé par le problème

def gcd(a, b):
    """Calcule le PGCD (gcd) de deux polynômes binaires
    sur F_2, en considérant leur représentation entière.
    On utilise l'algorithme Xor-Shift adapté au cas binaire.
    Arguments:
        a (int): premier polynôme (entier correspondant à la chaîne binaire)
        b (int): second polynôme (idem)
    Returns:
        int: Le PGCD de a et b sur F_2
    """
    if a < b:
        a, b = b, a
    while b:
        LA = a.bit_length()
        LB = b.bit_length()
        # On supprime le monôme de plus haut degré de a
        a ^= b << (LA - LB)
        if a < b:
            a, b = b, a
    return a

def main():
    """Point d'entrée principal. Lit les entrées, calcule le PGCD,
    puis compte le nombre de multiples de g (obtenu par PGCD)
    inférieurs ou égaux à X.
    Affiche ensuite le nombre selon le modulo imposé.
    """
    # Lecture de la première ligne : n inutilisé, x comme nombre binaire
    X = int(readline().split()[1], 2)

    # Lecture de tous les polynômes (en représentation binaire) à traiter
    A = [int(x, 2) for x in readlines()]

    # Calcul du PGCD de toute la suite
    g = reduce(gcd, A)

    # Pour compter le nombre de multiples du polynôme g qui sont inférieurs ou égaux à X
    # On s'appuie sur la structure particulière des polynômes sur F_2
    LX = X.bit_length()     # degré de X (plus haut monôme activé)
    Lg = g.bit_length()     # degré de g
    answer = X >> (Lg - 1)  # quotient : nombre d'offsets de g qui rentrent dans X en ignorant le reste

    # Cette boucle simule la "division polynomiale" de X par g, pour compter le cas frontière
    prod = 0         # Produit partiel du multiple de g
    x = X            # Variable mutable pour X
    Lx = LX          # Bit length courant de x

    while Lx >= Lg:
        prod ^= g << (Lx - Lg)   # Soustraction du monôme principal dans la division polynomiale
        x ^= g << (Lx - Lg)      # Mise à jour de x comme dans l'algorithme classique de division
        Lx = x.bit_length()      # Mise à jour du degré du polynôme restant

    # Si le dernier multiple est inférieur/égal à X, on l'inclut
    if prod <= X:
        answer += 1

    answer %= MOD
    print(answer)

# Appel du point d'entrée principal
if __name__ == "__main__":
    main()