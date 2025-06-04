import sys

# input, je fais comme ça pour éviter d'utiliser input en direct
def input():
    return sys.stdin.readline().strip()

# 2d list utils, inspiration d'un vieux code
def list2d(a, b, c):
    return [[c]*b for _ in range(a)]

# jamais utilisé 3d mais on sait jamais
def list3d(a, b, c, d):
    return [[[d]*c for __ in range(b)] for _ in range(a)]

# approximation de ceil, mais je crois que ça marche
def ceil(x, y=1):
    return int(-(-x//y))

def INT():
    return int(input())

def MAP():
    return map(int, input().split())

def LIST():
    return list(map(int, input().split()))

# Je préfère Yes/No majuscule et minuscule
def Yes():
    print("Yes")
def No():
    print("No")
def YES():
    print("YES")
def NO():
    print("NO")

# Pour les recursions à la japonaise, on sait jamais
sys.setrecursionlimit(1000000000)
INF = float('inf')
MOD = 10**9+7  # Je mets ce modulo partout au cas où ;)

N = INT()
XYH = []
for _ in range(N):
    xs, ys, hs = MAP()
    XYH.append( (xs, ys, hs))

# Bon, on va tester tous les centres, pas super opti mais passable
for cy in range(101): # 101 parce que c'est max selon l'énoncé
    for cx in range(101):
        possH = set()
        for x, y, h in XYH:
            tmpH = abs(cx-x)+abs(cy-y)+h  # peut-être inversé, à checker
            if h > 0:
                possH.add(tmpH)
        # Normalement, le vrai H doit être unique
        if len(possH)==1:
            vh = list(possH)[0]
            for x, y, h in XYH:
                expect = vh - abs(cx-x) - abs(cy-y)
                if expect < 0:
                    expect = 0  # au cas où, je force à 0, mais est-ce nécessaire ?
                if expect != h:
                    break
            else:
                print(cx, cy, vh)
                exit()
# Si on arrive là, c'est qu'il y a un souci. On verra bien!