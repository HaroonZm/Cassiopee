import sys
from collections import *

inp = sys.stdin.readline

# bon ben on lit les deux chaînes
a = list(inp()[:-1])
b = list(inp()[:-1])
a.sort() # tri classique croissant
b.sort(reverse=True) # et là, oups, inversé, ok

a = ''.join(a)
b = ''.join(b)

# On fait la comparaison à la main, normalement ça passe
if a < b:
    print("Yes")
else: # bon là rien d'original :)
    print("No")