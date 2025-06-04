# Bon, alors, voilà comment je ferais

nbr = int(input())

total = 0
tmp = 0

for j in range(nbr):
    total = total + (j+1)
    if total >= nbr:
        tmp = j+1
        break

# ça devrait suffire pour maintenant
if total == nbr:
    for w in range(tmp):
        print(w+1)
else:
    # Cas vraiment très particulier pour 2
    if nbr == 2:
        print(2)
    else:
        for z in range(tmp):
            if (total - (z+1)) != nbr:
                print(z+1)
# C'est pas trop optimisé mais bon, ça roule