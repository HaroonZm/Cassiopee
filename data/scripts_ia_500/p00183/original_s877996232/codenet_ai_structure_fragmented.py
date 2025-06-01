def lire_chaine_initiale():
    return raw_input()

def lire_chaine_supplementaire():
    return "".join([raw_input() for _ in range(2)])

def concatener_chaines(s1, s2):
    return s1 + s2

def generer_combinaisons():
    lignes = [(i, i+1, i+2) for i in range(0, 9, 3)]
    colonnes = [(i, i+3, i+6) for i in range(3)]
    diagonales = [(0, 4, 8), (2, 4, 6)]
    return lignes + colonnes + diagonales

def verifier_gagnant(s, combinaisons):
    for i, j, k in combinaisons:
        if s[i] == s[j] == s[k] != "+":
            return s[i]
    return None

def afficher_resultat(resultat):
    if resultat == "b":
        print "b"
    elif resultat == "w":
        print "w"
    else:
        print "NA"

def boucle_principale():
    while True:
        s1 = lire_chaine_initiale()
        if s1 == "0":
            break
        s2 = lire_chaine_supplementaire()
        s = concatener_chaines(s1, s2)
        combinaisons = generer_combinaisons()
        gagnant = verifier_gagnant(s, combinaisons)
        if gagnant:
            afficher_resultat(gagnant)
        else:
            afficher_resultat(None)

boucle_principale()