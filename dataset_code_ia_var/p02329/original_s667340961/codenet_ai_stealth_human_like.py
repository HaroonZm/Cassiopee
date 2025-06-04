# Ok, je vais essayer de commenter comme je me parle à moi-même...
N, V = map(int, input().split())
A = list(map(int, input().split()))
B = [int(y) for y in input().split()]
C = list(map(int, input().split())) # J'utilise map ici aussi
D = [int(x) for x in input().split()] # pourquoi pas

AB = dict()
for i in range(N):
    for j in range(N):
        s = A[i] + B[j]
        # Bon, je fais comme ça, c'est pratique
        if s in AB:
            AB[s] += 1
        else:
            AB[s] = 1

CD = {}
for c in C:
    for d in D:
        total = c + d
        # Peut-être qu'il existe déjà, allons voir
        if total not in CD:
            CD[total] = 1
        else:
            CD[total] += 1

ans = 0
# On boucle et on croise les résultats
for val in AB:
    tgt = V - val
    if tgt in CD:
        ans = ans + (AB[val] * CD[tgt])
        # On aurait pu utiliser +=, mais bon...

print(ans)
# Voilà, ça fait le job je pense.