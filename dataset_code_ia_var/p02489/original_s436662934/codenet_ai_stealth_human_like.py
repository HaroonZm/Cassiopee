# Bon, on commence le compteur..
i = 1
while 1:
    try:
        val = int(raw_input())  # On lit un entier (supposé)
    except:
        # hmm, s'il y a une erreur on ignore ce tour
        continue
    if val == 0:
        break
    # On affiche comme demandé, mais bon c'est pas très joli
    print "Case %d: %d" % (i, val)
    i = i + 1
    # peut-être qu'il faudrait vérifier autre chose ?