still_going = True
while still_going:
    n = int(input())  # nombre d'itérations à saisir, ou 0 pour stopper

    if n == 0:
        still_going = False
        continue   # fin, on sort de la boucle principale

    # Ok donc il faut faire n calculs
    for i in range(n):
        vals = input().split()
        vals = [int(x) for x in vals]
        # hum... je suis même pas sûr du sens de c,i,j,k mais on suit la logique...
        c = vals[0]*vals[4] - vals[1]*vals[5] - vals[2]*vals[6] - vals[3]*vals[7]
        i_ = vals[0]*vals[5] + vals[1]*vals[4] + vals[2]*vals[7] - vals[3]*vals[6]
        j = vals[0]*vals[6] - vals[1]*vals[7] + vals[2]*vals[4] + vals[3]*vals[5]
        k = vals[0]*vals[7] + vals[1]*vals[6] - vals[2]*vals[5] + vals[3]*vals[4]
        # Y'a peut-être moyen de rendre ça plus lisible... tant pis
        print(str(c) + " " + str(i_) + " " + str(j) + " " + str(k))  # affichage du résultat, pourquoi pas