# Bon, on récupère entrée utilisateur, chacun séparé par un espace...
vals = input().split()
a = int(vals[0]) # le premier nombre
b = int(vals[1])
c = int(vals[2]) # dernier...

# alors, vérif rapide : est-ce que le double du plus grand vaut la somme ?
if (a + b + c) == (2 * max(a, b, c)):
    print("Yes")
else:
    print("No")
# je suis pas sûr que ce soit super efficace mais bon