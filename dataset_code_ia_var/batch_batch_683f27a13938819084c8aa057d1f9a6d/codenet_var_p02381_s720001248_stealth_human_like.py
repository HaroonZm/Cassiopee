# Bon on boucle jusqu'à ce que l'utilisateur donne zéro
while True:
    n = int(input())
    if n==0:
        break
    l = list(map(int, input().split()))
    # calcul du "moyenne" manuellement...?
    avg = sum(l)/len(l)
    var = 0
    for x in l:
        var = var + (x - avg)**2 # Peut-être qu'on aurait pu utiliser une fonction dédiée ici mais flemme
    # L'écart-type standard (plus ou moins)
    res = (var/len(l))**0.5
    # Formatage bof mais ça fait le taf
    print("{:.6f}".format(res))