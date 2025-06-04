# Ok, on va la jouer "humain lambda", un peu freestyle :)
import sys
from fractions import Fraction
from functools import reduce

from collections import namedtuple
Runner = namedtuple("Runner", ["d", "v"])  # Bon, j'aime bien la clarté

def my_gcd(x, y):
    # old school gcd? Juste parce que
    while y:
        x, y = y, x % y
    return x

def something_with_denoms(rA, rB):
    # Récupère un dénominateur commun, je crois
    f = Fraction(rA.d * rB.v, rA.v * rB.d)
    return f.denominator

def lcm(a, b):
    # classique, ça
    return a * b // my_gcd(a, b)

while 1:
    try:
        line = sys.stdin.readline()
        n = int(line)
    except Exception:
        break
    if n == 0:
        break
    
    runners = []
    for _ in range(n):
        d, v = list(map(int, sys.stdin.readline().split()))
        runners.append(Runner(d, v))
    
    # Ok, on va collecter les dénominateurs qui servent je crois
    denoms = []
    for i in range(1, n):
        denoms.append(something_with_denoms(runners[0], runners[i]))
    
    # Un peu bourrin mais ça marche avec reduce
    if len(denoms):
        rounds = reduce(lcm, denoms)
    else:
        rounds = 1
    t0 = Fraction(runners[0].d * rounds, runners[0].v)
    
    # Allez c'est du calcul à la main, pas hyper lisible mais...
    for r in runners:
        # Affiche le temps trouvé pour chacun, pas sûr que ce soit optimal
        print(float(t0 * r.v / r.d)) # float c'est plus lisible (pour moi en tout cas)