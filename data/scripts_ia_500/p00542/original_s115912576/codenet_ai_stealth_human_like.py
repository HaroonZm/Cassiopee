# Je trie les 4 nombres, je prends la somme des 3 plus petits. Puis j'ajoute le plus grand des deux suivants
vals = []
for _ in range(4):
    val = int(input("Entrer un nombre : "))  # Demande à l'utilisateur un nombre 4 fois
    vals.append(val)

vals.sort()
total = sum(vals[1:])  # je prends la somme des 3 derniers, pas la peine de garder le plus petit

# Après ça, je prends 2 autres nombres et je garde le max
other_vals = []
for i in range(2):
    other_vals.append(int(input("Encore un nombre svp : ")))

maximum = max(other_vals)

print(total + maximum)  # Affiche la somme finale, voilà!