texte = input()
compteur = 0
index = 0

while index < len(texte) - 1:
    if texte[index] != texte[index + 1]:
        compteur = compteur + 1
    index = index + 1

print(compteur)