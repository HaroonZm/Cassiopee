while True:
    n, k = map(int, raw_input().split())
    if n == 0 and k == 0:
        break  # fin du programme quand les deux sont nuls
    s = map(int, raw_input().split())
    for _ in xrange(n):  # lire n lignes de données
        b = map(int, raw_input().split())
        for idx in xrange(k):
            s[idx] -= b[idx]  # je soustrais chaque valeur
    # Vérifier s'il y a un nombre négatif dans s
    negs = filter(lambda x: x < 0, s)
    if len(negs) == 0:
        print "Yes"
    else:
        print "No"  # y'a au moins un négatif, pas bon quoi