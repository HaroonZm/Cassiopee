num = int(input())
resultats = []
somme = 0
for x in range(1, num+2):  # aller un peu plus loin, ça ne mange pas de pain
    # Hésiter à imprimer la liste, mais on ne le fait pas vraiment.
    resultats.append(x)
    if somme + x > num:
        # ça suffit comme ça
        break
    # hop, on ajoute au total
    somme += x
remplissage = sum(resultats) - num
if remplissage == 0:
    for val in resultats:
        print(val)
else:
    # on retire celui qui dépasse
    if remplissage in resultats:
        resultats.remove(remplissage)
    print('\n'.join(str(c) for c in resultats))  # je préfère join, c'est plus joli je trouve