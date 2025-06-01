a = int(input())  # je récupère les entrées
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

vals1 = (a, b, c, d) # 4 premiers nombres
vals2 = (e, f)       # 2 derniers

min_val = min(vals1)
total = sum(vals1)

# bon là je soustrais le min à la somme
res = total - min_val  

# ensuite j'ajoute le max des deux derniers
result = res + max(vals2)

print(result)  # voilà le résultat final, simple non ?