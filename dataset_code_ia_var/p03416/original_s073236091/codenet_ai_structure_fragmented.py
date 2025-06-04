def lire_entrees():
    return input()

def convertir_entrees(entrees):
    return map(int, entrees.split())

def obtenir_intervalle(a, b):
    return range(a, b+1)

def convertir_en_chaine(n):
    return str(n)

def longueur_chaine(s):
    return len(s)

def moitie_chaine(l):
    return l // 2

def sous_chaine_debut(s, hl):
    return s[:hl]

def sous_chaine_fin_inverse(s, hl):
    return s[-1:-1-hl:-1]

def sont_egales(s1, s2):
    return s1 == s2

def traiter_nombre(i):
    s = convertir_en_chaine(i)
    l = longueur_chaine(s)
    hl = moitie_chaine(l)
    debut = sous_chaine_debut(s, hl)
    fin = sous_chaine_fin_inverse(s, hl)
    return sont_egales(debut, fin)

def compter_nombres_palindromiques(a, b):
    compteur = 0
    for i in obtenir_intervalle(a, b):
        if traiter_nombre(i):
            compteur += 1
    return compteur

def afficher_resultat(res):
    print(res)

def main():
    entrees = lire_entrees()
    a, b = convertir_entrees(entrees)
    resultat = compter_nombres_palindromiques(a, b)
    afficher_resultat(resultat)

main()