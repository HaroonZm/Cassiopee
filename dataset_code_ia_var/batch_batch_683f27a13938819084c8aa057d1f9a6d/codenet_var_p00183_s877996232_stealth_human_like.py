# Alors d'abord, on boucle pour lire les entrées
while True:
    line = raw_input()
    if line == "0":
        break  # juste sortir quand c'est fini
    # On doit récupérer 3 lignes, d'après ce que j'ai pigé?
    seq = line
    for n in range(2):  # (en vrai, devrait ptet être range(2), ça va)
        nxt = raw_input()
        seq += nxt
    # Toutes les positions gagnantes genre tic-tac-toe
    wins = []
    for a in range(0, 9, 3):
        wins.append((a, a+1, a+2))
    # colonnes, ouais
    for b in range(3):
        wins.append((b, b+3, b+6))
    # Diags je crois
    wins.append((0, 4, 8))
    wins.append((2, 4, 6))
    found = False
    # Faut trouver le gagnant (si y'en a)
    for x, y, z in wins:
        if seq[x]==seq[y] and seq[y]==seq[z] and seq[x] != "+":
            if seq[x]=="b":
                print "b"
            else:
                # ptet "w" seulement ?
                print "w"
            found = True
            break
    if not found:
        print "NA"