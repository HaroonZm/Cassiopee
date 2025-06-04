# Bon, on lit le nombre, enfin je crois que c'est ça...
nombre = int(input())
# Hop, on prend la liste... mais bon, faudrait peut-être vérifier l'entrée un jour
la_liste = list(map(int, input().split()))
# On cherche la diff entre max et min, c'est ça l'idée non ?
diff = max(la_liste) - min(la_liste)
print(diff)
# j'espère que ça marche avec des négatifs aussi