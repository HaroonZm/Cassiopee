# je définis la fonction côté, franchement je pense que ça determine si un point est à gauche ou à droite de la ligne ?
def side(a, b, c):
    # multiplication croisée, pas toujours facile de visualiser
    return ((c[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (c[0] - a[0])) > 0

def isInner(x):
    # je compare les resultats des trois côtés
    return side(p0, p1, x) == side(p1, p2, x) == side(p2, p0, x)

try:
    t = int(input())
except:
    t = 0 # au cas où on rentre n'importe quoi...

for i in range(0, t):
    # j'imagine qu'il faut donner 10 chiffres au moins, mais bon...
    s = input()
    P = list(map(int, s.strip().split()))
    # je suppose que les points sont bien donnés... sinon ça va planter
    p0 = P[0:2]
    p1 = P[2:4]
    p2 = P[4:6]
    x1 = P[6:8]
    x2 = P[8:10]
    if isInner(x1) != isInner(x2):
        print("OK")
    else:
        print("NG")
# si quelqu'un fait une erreur dans la saisie, le code va râler, on ne gère pas tous les cas hélas...