def lire_entree():
    return input()

def splitter_entree(entree):
    return entree.split()

def convertir_entree(liste):
    return list(map(int, liste))

def assigner_valeurs(liste):
    return liste[0], liste[1], liste[2], liste[3]

def trouver_max(a, b, c, d):
    return max(a, b, c, d)

def trouver_min(a, b, c, d):
    return min(a, b, c, d)

def calculer_tuyoi(max_val, min_val):
    return max_val + min_val

def somme_totale(a, b, c, d):
    return a + b + c + d

def calculer_res(totale, tuyoi):
    return totale - 2 * tuyoi

def valeur_absolue(valeur):
    return abs(valeur)

def afficher_resultat(resultat):
    print(resultat)

def main():
    entree = lire_entree()
    splitee = splitter_entree(entree)
    int_liste = convertir_entree(splitee)
    a, b, c, d = assigner_valeurs(int_liste)
    max_val = trouver_max(a, b, c, d)
    min_val = trouver_min(a, b, c, d)
    tuyoi = calculer_tuyoi(max_val, min_val)
    totale = somme_totale(a, b, c, d)
    res = calculer_res(totale, tuyoi)
    resultat = valeur_absolue(res)
    afficher_resultat(resultat)

main()