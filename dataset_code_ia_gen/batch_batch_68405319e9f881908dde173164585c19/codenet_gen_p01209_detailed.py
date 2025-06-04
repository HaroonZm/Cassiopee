import sys
import math

def prime_factors(n):
    """
    Décompose un entier n en ses facteurs premiers.
    Renvoie un dictionnaire {facteur_premier: exposant}.
    """
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2  # après 2, on teste que les impairs
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def count_factor_in_factorial(m, p):
    """
    Calcule le nombre d'occurrences du facteur premier p dans m! (factorielle de m).
    Utilise la formule : sum_{k=1}^∞ floor(m / p^k)
    """
    count = 0
    power = p
    while power <= m:
        count += m // power
        power *= p
    return count

def baseN_to_decimal(s, base):
    """
    Convertit une chaîne s représentant un nombre en base 'base' en entier décimal.
    Ex: baseN_to_decimal("A", 16) -> 10
    """
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = 0
    for ch in s:
        val = val * base + digits.index(ch)
    return val

def trailing_zeros_factorial_in_base(n, m_str):
    """
    Calcule le nombre de zéros à la fin de M! en base N.
    Méthode:
    1) Décomposer la base N en facteurs premiers : N = p1^e1 * p2^e2 * ...
    2) Pour chaque facteur premier p_i, compter combien de fois p_i apparaît dans M!.
    3) Pour chaque p_i, le nombre de zéros est floor(v_p(M!) / e_i).
    4) Le nombre total de zéros est le minimum sur tous les p_i.
    """
    # Convertir M de la base N en décimal
    m = baseN_to_decimal(m_str, n)
    # Décomposer N en facteurs premiers avec exposants
    factorization = prime_factors(n)
    # Pour chaque facteur p de N, compter combien de fois p divise M!
    zeros_counts = []
    for p, e in factorization.items():
        vp = count_factor_in_factorial(m, p)
        zeros_counts.append(vp // e)
    # La quantité de zéro dans la base N est déterminée par le facteur limitant
    return min(zeros_counts)

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "0 0":
            break
        n, m_str = line.split()
        n = int(n)
        # calcul et affichage du résultat
        print(trailing_zeros_factorial_in_base(n, m_str))

if __name__ == "__main__":
    main()