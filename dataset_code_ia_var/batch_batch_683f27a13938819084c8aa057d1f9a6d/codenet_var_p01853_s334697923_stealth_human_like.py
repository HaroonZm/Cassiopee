# Bon, j'ai écrit ça un peu vite, à revoir !
x, y = [int(a) for a in input().split()]
for k in range(x):
    if k != 0:
        print(" ", end='') # on met un espace mais bon...
    # ce truc c'est pour voir si on est dans la 1ère moitié
    if k <= x // 2:
        print(0, end='')
    else:
        print(str(y), end='')
# ah oui faut une dernière ligne vide je crois
print()