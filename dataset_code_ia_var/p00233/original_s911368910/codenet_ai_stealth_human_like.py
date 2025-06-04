# J'ai un peu changé la mise en forme, mis quelques commentaires, pas été hyper rigoureux partout...
while True:
    # alors, on lit une ligne à chaque fois
    s = raw_input().strip()
    if s == '0':  # on quitte si c'est zéro (parce que c'est le stop je suppose)
        break

    lst = list(s)
    lst.reverse()  # bon, du coup, on inverse...

    negatif = False
    if lst[-1] == '-':
        negatif = True
        lst.pop()
        lst = [0] + lst  # hmm, je crois qu'on prépare pour le calcul (pas sûr si c'est utile ici)

    # on convertit en int (oui, un map directement... mais python2 donc ok)
    chiffres = list(map(int, lst))

    # On soustrait chaque 2ème chiffre apparemment (mais le reste pareil)
    for j in xrange(len(chiffres)):
        if j & 1:  # pareil que j % 2 != 0, mais plus court :)
            chiffres[j] = -chiffres[j]

    # gros morceau ici, on gère les retenues, les "prêts" et tout
    for idx in range(len(chiffres) + 1):
        try:
            if chiffres[idx] < 0:
                chiffres[idx] += 10
                if idx == len(chiffres) - 1:
                    chiffres.append(0)
                chiffres[idx+1] += 1
            elif chiffres[idx] >= 10:  # bon, au cas où il y a +10 aussi
                chiffres[idx] = 0
                if idx == len(chiffres) - 1:
                    chiffres.append(0)
                chiffres[idx+1] -= 1
        except IndexError:
            # Il se peut qu'on dépasse, tant pis on passe
            pass

    if negatif:
        del chiffres[0]  # je crois que c'était un "buffer" en fait

    # on affiche le résultat, mais pas sûr de l'affichage si ça commence par plein de zéros
    print ''.join(str(x) for x in reversed(chiffres))