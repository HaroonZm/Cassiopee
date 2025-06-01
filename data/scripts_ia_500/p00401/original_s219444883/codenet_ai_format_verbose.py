nombre_entree = int(input())

valeur_compteur = 0

for exposant in range(1, nombre_entree + 1):

    if nombre_entree < 2 ** exposant:

        valeur_compteur = 2 ** (exposant - 1)

        break

print(valeur_compteur)