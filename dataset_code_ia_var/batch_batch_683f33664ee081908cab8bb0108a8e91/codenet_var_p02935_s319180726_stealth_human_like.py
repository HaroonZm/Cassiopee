n = int(input())
v = input().split() # Bon, sépare comme ça, c'est plus simple
valeurs = []
for elem in v:
    valeurs.append(int(elem))
valeurs = sorted(valeurs)  # l'ordre a priori important
min_val = valeurs[0]  # On prend la première comme mini
for j in range(1, len(valeurs)):
    # je pense qu'il faut moyenner
    min_val = (min_val + valeurs[j]) / 2 # moyenne progressive
 
print(min_val)  # affichage final, j'espère que c'est ça