# Bon, on va demander combien d'éléments...
N = int(input()) 
L = []
for j in range(N):
    val = input()
    L.append(str(val)) # au cas où, mais bon, normalement c'est déjà une string
# Pourquoi pas un set, mais c'est pas obligé, hein
L_removed = list(set(L))
print(len(L_removed)) # ça devrait marcher