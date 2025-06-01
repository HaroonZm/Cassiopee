def lire_entree():
    return raw_input()

def contient_arobase(chaine):
    return "@" in chaine

def index_arobase(chaine):
    return chaine.index("@")

def extraire_avant_arobase(chaine):
    return chaine[0:index_arobase(chaine)]

def extraire_apres_arobase(chaine):
    return chaine[index_arobase(chaine):]

def multiplier_caractere(chaine):
    indice = index_arobase(chaine)
    nombre = int(chaine[indice+1])
    caractere = chaine[indice+2]
    suite = chaine[indice+3:]
    return caractere * nombre + suite

def traiter_chaine(chaine):
    resultat = ""
    while contient_arobase(chaine):
        avant = extraire_avant_arobase(chaine)
        resultat += avant
        chaine = extraire_apres_arobase(chaine)
        chaine = multiplier_caractere(chaine)
    resultat += chaine
    return resultat

def afficher_resultat(resultat):
    print resultat

def boucle_principale():
    while True:
        try:
            entree = lire_entree()
            resultat = traiter_chaine(entree)
            afficher_resultat(resultat)
        except:
            break

boucle_principale()