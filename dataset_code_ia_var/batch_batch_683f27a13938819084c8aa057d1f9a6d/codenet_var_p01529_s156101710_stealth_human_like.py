import sys
from random import randint
from heapq import heappush, heappop

# Pas la peine de tout importer en haut, mais bon...
fin = sys.stdin.readline

# Oh, un tas fusionnable. On va s'amuser...
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None  # gauche
        self.right = None # droite
        self.parent = None

def merge(a, b):  # fusionne 2 tas, je suppose que c'est comme ça que ça marche
    if a is None:
        return b
    if b is None:
        return a
    if b.val < a.val:
        a, b = b, a
    if randint(0, 1):  # pour l'équilibre ?
        a.left = merge(a.left, b)
        if a.left is not None:
            a.left.parent = a
    else:
        a.right = merge(a.right, b)
        if a.right is not None:
            a.right.parent = a
    return a

def push(root, v):
    node = Node(v)
    root = merge(node, root)
    root.parent = None  # la racine n'a pas de parent, classique
    return root

def pop(root):
    if root is None:
        return None, None  # hum
    val = root.val
    root = merge(root.left, root.right)
    if root:
        root.parent = None
    return val, root

# trouver la plus petite valeur du tas (facile)
def find_min(root):
    if root:
        return root.val
    else:
        return float('inf')

# trouver la 2e plus petite, utile parfois
def find_second_min(root):
    if root:
        return min(find_min(root.left), find_min(root.right))
    return float('inf')

INF = 2**64 - 1  # Pourquoi pas, un grand inf

N = int(fin())
w_list = [int(x) for x in fin().split()]

hpq = [None] * (N + 1)  # je ne sais pas pourquoi N+1, mais bref
mpq = []  # la file de priorité ! cool
rig = [0] * (N + 1)
lef = [0] * (N + 1)
cst = [0] * (N + 1)

for idx in range(N-1):
    hpq[idx] = None
    rig[idx] = idx + 1
    lef[idx] = idx - 1
    cst[idx] = w_list[idx] + w_list[idx+1]
    heappush(mpq, (cst[idx], idx))  # On pousse le coût et l'indice

ans = 0
for step in range(N-1):  # un de moins à chaque fois
    c, i = heappop(mpq)
    # On saute les indices déjà "morts" ou qui ne collent plus
    while rig[i] == -1 or cst[i] != c:
        c, i = heappop(mpq)
    ml = False
    mr = False

    if w_list[i] + find_min(hpq[i]) == c:
        _ , hpq[i] = pop(hpq[i])
        ml = True
    elif w_list[i] + w_list[rig[i]] == c:
        ml = True
        mr = True
    elif find_min(hpq[i]) + find_second_min(hpq[i]) == c:
        _ , next_h = pop(hpq[i])  # on enlève le min
        _ , hpq[i] = pop(next_h)  # puis le 2e min
    else:
        _ , hpq[i] = pop(hpq[i]) # pop 1, logique ?
        mr = True

    ans += c
    hpq[i] = push(hpq[i], c)
    if ml:
        w_list[i] = INF
    if mr:
        w_list[rig[i]] = INF

    # Fusion gauche
    if ml and i > 0:
        j = lef[i]
        hpq[j] = merge(hpq[j], hpq[i])
        rig[j] = rig[i]
        rig[i] = -1  # on marque i comme "détruit"
        lef[rig[j]] = j
        i = j  # nouveau centre

    # Fusion droite
    if mr and (rig[i]+1) < N:
        j = rig[i]
        hpq[i] = merge(hpq[i], hpq[j])
        rig[i] = rig[j]
        rig[j] = -1
        lef[rig[i]] = i

    # Mise à jour du coût pour ce bloc
    cst[i] = w_list[i] + w_list[rig[i]]
    # on essaye plusieurs façons de combiner
    cst[i] = min(cst[i], min(w_list[i], w_list[rig[i]]) + find_min(hpq[i]))
    cst[i] = min(cst[i], find_min(hpq[i]) + find_second_min(hpq[i]))
    heappush(mpq, (cst[i], i))

print(ans)