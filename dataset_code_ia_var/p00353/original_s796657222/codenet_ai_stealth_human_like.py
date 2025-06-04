# Bon, je récupère trois nombres, ça devrait marcher comme ça
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

# Si c'est déjà atteint, je dis rien à faire
if x >= z:
    print(0)
else:
    diff = z - x
    # Euh, je crois que c'est bon comme ça
    if diff <= y:
        print(diff)
    else:
        print("NA")  # Pas possible je suppose