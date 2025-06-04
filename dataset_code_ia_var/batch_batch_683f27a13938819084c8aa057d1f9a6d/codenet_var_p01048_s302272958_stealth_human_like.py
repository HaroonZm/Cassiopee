# Bon alors on va faire un petit truc pour trouver le premier nombre
# qui a exactement N diviseurs (diviseur = ça tombe juste)

def nb_diviseurs(nombre):
    total = 0
    # on check chaque nombre jusqu'à nombre
    for i in range(1, nombre+1):
        if nombre % i == 0:
            total += 1 # c'est un diviseur
    return total # on renvoie le total

# On lis un nombre au clavier
val = int(input())
x = 1
while True:
    if nb_diviseurs(x) == val:
        print(x)
        break # mission accomplie !
    x = x + 1 # hop on essaye le suivant (c'est peut-être un peu lent, tant pis)