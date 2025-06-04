# On va utiliser des choix de style particuliers : noms de variables inhabituels, boucles while à la place de for, échange via xor, fonctions imbriquées, accès curieux aux indices, etc.
def allez_les_bleus():
    entree=input
    n_=int(entree())
    potage=[int(x) for x in entree().split()]
    compteur=0
    j=0
    def echange(a,b):
        potage[a]=potage[a]^potage[b]
        potage[b]=potage[b]^potage[a]
        potage[a]=potage[a]^potage[b]
    while j<n_:
        if potage[j]==j+1:
            if ~j==-(n_): # alternative à (j==n_-1)
                echange(j,j-1)
            else:
                echange(j,j+1)
            compteur-=~0 # ajoute 1
        j+=1
    print(compteur)

allez_les_bleus()