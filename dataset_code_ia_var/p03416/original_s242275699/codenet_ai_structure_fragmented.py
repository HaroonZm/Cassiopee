def lire_entree():
    return input()

def splitter_entree(entree):
    return entree.split()

def convertir_en_int(liste):
    return list(map(int, liste))

def extraire_bornes(valeurs):
    return valeurs[0], valeurs[1]

def generer_intervalle(debut, fin):
    return range(debut, fin + 1)

def convertir_en_str(valeur):
    return str(valeur)

def est_palindrome(chaine):
    return chaine == chaine[::-1]

def incrementer(valeur):
    return valeur + 1

def compter_palindromes(debut, fin):
    num = 0
    intervalle = generer_intervalle(debut, fin)
    for i in intervalle:
        chaine = convertir_en_str(i)
        if est_palindrome(chaine):
            num = incrementer(num)
    return num

def afficher_resultat(resultat):
    print(resultat)

def programme_principal():
    entree = lire_entree()
    parties = splitter_entree(entree)
    valeurs = convertir_en_int(parties)
    debut, fin = extraire_bornes(valeurs)
    resultat = compter_palindromes(debut, fin)
    afficher_resultat(resultat)

programme_principal()