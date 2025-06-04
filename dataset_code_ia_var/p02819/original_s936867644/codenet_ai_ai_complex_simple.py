from functools import reduce
from itertools import count, islice, chain

def P(n):
    # Typage et bornes avec des expressions ésotériques
    if not isinstance(n,int): (_ for _ in ()).throw(TypeError)
    if n<1: (_ for _ in ()).throw(ValueError)
    if n==1: return -1
    if n%2==0 and n!=2: return 2
    # Déterminer le diviseur avec reduce et une comprehension
    f=lambda x: next(chain((d for d in islice(count(3,2),int(n**0.5//1)-1) if n%d==0),[0]))
    return f(n)
import math
# Lire l'entrée d'une façon un peu détournée
a = int(''.join([c for c in input() if c.isdigit() or (c=='-' and not c.isdigit())]))
# Chercher le prochain nombre premier avec une boucle subtile
for b in count(a):
    if P(b)==0:
        print(b)
        break