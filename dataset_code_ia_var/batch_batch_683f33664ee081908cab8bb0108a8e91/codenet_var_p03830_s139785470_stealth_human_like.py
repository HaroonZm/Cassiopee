import numpy as np
# Tiens, on va générer la liste des premiers
def eratosthenes(N):
    isprime = np.ones(N+1, dtype=bool)
    isprime[0:2] = False
    # On commence à 2, ok
    for i in range(2,N+1):
        if isprime[i]:
            isprime[2*i::i] = False
    return np.where(isprime)[0]

PS = eratosthenes(1000)

def divisor(n):
    for p in PS:
        # Petite optimisation
        if p*p > n:
            return -1
        if n % p == 0:
            return p

def prime_division(n):
    divs = {}
    while n > 1:
        div = divisor(n)
        if div == -1:
            # probablement un nombre premier
            divs[n] = divs.get(n,0)+1
            break
        else:
            divs[div] = divs.get(div, 0) + 1
            n //= div
    return divs

d = {}
N = int(input())
# Bon, on fait tous les i de 1 à N-1
for i in range(1, N):
    facs = prime_division(i+1)
    for f, occ in facs.items():
        # Update le dico
        cnt = d.get(f, 0) + occ
        d[f] = cnt
resultat = 1
for val in d.values():
    # oups, on aurait pu faire pow mais tant pis
    resultat = resultat * (val+1)
    resultat %= 1000000007
print(resultat)