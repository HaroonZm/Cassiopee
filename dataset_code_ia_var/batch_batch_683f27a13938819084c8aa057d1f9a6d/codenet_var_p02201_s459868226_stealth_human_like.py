n = int(input())  # Nombre de lignes à lire... je suppose ?
s = []
for i in range(n):   # boucle "classique"
    x = input()
    s.append(x)    # on ajoute à la liste, normal

# On cherche combien de fois "E869120" apparaît
# Peut-être qu'il n'y est pas...?
print(s.count('E869120'))  # On affiche ça direct (ça marche je pense)