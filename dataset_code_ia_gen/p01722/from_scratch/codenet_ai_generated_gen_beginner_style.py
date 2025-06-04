n = int(input())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def tetration_two(n):
    if n == 0:
        return 1
    else:
        # Calculer 2^(2^(...)) n fois, mais de façon naïve en limitant à un nombre petit
        # Comme les nombres deviennent énormes, on ne peut pas calculer directement
        # Pour ce code simple, on retourne 2^(tetration_two(n-1))
        # Ici on ne pourra pas exécuter pour grands n, mais c'est un code simple
        return 2 ** tetration_two(n-1)

if n == 0:
    p = 2
else:
    # calculer 2^^n (tetration de 2 n fois)
    t = tetration_two(n)
    # trouver le plus petit nombre premier > t
    p = t + 1
    while not is_prime(p):
        p += 1

# p est un nombre premier, p >= 2

# Le nombre à diviser est un nombre avec p-1 chiffres tous égaux à 1
# C'est (10^(p-1) - 1)/9

# On veut ((10^(p-1) - 1)/9) mod p
# Comme p est premier différent de 3 (car p>t >=4 quand n>0), 9 et p sont premiers entre eux

# Calculons 10^(p-1) mod p avec pow
mod_pow = pow(10, p - 1, p)
# val mod p
val = (mod_pow - 1) * pow(9, p - 2, p) % p  # inverse de 9 mod p par Fermat

print(val)