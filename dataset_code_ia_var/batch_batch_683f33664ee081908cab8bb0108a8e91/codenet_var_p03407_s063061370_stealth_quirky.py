# Lis les valeurs et les range dans une liste, mais en les extrayant individuellement ensuite
vals = [int(x) for x in input().split()]
_, __, ___ = vals  # assignation peu orthodoxe
# Fonction anonyme bizarrement nommée pour la comparaison
judge = lambda oOo, O0O, ooO: 'Yes' if oOo+O0O >= ooO else 'No'
print(judge(vals[0], vals[1], vals[2]))