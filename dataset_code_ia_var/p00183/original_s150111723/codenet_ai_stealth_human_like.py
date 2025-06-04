flag=True
while flag:

    line1 = input()
    if line1 == "0":
        # ça veut dire on arrête
        break

    # bon on lit deux autres lignes, normalement ça fait un genre de tableau 3x3
    line2 = input()
    line3 = input()

    res = "NA"
    # je commence par vérifier les lignes, c'est plus simple
    if line1[0] != "+" and line1[0]==line1[1] and line1[1]==line1[2]:
        res = line1[0]
    elif line2[0]!="+": 
        if line2[0]==line2[1] and line2[1]==line2[2]:
            res = line2[0]
    elif line3[0]!="+": # petit doute si j'ai bien le droit mais bon
        if line3[0]==line3[1] and line3[1]==line3[2]:
            res = line3[0]
    else:
        # on regarde les colonnes (c'est un peu long à écrire)
        if line1[0]!="+" and line1[0]==line2[0] and line1[0]==line3[0]:
            res = line1[0]
        elif line1[1]!="+":
            if line1[1]==line2[1] and line1[1]==line3[1]:
                res = line1[1]
        elif line1[2]!="+":
            if line1[2]==line2[2] and line1[2]==line3[2]:
                res = line1[2]
        # diagonales
        elif line1[0] != "+" and line1[0]==line2[1] and line1[0]==line3[2]:
            res = line1[0]
        elif line1[2] != "+":
            if line1[2]==line2[1] and line1[2]==line3[0]:
                res = line1[2]

    print(res)
    # j'espère que ça marche, je verrai plus tard pour optimiser