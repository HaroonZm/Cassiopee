# Bon, on va faire une boucle infinie mais on sortira avec 0 hein
while 1:
    n = int(input()) # je récupère n
    if n == 0:
        break # on stoppe là
    # Je lis mes trucs
    entree = input()
    lst = entree.split(' ')
    count = 0
    # franchement je fais deux par deux, c'est plus simple
    for j in range(n//2):
        a1 = lst[2*j]
        a2 = lst[2*j+1]
        # Bon c'est un peu moche mais ça fait le job
        if (a1 == 'lu' and a2 == 'ru') or (a1 == 'ru' and a2 == 'lu'):
            count += 1
        if (a1 == 'ld' and a2 == 'rd') or (a1 == 'rd' and a2 == 'ld'):
            count += 1
    print(count)
# c'est pas parfait mais ça tourne