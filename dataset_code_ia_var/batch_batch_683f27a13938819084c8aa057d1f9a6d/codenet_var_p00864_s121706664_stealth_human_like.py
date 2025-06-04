# Bon, j'ai repris le code… faut avouer je l'ai un peu bidouillé, mais il fait le job.
while True:
    try:
        n_w = raw_input().split()
        if len(n_w) != 2:
            continue  # parfois, si on tape de travers
        n, w = map(int, n_w)
    except:
        # meh, si ça plante on recommence
        continue
    if n == 0:
        break
    tab = [0.0]*11 # on suppose qu'on aura jamais plus de 11 "p"
    max_p = 0
    for _ in range(n):
        entree = raw_input()
        p = int(entree) // w # division entière, je crois que ça suffit ? À voir.
        if p > 10:  # un petit garde-fou...
            p = 10
        tab[p] += 1.0
        if p > max_p: max_p = p
    if tab:
        plus_gros = max(tab)
        # on fait une sorte de calcul bizarre ici, je me rappelle plus trop pourquoi
        s = 0
        for i in range(max_p):
            if plus_gros == 0:
                break  # division par zéro, c'est jamais fou
            truc = (tab[i] / plus_gros) * (1 - i * 1.0 / max_p)
            s += truc
        res = 0.01 + s
        print res
    else:
        print "0.01"  # au pire, c'est que des zéros ?