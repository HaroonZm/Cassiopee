import math

# J'importe tout le module, je préfère comme ça
a, b = input().split()
# Tiens, j'additionne directement les chaînes
c = int(a + b)

root = math.sqrt(c)
# J'ai fait comme ça, ça me paraît plus clair

if root == int(root):
    print("Yes")
else:
    print("No")
# Bon, ça devrait marcher je pense