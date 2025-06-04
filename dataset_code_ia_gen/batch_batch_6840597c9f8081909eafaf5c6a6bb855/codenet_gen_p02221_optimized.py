import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
S = input().rstrip()
P = list(map(int, input().split()))
M = 2**N

# Préparation d'un tableau de résultats de matchs direct entre joueurs
# winner(x,y) retourne le gagnant entre x et y selon S
def winner(x, y):
    return x if S[y - x - 1] == '0' else y

# Construction d'un arbre segmentaire binaire sur P,
# chaque noeud contient le gagnant du tournoi des participants correspondants
# Cette structure permet de reconstruire rapidement le gagnant sous les rotations

size = 1 << N
tree = [0] * (2*size)

# Initialisation des feuilles
for i in range(size):
    tree[size + i] = P[i]

# Construction de l'arbre
for i in range(size - 1, 0, -1):
    tree[i] = winner(tree[i << 1], tree[i << 1 | 1])

# Fonction pour extraire le gagnant d'un segment de taille power of two
# Sous le décalage pos dans la permutation
def get_winner(pos):
    idx = 1
    offset = 0
    length = size
    while idx < size:
        length >>= 1
        left_pos = (pos - offset) % size
        if left_pos < length:
            idx = idx << 1
        else:
            offset += length
            idx = idx << 1 | 1
    return tree[idx]

# Pour éviter de simuler chaque rotation,
# on exploite que le tournoi est binaire et l'ordre cyclique des joueurs.
# On pré-calculera un tableau de résultats pour les décalages
# par une technique de DP sur arbre segmentaire binaire.

# Ici, on représente la position des joueurs dans la rotation avec un décalage k.
# Pour chaque noeud de l'arbre, on stocke un tableau winners_sub: taille = taille sous-arbre,
# winners_sub[d] = gagnant quand la racine subit une rotation de d modulo taille_sous_arbre
# Puis on combine pour remonter l'arbre

# Implémentation bottom-up

# winners_sub pour feuilles : gagnant stable = joueur lui même
winners_sub = [[p] for p in P]

size_subtree = 1
for _ in range(N):
    next_winners = []
    size_subtree <<= 1
    half = size_subtree >> 1
    for i in range(0, len(winners_sub), 2):
        left = winners_sub[i]
        right = winners_sub[i+1]
        res = [0]*size_subtree
        # Pour décalage d dans [0, size_subtree)
        # On veut déterminer qui gagne en fonction des décalages dans les sous-arbres
        # Le tournoi se déroule en un match final entre left_gagne et right_gagne
        for d in range(size_subtree):
            # décalage dans sous-arbres
            d_left = d % half
            d_right = d % half
            wL = left[d_left]
            wR = right[d_right]
            res[d] = winner(wL, wR)
        next_winners.append(res)
    winners_sub = next_winners

# winners_sub[0][k] donne le gagnant du tournoi sous la rotation k modulo M

for k in range(M):
    print(winners_sub[0][k])