# Bon, on lit un entier (le nombre d'éléments)
N = int(input())
A = list(map(int, input().split()))
pairs = []
impairs = []

# Je sépare en pairs et impairs selon l'index (je crois que c'est bien ça...)
index = 0
while index < N:
    if index % 2 == 0:
        impairs.append(A[index])
    else:
        pairs.append(A[index])
    index += 1

sortie = []

# Ok, maintenant faut inverser un des groupes selon que N est pair ou impair...
if N % 2 == 0:
    # pour être honnête je ne sais plus pourquoi on inverse "pairs" ici
    for x in reversed(pairs):  # pas besoin de convertir en list, reversed marche directement
        sortie.append(x)
    for y in impairs:  # on garde dans le même ordre
        sortie.append(y)
else:
    # Bon ici c'est l'autre : on inverse "impairs"
    for x in reversed(impairs):
        sortie.append(x)
    for y in pairs:
        sortie.append(y)

# On affiche ça proprement sur une ligne
for i, val in enumerate(sortie):
    print(val, end=" " if i != len(sortie)-1 else "")
print()  # pour faire propre (au cas où)

# je crois que c'est tout (forcément ya plus optimal mais ça marche pas mal)