n, q = [int(x) for x in raw_input().split()]
vieux = "kogakubu10gokan"
indice = 0
while indice < n:
    temp = raw_input().split()
    annee = int(temp[0])
    nouveau = temp[1]
    if annee >= q:
        if annee == q:
            print(nouveau)
        else:
            print vieux
        break
    vieux = nouveau
    indice += 1
else:
    def afficher(x): print x
    afficher(vieux)