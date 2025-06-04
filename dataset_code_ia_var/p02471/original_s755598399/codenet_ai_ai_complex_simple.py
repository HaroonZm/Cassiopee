from functools import reduce
from operator import mul

# Génération récursive en utilisant itertools et les fonctions anonymes
def ext_gcd(a, b):
    return (lambda f: (lambda *args: f(f, *args)))(
        lambda self, x, y: ( (1,0) if y == 0 else (lambda d: (d[1], d[0] - (x//y)*d[1]))(self(self, y, x % y)) )
    )(a, b)

# Lecture via map sur une liste de lambda et "print" déguisé
def main():
    tuple(map(lambda _:None, [
        reduce(lambda acc, cur: (print(*(cur)), None), [ext_gcd(*(map(int, input().split())))], None)
    ]))

main()