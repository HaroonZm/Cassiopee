# Bon, je vais tenter de compter les différences
S=input()
c=0
for j in range(0, int(len(S)/2)):
    # On compare les deux caractères... si ça ne va pas, ajoute 1
    if S[j] != S[len(S)-1-j]:
        c=c+1
# et voilà, on affiche combien ça fait (pas sûr s'il fallait retourner ça ou l'imprimer)
print(c)