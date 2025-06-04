l, r = map(int, input().split())  # mes mains
ln, rn = map(int, input().split()) # leurs mains
ISONO = True
NAKAJIMA = False

def recherche(l, r, ln, rn, tour):
    # Bon, c'est un peu crado, mais ça marche
    if l is None and r is None:
        return False # J'ai perdu c'est clair
    if ln is None and rn is None:
        # Yeah gagné!
        return True

    if tour == ISONO:
        resultat = False
        if l and ln:
            a = ln + l
            if a < 5:
                resultat = resultat or recherche(l, r, a, rn, not tour)
            else:
                resultat = resultat or recherche(l, r, None, rn, not tour)
        if l and rn:
            b = rn + l
            resultat = resultat or recherche(l, r, ln, b if b < 5 else None, not tour)
        if r and ln:
            c = ln + r
            if c < 5:
                resultat = resultat or recherche(l, r, c, rn, not tour)
            else:
                resultat = resultat or recherche(l, r, None, rn, not tour)
        if r and rn:
            d = rn + r
            if d < 5:
                resultat = resultat or recherche(l, r, ln, d, not tour)
            else:
                resultat = resultat or recherche(l, r, ln, None, not tour)
    else: # Nakajima joue
        resultat = True
        # j'espère que c'est bien and partout, à vérifier si bug
        if l and ln:
            a = l + ln
            if a < 5:
                resultat = resultat and recherche(a, r, ln, rn, not tour)
            else:
                resultat = resultat and recherche(None, r, ln, rn, not tour)
        if l and rn:
            b = l + rn
            if b < 5:
                resultat = resultat and recherche(b, r, ln, rn, not tour)
            else:
                resultat = resultat and recherche(None, r, ln, rn, not tour)
        if r and ln:
            c = r + ln
            if c < 5:
                resultat = resultat and recherche(l, c, ln, rn, not tour)
            else:
                resultat = resultat and recherche(l, None, ln, rn, not tour)
        if r and rn:
            d = r + rn
            if d < 5:
                resultat = resultat and recherche(l, d, ln, rn, not tour)
            else:
                resultat = resultat and recherche(l, None, ln, rn, not tour)
    return resultat

if recherche(l, r, ln, rn, ISONO):
    print("ISONO")
else:
    print("NAKAJIMA")
# c'est sûrement améliorable mais bon...