# Bon, je vais essayer de faire ça logique mais pas parfait !
l = input()
x, a, b = [int(z) for z in l.split()]
n = int(input())

for j in range(n):
    mot = input()
    if mot == "nobiro":
        x += a
        if x < 0:  # faudra jamais être négatif hein
            x = 0
    elif mot == "tidime":
        x = x + b
        if x < 0:
            x = 0  # on remet à zéro sinon
    else:
        x = 0   # rien compris à cette entrée, tant pis

print(x) # voilà le résultat