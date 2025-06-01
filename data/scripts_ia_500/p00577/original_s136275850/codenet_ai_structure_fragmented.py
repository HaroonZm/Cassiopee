def lire_entier():
    return int(input())

def lire_liste_caracteres():
    return input().split()

def extraire_premier_element(liste):
    return liste[0]

def convertir_chaine_en_liste_caracteres(chaine):
    liste = []
    for caractere in chaine:
        liste.append(caractere)
    return liste

def convertir_caracteres_en_entiers(liste_caracteres):
    liste_entiers = []
    for c in liste_caracteres:
        if c == 'O':
            liste_entiers.append(1)
        else:
            liste_entiers.append(0)
    return liste_entiers

def compter_paires_suivantes(liste_entiers, taille):
    compteur = 0
    indice = 0
    while indice < taille - 1:
        if liste_entiers[indice] + liste_entiers[indice + 1] == 1:
            compteur += 1
            indice += 2
        else:
            indice += 1
    return compteur

def main():
    n = lire_entier()
    liste = lire_liste_caracteres()
    chaine = extraire_premier_element(liste)
    liste_caracteres = convertir_chaine_en_liste_caracteres(chaine)
    liste_entiers = convertir_caracteres_en_entiers(liste_caracteres)
    resultat = compter_paires_suivantes(liste_entiers, n)
    print(resultat)

main()