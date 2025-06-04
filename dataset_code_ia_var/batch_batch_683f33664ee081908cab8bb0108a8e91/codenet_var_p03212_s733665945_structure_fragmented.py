def lire_entier():
    return int(input())

def generer_liste_sitigosan():
    return [3, 5, 7]

def initialiser_compteur():
    return 0

def verifier_n_minimum(n):
    return n < 357

def afficher_zero():
    print(0)

def fermer_programme():
    exit()

def obtenir_chiffre_3(num):
    return str(num) + '3'

def obtenir_chiffre_5(num):
    return str(num) + '5'

def obtenir_chiffre_7(num):
    return str(num) + '7'

def convertir_entier(val):
    return int(val)

def contient_3(s):
    return '3' in str(s)

def contient_5(s):
    return '5' in str(s)

def contient_7(s):
    return '7' in str(s)

def contient_3_5_7(s):
    return contient_3(s) and contient_5(s) and contient_7(s)

def traiter_chemin(val, n, compteur, fonction_exploration):
    if convertir_entier(val) > n:
        return compteur
    if contient_3_5_7(val):
        compteur[0] += 1
    fonction_exploration(val, n, compteur)
    return compteur

def explorer_753(num, n, compteur):
    b = obtenir_chiffre_3(num)
    c = obtenir_chiffre_5(num)
    d = obtenir_chiffre_7(num)
    traiter_chemin(b, n, compteur, explorer_753)
    traiter_chemin(c, n, compteur, explorer_753)
    traiter_chemin(d, n, compteur, explorer_753)

def afficher_compteur(compteur):
    print(compteur[0])

def main():
    n = lire_entier()
    sitigosan_list = generer_liste_sitigosan()
    compteur = [initialiser_compteur()]
    if verifier_n_minimum(n):
        afficher_zero()
        fermer_programme()
    explorer_753('', n, compteur)
    afficher_compteur(compteur)

main()