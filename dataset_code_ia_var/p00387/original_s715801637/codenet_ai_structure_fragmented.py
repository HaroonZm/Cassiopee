def lire_ligne():
    return input()

def couper_ligne_en_mots(ligne):
    return ligne.split()

def convertir_en_entiers(liste):
    return list(map(int, liste))

def obtenir_A_B():
    ligne = lire_ligne()
    mots = couper_ligne_en_mots(ligne)
    entiers = convertir_en_entiers(mots)
    return entiers[0], entiers[1]

def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def ajouter_et_soustraire(a, b, c):
    return additionner(b, soustraire(a, c))

def ajout(a, b):
    return a + b

def calculer_resultat(A, B):
    intermediaire = additionner(B, A)
    val = soustraire(intermediaire, 1)
    return diviser_entiere(val, A)

def diviser_entiere(a, b):
    return a // b

def afficher_res(res):
    print(res)

def main():
    A, B = obtenir_A_B()
    resultat = calculer_resultat(A, B)
    afficher_res(resultat)

main()