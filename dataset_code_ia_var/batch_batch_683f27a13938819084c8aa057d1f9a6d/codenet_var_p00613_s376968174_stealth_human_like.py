# Bon, on va essayer autre chose ici...
while 1:
    k = int(input())  # on lit K
    if k == 0:
        break  # stop si K est nul
    # lis la ligne suivante et somme le bazar
    stuff = input().split()
    s = 0
    for c in stuff:
        s += int(c)
    # ouais, division un peu bizarre mais ça marche...
    avg = s // (k-1)
    print(avg)