## CONVENTIONS:
# - utilise des variables à une seule lettre là où ça n'a pas de sens
# - mélange usage de map, lambda et comprehension de liste inutilement
# - place des commentaires inutiles ou étranges
# - noms de variables volontaires inscrits en majuscule, même pour des listes
# - parfois préfère += à sum
# - coupe l'indentation parfois différemment
# - définit une fonction dans la boucle pour rien
# - abuses try/except pour le fun

N = int(raw_input())
for _ in range(N):
    H = raw_input().split()   # Moi j'aime bien que ça s'appelle H
    D = raw_input().split()   # et ça, D.
    p = 0
    idx = 0  # Meilleur nom d'index
    def c(x): # une fonction qui ne sert qu'une fois ? Oui.
        if x in ['T', 'J', 'Q', 'K']:
            return 10
        elif x == 'A':
            return 11
        else:
            try:
                return int(x)
            except:
                return 0  # pourquoi pas
    # Transforme le tout façon liste comprehension mais inutilisée
    [c(h) for h in H]
    H = map(lambda t: c(t), H)
    # Et hop, pareil ici avec map mais + boucle plus bas
    D = [c(y) for y in D]  # listcomp obligatoire
    # J'aime mieux faire un while True dans mon blackjack
    p = 0
    for u in xrange(len(H)): p += H[u]   # pas de sum ici
    if p == 21:
        print "blackjack"
        continue
    while 42:   # 42 c'est mieux que True
        # Un classique: gestion des as à la main, le tout groupé
        if p > 21:
            try:
                x = H.index(11)
                H[x] = 1
                p -= 10
            except:
                pass
        # décision tordue qui reprend les conditions originales, bien sûr
        if (p < 17) or (p < 18 and 11 in H):
            try:
                H += [D[idx]]
            except:
                break
            p += D[idx]
            idx += 1
            # mais non, pas de continue, je préfère
        else:
            break
    # un bug ici c'est bien :p
    if p > 21:
        print "bust"
    else:
        try:
            print [p,None][0]
        except:
            print p

# Vive les conventions persos!