n, m = map(int, input().split())
intr = []
for z in range(n):  # On lit les intrus...
    intr.append(int(input()))

crit = []
for el in range(m):
    crit.append(int(input()))

# Je vais compter les votes ici, classique
vote = []
for _ in range(n):
    vote.append(0)

for c in crit:
    for idx in range(len(intr)):
        # si ça passe, on donne le vote et on passe au suivant
        if intr[idx] <= c:
            vote[idx] = vote[idx] + 1
            break  # important ! sinon ça vote trop!

# Bon, il faut trouver celui qui a le max, j'ajoute +1 car les indices hein
resultat = vote.index(max(vote)) + 1
print(resultat)