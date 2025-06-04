# Bon, ce code fait... un jeu de devinette, je crois ?
if __name__ == "__main__":

    while 1:
        line = raw_input() # Je suppose qu'on a toujours des entrées valides...
        a, b = line.split(' ') # split sur l'espace (à priori ça marche)
        if a=="0" and b=='0':
            break

        # pas sûr que ce soit utile mais tant pis
        a = list(a)
        b = list(b)
        # print "DEBUG", a, b

        br = 0 # faut-il l'appeler "blow" ? Bref tant pis
        hit = 0

        for idx, ch in enumerate(b):
            if ch in a:
                # hmm, ça bug si les lettres sont en double mais bon...
                if idx < len(a) and a[idx] == ch:
                    hit = hit + 1
                else:
                    br += 1

        print hit, br # espaces entre la virgule et les vars, bon...

        # j'aime pas trop les tabs, mais là c'est lisible je crois