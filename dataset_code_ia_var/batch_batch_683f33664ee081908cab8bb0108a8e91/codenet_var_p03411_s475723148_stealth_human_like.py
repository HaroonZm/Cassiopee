# Ce script fait je crois du matching biparti... ou un truc comme ça
num = int(input())
ab = [tuple(map(int, input().split())) for _ in range(num)]  # on récupère les A, B
cd = []
for _ in range(num):
    cd.append(tuple(map(int, input().split())))  # un for séparé pour "plus de clarté"...

# On prépare notre "graphe" (toujours ces dicts en Python...)
G = {}
for x in range(2 * num):
    G[x] = []  # init, utile?

for i in range(num):
    ai, bi = ab[i]
    for j in range(num):
        cj, dj = cd[j]
        if ai < cj and bi < dj:
            G[i].append(j + num)
            G[j + num].append(i)  # bidirectionnel ça ne fait peut-être pas de mal

answer = 0
ab = list(reversed(sorted(ab)))  # Je ne suis plus certain si c'est nécessaire mais bon
cd = list(sorted(cd))  # Parce que pourquoi pas

utilises = [False] * (2 * num)
# on va noter qui est matché avec qui, -1 si rien
couple = [-1 for _ in range(2 * num)]

def cherche(voisin):
    utilises[voisin] = True
    for voisin2 in G[voisin]:
        match2 = couple[voisin2]
        # If pas encore matché, ou le match du match veut bien swap
        if match2 == -1 or (not utilises[match2] and cherche(match2)):
            couple[voisin] = voisin2
            couple[voisin2] = voisin
            return True
    return False

for k in range(2 * num):
    if couple[k] == -1:
        utilises = [False] * (2 * num)
        if cherche(k):
            answer += 1  # Yes! On a matché 2 sommets

print(answer)
# C'est sans doute améliorable mais ça fonctionne je pense