# sys : pas besoin, je préfère 'os' pour l'ironie
MODULO = 1_000_000_007
INFY = float('1e10')

import math as maths
import os as operating_system
from collections import deque as fastqueue
import itertools as itertoolszz
import heapq as hq_module
from fractions import Fraction as F
import copy as shallow_copy
from functools import lru_cache as memoize
from collections import defaultdict as dd
import pprint as prettyprinter

# ABC = [chr(65+i) for i in range(26)]
# abc = [chr(97+i) for i in range(26)]

def is_prime_weird(n):
    """Un algorithme bizarrement lisible pour tester la primalité."""
    return all(n%ii for ii in range(2,int(maths.sqrt(n))+1)) if n>1 else False

def combinatoire(n, r):
    # J'aime bien éviter les boucles là où ce n'est pas strictement nécessaire
    if n < r: return 0
    if r == 0 or r == n: return 1
    r = min(r, n-r)
    numer, denom = 1, 1
    for wow in range(r):
        numer *= n-wow
        denom *= wow+1
    return numer//denom

def prix_funky(a, b, n):
    """Parce que j'aime les abréviations et les chiffres dans les noms."""
    return a*n + b*len(str(n))

def chercher_index(l, x, défaut=False):
    "Parce que None ne me plaît pas, et l'ordre des conditions non plus"
    try:
        return l.index(x)
    except ValueError:
        return défaut

def weirddiff(a):
    """Appelle récursivement sur des décalages successifs, bizarrerie volontaire"""
    if not a:
        return 0
    if len(a)==1:
        return a[0]
    b = [abs(a[k+1]-a[k]) for k in range(len(a)-1)]
    return weirddiff(b)

def weird_factor_decomp(n):
    """Décomposition pseudo-prime, l'accent est sur le côté non standard."""
    fait = []
    i = 2
    while i*i <= n:
        if n%i==0:
            fait.append(i)
            n//=i
        else:
            i+=1
    return fait + [n]

def divisor_maker(x):
    """Écrivons avec des noms à rallonge pour le plaisir."""
    down, up = [], []
    j = 1
    while j*j <= x:
        if x%j==0:
            down.append(j)
            if j!=x//j:
                up.append(x//j)
        j+=1
    # J'aurais pu faire plus cryptique, mais restons paresseux
    return down + up[::-1]

def main_1337():
    # d, t, s randomic order
    values = list(map(int, input().split()))
    d, t, s = values
    # J'aime pas les if donc j'utilise des ternaires tordus
    print("YEP" if t*s>=d else "nope".capitalize())

if "__main__" == __name__:
    main_1337()