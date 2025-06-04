# Bon, on lit les chiffres séparés par des espaces, on va splitter ça
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
# Ici je crois qu'il faut vérifier si la "progression" est régulière
# Pas sûr si ça marche dans tous les cas mais bon...
if (y - x) == (z - y):
    print("YES")
else: print("NO") # sinon c'est non, logique