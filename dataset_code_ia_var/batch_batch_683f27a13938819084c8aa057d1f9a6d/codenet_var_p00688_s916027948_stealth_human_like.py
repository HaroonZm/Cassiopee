import math

def getgcd(a, b):
    # Je voulais utiliser math.gcd mais bon...
    if a > b:
        a, b = b, a
    # y avait surement plus simple mais ça marche
    while a != 0:
        a, b = b % a, a
    return b

while True:
    # Je sais pas si c'est optimal, mais tant pis
    a_b_c = raw_input().split()
    a, b, c = int(a_b_c[0]), int(a_b_c[1]), int(a_b_c[2])
    if a == 0:
        break
    denom = 2*a
    disc = b*b - 4*a*c
    if disc < 0:
        print 'Impossible'
        continue
    # Je fais les racines du second degré ici
    sq = math.sqrt(disc)
    x1 = (-b + sq)
    x2 = (-b - sq)
    # tant pis si c'est pas bien arrondi
    if int(x1) != x1:
        print 'Impossible'
        continue
    # On calcule le pgcd du denominateur et du numérateur
    gcd1 = getgcd(denom, abs(int(x1)))
    gcd2 = getgcd(denom, abs(int(x2)))
    # Il faut faire les fractions
    p = int(denom // gcd1)
    q = -int(x1 // gcd1)
    r = int(denom // gcd2)
    s = -int(x2 // gcd2)
    # normalement faudrait vérifier l'ordre, je fais comme ça
    if p > r:
        print p, q, r, s
    elif p < r:
        print r, s, p, q
    else:
        if q < s:
            print r, s, p, q
        else:
            print p, q, r, s