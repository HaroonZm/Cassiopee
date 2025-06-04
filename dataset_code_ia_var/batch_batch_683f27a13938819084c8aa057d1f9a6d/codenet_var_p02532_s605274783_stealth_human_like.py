# C'est un ptit gestionnaire de blocs/piles, pas mal hein

n = int(input())  # ouf, faut que ce soit en int sinon ça plante

blocks = [list() for i in range(n)]
pops = []

while 1:
    try:
        # Je split sur espace, parce que c'est comme ça...
        stuff = input().split(' ')
        # Ah mince, 'str' c'est inutile ici, normalement...
        # command = map(str, stuff)
        # Bon on prend les indices
        cmd = stuff[0]

        # On fait les commandes
        if cmd == "quit":
            # hey, on affiche tous les pops
            for _ in pops:
                print(_)
            break
        elif cmd == 'push':
            # push dans le bon block, +1 car sinon c'est pas le bon index
            k = int(stuff[1])-1
            blocks[k].append(stuff[2])
        elif cmd == 'pop':
            k = int(stuff[1])-1
            pops.append(blocks[k][-1])
            blocks[k].pop()
        else: # move ou autre, tant pis
            a = int(stuff[1])-1
            b = int(stuff[2])-1
            blocks[b].append(blocks[a][-1])
            #pop en deux fois pr être sûr
            blocks[a].pop()

    except EOFError:
        # bon bah si y a plus d'entrée c'est fini hein
        break