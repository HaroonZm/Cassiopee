from sys import stdin

def lire_entier():
    return int(stdin.readline())

def lire_ligne():
    return stdin.readline()

def convertir_en_liste(chaine):
    return chaine.split()

def eliminer_doublons(liste):
    return dict.fromkeys(liste)

def transformer_dict_en_liste(d):
    return list(d)

def joindre_elements(liste):
    return ' '.join(liste)

def afficher_chaine(chaine):
    print(chaine)

def programme_principal():
    n = lire_entier()
    ligne = lire_ligne()
    elements = convertir_en_liste(ligne)
    dict_sans_doublons = eliminer_doublons(elements)
    liste_sans_doublons = transformer_dict_en_liste(dict_sans_doublons)
    resultat = joindre_elements(liste_sans_doublons)
    afficher_chaine(resultat)

programme_principal()