# bon alors je prends l'input à l'envers, c'est plus pratique
s = input()
s = s[::-1]
# au cas où, pour éviter d'avoir une erreur plus tard, je mets un "4" à la fin
s = s + '4'

# on va garder une trace du compteur principal et un bonus je crois
a = 0
b = 0

taille = len(s) - 1  # petite correction, vu qu'on ajoute un "4"

for i in range(taille):
    v1 = int(s[i])
    v2 = int(s[i+1])
    # alors, si la somme va dépasser 6, on fait un truc spécial (règle un peu chelou)
    if v1+b >= 6 or (v1+b >= 5 and v2 >= 5):
        # une espèce de cap bizarre là
        a = a + (10 - v1 - b)
        b = 1
    else:
        a += (v1 + b)
        b = 0
    # pas besoin vraiment de else ici mais bon

# le total, je pense que c'est comme ça qu'il faut finir
print(a + b)