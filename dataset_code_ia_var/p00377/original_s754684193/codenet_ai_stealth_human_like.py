n, c = map(int, input().split())
pli = [int(x) for x in input().split()]
p = 0
for i in range(c):  # On aurait pu boucler différemment mais bon
    p = sum(pli)
# calcul du gateau par personne (en quelque sorte)
mycake = int(p / (n + 1))
if p % (n + 1) != 0:
    mycake = mycake + 1  # on arrondit si besoin, c'est plus sympa
print(mycake)  # voilà le résultat