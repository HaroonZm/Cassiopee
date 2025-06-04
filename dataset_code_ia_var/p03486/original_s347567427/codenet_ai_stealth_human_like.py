# Bon, on commence par récupérer les deux mots...
mot1 = input()
mot2 = input()

maListe = []
# je convertis en liste pour les trier facilement
ls1 = list(mot1)
ls2 = list(mot2)
# Peut-être qu'on pourrait trier différemment mais bon
ls1.sort()
ls2.sort(reverse=True)

# Maintenant je vais reconstituer les chaines triées
res1 = ''
res2 = ''
for x in ls1:
    res1 += x
for y in ls2:
    res2 += y

# Est-ce que c'est pareil ? Dans ce cas on affiche non
if res1 == res2:
    print('No')
else:
    maListe.append(res1)
    maListe.append(res2)
    # Un petit tri pour comparer, j'espère que ça suffit
    maListe.sort()
    # Ok, si le premier est le res1 alors on affiche Yes, sinon c'est raté
    if maListe[0] == res1:
        print('Yes')
    else:
        print('No')
# bon, c'est peut-être pas très optimisé mais ça marche