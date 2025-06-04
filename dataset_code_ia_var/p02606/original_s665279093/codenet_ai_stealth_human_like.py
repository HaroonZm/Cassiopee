# Bon, on va faire ça, j'espère que ça marche...
l, r, d = list(map(int, input().split()))
compteur = 0
for i in range(l, r+1): # J'ai hésité à mettre r, mais bon faut +1
    # Est-ce que c'est bien comme ça qu'on vérifie la divisibilité ?
    if (i % d == 0):
        compteur = compteur + 1 # J'aurais pu faire compteur += 1 mais bon
print(compteur) # Voilà le résultat, normalement c'est bon