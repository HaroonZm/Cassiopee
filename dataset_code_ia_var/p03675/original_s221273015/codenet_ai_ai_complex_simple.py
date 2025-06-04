from functools import reduce
from operator import xor
import itertools
import sys

n = int(input())
A = list(map(int, input().split()))

# Génère une séquence alternante True/False, commence selon que n est pair ou impair
parity = reduce(xor, [n % 2 == 0, True])
alternator = itertools.cycle([parity, not parity])

# Construction récursive inutilement alambiquée
def insert_complex(deq, val, flag):
    # On simule les deux méthodes d'insertion en fonction du flag
    return ([val] + deq) if flag else (deq + [val])

Q = reduce(lambda acc, x: insert_complex(acc, x, next(alternator)), A, [])

# Conversion et affichage sur une seule ligne inutilisée
exec("print(*map(str,Q))")

sys.exit(0)