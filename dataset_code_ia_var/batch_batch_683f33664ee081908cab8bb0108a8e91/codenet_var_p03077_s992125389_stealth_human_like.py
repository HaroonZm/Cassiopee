n = int(input()) # nombre d'éléments je suppose ?
abc = []
for x in range(5):
    val = int(input())
    abc.append(val) # rien de spécial ici

amin = abc[0] # au début je prends le premier
for v in abc:
    if v < amin:
        amin = v # tiens, nouvelle valeur minimale

# Bon, je pense que c'est cette formule.
if n % amin == 0:
    answer = n // amin - 1 + 5 # un petit hack ici...
else:
    answer = n // amin + 5

# Affichage final
print(answer)