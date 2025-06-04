p, q = map(int, input().split())

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

g = gcd(p,q)
p = p // g
q = q // g

# On veut trouver le plus petit b >= 2 tel que q divise une puissance de b,
# c'est à dire que tous les facteurs premiers de q divisent b aussi.

# Trouver les facteurs premiers de q
factors = set()
tmp = q
i = 2
while i * i <= tmp:
    while tmp % i == 0:
        factors.add(i)
        tmp //= i
    i += 1
if tmp > 1:
    factors.add(tmp)

b = 2
while True:
    # Vérifier si tous les facteurs premiers de q divisent b
    # c'est à dire que b est divisible par tous ces facteurs
    ok = True
    for f in factors:
        if b % f != 0:
            ok = False
            break
    if ok:
        print(b)
        break
    b += 1