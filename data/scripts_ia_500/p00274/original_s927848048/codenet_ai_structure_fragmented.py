def lire_entree():
    return input()

def convertir_chaine_entiers(chaine):
    return map(int, chaine.split())

def valeur_maximum(liste):
    return max(liste)

def liste_filtrée(liste):
    return [i for i in liste if i > 0]

def condition_na(liste):
    return valeur_maximum(liste) < 2

def calculer_sortie(liste):
    if condition_na(liste):
        return "NA"
    else:
        return 1 + len(liste_filtrée(liste))

def boucle_principale():
    while True:
        n = lire_entree()
        if n == '0':
            break
        t = convertir_chaine_entiers(input())
        print(calculer_sortie(t))

boucle_principale()