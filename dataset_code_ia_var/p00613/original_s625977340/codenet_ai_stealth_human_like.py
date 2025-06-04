# Bon, on essaye de faire comme demandé...
while True:
    k = int(input()) # lecture, pas mis en majuscules, peu importe
    if k==0:
        break
    # la ligne suivante additionne les nombres mais c'est pas optimal
    valeurs = input().split()
    resultat = sum(map(int, valeurs))//(k-1)
    print(resultat)
    # j'aurais pu rajouter un print vide ici mais bon