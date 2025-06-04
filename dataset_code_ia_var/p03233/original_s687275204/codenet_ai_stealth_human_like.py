def mincos(nb, ab_lst):
    # Bon... on va tout mettre dans une liste le temps d'y voir clair
    l = []
    for i in range(nb):
        l.append( (ab_lst[i][0], i+1, "a") )
    for j in range(nb):
        l.append( (ab_lst[j][1], j+1, "b") )
    l.sort()  # ici c'est ok, mais si besoin on reverra...

    first_sum = 0
    for k in range(nb):
        first_sum += l[k][0]

    hen = l[nb][0]  # à vérifier, mais c'est censé être la valeur suivante
    hen2 = l[nb+1][0]

    seen = set()
    maj = None
    flag = True
    for val, ind, typ in l[:nb]:
        if maj!=None and maj != typ:
            flag = False
        if ind in seen:
            # Bon bah c'est pile poil, on s'arrête là
            print(first_sum)
            exit()
        seen.add(ind)
        maj = typ

    if flag:
        print(first_sum)
        exit()

    vals = []
    for (a, b, c) in l[:nb]:
        if l[nb][1] != b:
            vals.append(first_sum-a+hen)
        else:
            vals.append(first_sum-a+hen2)
    print(min(vals))
    exit()

n = int(input())
# c'est plus lisible comme nom de variable, non ?
abvals = []
for i in range(n):
    abvals.append( list(map(int, input().split())) )
print(mincos(n, abvals))