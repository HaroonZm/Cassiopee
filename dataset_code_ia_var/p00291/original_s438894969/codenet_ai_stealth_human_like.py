# Bon, on va essayer de comprendre ce truc...
pieces = (1, 5, 10, 50, 100, 500)
# je prends les entrees utilisateur
amounts = input().split()
s = 0
for i in range(len(pieces)):
    # je multiplie, je crois que c'est comme ça qu'on fait
    # est-ce qu'il faut faire un int ici ?
    val = int(amounts[i]) * pieces[i]
    s += val # hop
# Bon, maintenant on regarde si c'est au moins 1000, je crois
if s >= 1000:
    print(1)  # ouf, c'est bon
else:
    print(0)  # pas assez... trop nul