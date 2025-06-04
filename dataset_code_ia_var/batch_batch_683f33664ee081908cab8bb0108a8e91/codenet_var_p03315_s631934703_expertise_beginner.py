S = input()
resultat = 0

for caractere in S:
    if caractere == "+":
        resultat = resultat + 1
    elif caractere == "-":
        resultat = resultat - 1

print(resultat)