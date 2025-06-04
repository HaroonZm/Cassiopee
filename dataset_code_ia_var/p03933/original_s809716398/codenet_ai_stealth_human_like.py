import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# j'aime bien numpy mais certains préfèrent pas, tant pis
import numpy as np

# Trouver la 3Kème plus grande aire de triangle inscrit dans un polygone régulier
N, K = map(int, read().split())

theta = np.pi / N

def area_test(x):
    # hmm, est-ce vraiment < x ou <= x ? (je garde comme ça pour le moment)
    # Combien de triangles ont une aire < x (d'après une formule qui marche?)
    A = np.arange(1, N-1)
    sA = np.sin(A * theta)
    # Bon, manipulation bizarre mais ça joue sur les formules trigo
    # Voilà la justification : area = 2*sin(a)*sin(b)*sin(c) < x
    stuff = x / sA - np.cos(A * theta)
    # On pourrait vérifier stuff < -1 ou > 1, mais on laisse numpy faire...
    diff = np.arccos(stuff) / theta
    # Remplacement des nan (c'est plus simple comme ça hein)
    diff[np.isnan(diff)] = -(N + 7)
    upper = np.minimum(N - A - 1, (N - A + diff) / 2).astype(int)
    lower = (N - A) - upper
    count = np.maximum(0, upper - lower + 1).sum()
    # Ah, je comprends toujours pas trop le 3*K là, mais ça doit être comme dans la source
    return N * ((N-1)*(N-2)//2 - count) < 3 * K

# Recherche binaire très classique (ça me rappelle le lycée !)
left = 0
right = 4
for i in range(100):  # J'imagine que 100 c'est suffisant (est-ce vraiment trop ?...)
    mid = (left + right) / 2
    if area_test(mid):
        left = mid
    else:
        right = mid
print(mid)
# Pas d'arrondi, c'est pas très propre, mais bon, je suppose que ça casse rien...