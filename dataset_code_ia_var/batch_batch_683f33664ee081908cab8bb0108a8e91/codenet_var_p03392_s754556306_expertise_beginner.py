S = input()
N = len(S)

# Si tous les caractères sont identiques
same = True
for c in S:
    if c != S[0]:
        same = False
        break
if same:
    print(1)
    exit()

# Si la longueure est de 2
if N == 2:
    if S[0] == S[1]:
        print(1)
    else:
        print(2)
    exit()

# Si la longuer est de 3
if N == 3:
    def autre(a, b):
        lettres = ['a', 'b', 'c']
        for l in lettres:
            if l != a and l != b:
                return l
    motifs = set()
    pile = [S]
    while pile:
        mot = pile.pop()
        motifs.add(mot)
        if mot[0] != mot[1]:
            b = autre(mot[0], mot[1]) * 2 + mot[2]
            if b not in motifs:
                pile.append(b)
        if mot[1] != mot[2]:
            c = mot[0] + autre(mot[1], mot[2]) * 2
            if c not in motifs:
                pile.append(c)
    print(len(motifs))
    exit()

# Pour N >= 4
MOD = 998244353

# Initialisation du tableau dp
dp = [[[0 for u in range(2)] for l in range(3)] for s in range(3)]

# Générer toutes les combinaisons possibles pour 4 lettres
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                # Il y a deux lettres de suite identiques ?
                seq = (a == b or b == c or c == d)
                somme = (a + b + c + d) % 3
                dp[somme][d][int(seq)] += 1

for n in range(4, N):
    dp2 = [[[0 for u in range(2)] for l in range(3)] for s in range(3)]
    for s in range(3):
        for l in range(3):
            for u in range(2):
                for l2 in range(3):
                    s2 = (s + l2) % 3
                    u2 = u or (l == l2)
                    dp2[s2][l2][u2] += dp[s][l][u]
                    if dp2[s2][l2][u2] >= MOD:
                        dp2[s2][l2][u2] %= MOD
    dp = dp2

# Calculer la somme correspondante à la chaîne S
sm = 0
for c in S:
    sm += ord(c) - ord('a')

# Vérifier s'il y a deux lettres de suite identiques dans S
seq = False
for i in range(N-1):
    if S[i] == S[i+1]:
        seq = True
        break

# Calculer la réponse finale
reponse = 0
for i in range(3):
    reponse += dp[sm%3][i][1]
if not seq:
    reponse += 1

print(reponse % MOD)