chaine = input()
compteur = 0
for caractere in chaine:
    if caractere == '+':
        compteur = compteur + 1
    else:
        compteur = compteur - 1
print(compteur)