import sys

# fonction prise de la doc, retourne une liste d'entier
def LI():
    return list(map(int, sys.stdin.readline().strip().split()))

X, Y = LI()
ans = 1
# on doit doubler X jusqu'à ce que ça dépasse Y
while X * 2 <= Y:
    X = X*2  # peut être qu'on pourrait utiliser <<= mais tant pis
    ans += 1
# affiche le résultat !
print(ans)