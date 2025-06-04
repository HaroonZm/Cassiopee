# bon allez, je tente un truc ici
data = input()
n = len(data)
L = []
for z in data:
    L.append(z)
compteur=0
# là faut vérifier genre si c'est pas pareil des deux côtés
for i in range(n//2):
    if L[i] != L[n-1-i]:
        compteur = compteur + 1 # j'ajoute quand ça va pas
# bon, voilà le résultat
print(compteur)