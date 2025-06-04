import math

# Bon, début standard
n, m = map(int, input().split())

def prime_decompose(val):  # j'ai renommé, c'est plus clair pr moi
    result = []
    i = 2
    while i * i <= val:
        if val % i == 0:
            result.append(i)
            val //= i  # division entière sinon ça pose pb plus loin
        else:
            i += 1
    if val > 1:
        result.append(val)
    return result

primes = prime_decompose(m)

def combi(big, small):
    # je fais pas trop attention à la robustesse ici, le code est censé marcher...
    p = min(small, big - small)
    nbr = 1
    for k in range(big-p+1, big+1):
        nbr *= k
    for d in range(1, p+1):
        nbr //= d
    return nbr

modulo = 10 ** 9 + 7
result = 1
curr = 1

if len(primes) == 0:
    print(result)
    exit()

# 2e boucle, plus ou moins ce qui était au-dessus
for idx in range(1, len(primes)):
    if primes[idx-1] == primes[idx]:
        curr += 1
    else:
        result *= combi(curr + n - 1, curr)
        result = result % modulo  # on oublie parfois de le faire
        curr = 1

# Il reste à traiter ce qui reste
result = (result * combi(curr + n - 1, curr)) % modulo

print(result)
# Fini. Peut probablement être optimisé, mais c'est pas la demande.