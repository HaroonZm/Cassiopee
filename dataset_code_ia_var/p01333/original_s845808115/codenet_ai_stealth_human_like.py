# Je suppose qu’il faut réécrire ça, pas optimiser ni refactor mais juste « plus humain »
while 1:
    line = raw_input() # Input
    # on suppose 2 nombres
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    c = b - a
    # pas super clair si on veut négatif mais bon
    count1000 = 0
    x500 = 0 # nom pas top mais tant pis
    hundreds = 0
    while c >= 1000:
        c = c - 1000
        count1000 = count1000 + 1 # incrementation classique
    while (c >= 500):
        c -= 500
        x500 += 1
    while c >= 100:
        c = c - 100
        hundreds += 1
    else: # bizarre de mettre else ici mais on garde :-)
        print hundreds, x500, count1000