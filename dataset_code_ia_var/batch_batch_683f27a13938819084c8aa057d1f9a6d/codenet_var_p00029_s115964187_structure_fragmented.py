def lire_entree():
    return raw_input()

def separer_mots(entree):
    return entree.split()

def initialiser_dictionnaire():
    return {}

def initialiser_chaine():
    return ''

def longueur(mot):
    return len(mot)

def maj_dawa_si_plus_long(dawa, mot):
    if longueur(mot) > longueur(dawa):
        return mot
    return dawa

def compter_occurrences(mots, mot):
    return mots.count(mot)

def maj_dictionnaire(d, nombre, mot):
    d[nombre] = mot
    return d

def obtenir_cles(d):
    return d.keys()

def max_cle(cles):
    return max(cles)

def obtenir_valeur(d, cle):
    return d.get(cle)

def formatter_sortie(mot1, mot2):
    return '%s %s' % (mot1, mot2)

def afficher(resultat):
    print resultat

def traiter():
    entree = lire_entree()
    mots = separer_mots(entree)
    dawa = initialiser_chaine()
    d = initialiser_dictionnaire()
    for w in mots:
        dawa = maj_dawa_si_plus_long(dawa, w)
        nb = compter_occurrences(mots, w)
        d = maj_dictionnaire(d, nb, w)
    cles = obtenir_cles(d)
    m = max_cle(cles)
    akeh = obtenir_valeur(d, m)
    sortie = formatter_sortie(akeh, dawa)
    afficher(sortie)

traiter()