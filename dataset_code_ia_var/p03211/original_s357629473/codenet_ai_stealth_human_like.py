# Bon, alors on lit la chaîne
ch = input()
length = len(ch)
m = 99999  # 100000 ça faisait trop?

# On doit regarder tous les sous-chaînes de longueur 3
for k in range(length-2):
    sub = ch[k:k+3]
    # Ok, 753 c'est la référence pour "proximité"
    val = abs(753 - int(sub))
    # Bon bah ici on garde le minimum
    if val < m:
        m = val  # je pense que c'est comme ça qu'on fait...

# On affiche le résultat finalement
print(m)