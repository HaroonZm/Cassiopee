def lire_lignes():
    return [input().split() for _ in range(6)]

def convertir_vers_entiers(lignes):
    return [list(map(int, ligne)) for ligne in lignes]

def trier_chacune(liste_de_listes):
    return [sorted(liste) for liste in liste_de_listes]

def trier_par_deuxieme_element(liste_de_listes):
    return sorted(liste_de_listes, key=lambda x: x[1])

def trier_par_premier_element(liste_de_listes):
    return sorted(liste_de_listes, key=lambda x: x[0])

def verifier_premiere_condition(a):
    return a[0] == a[1]

def verifier_deuxieme_condition(a):
    return a[2] == a[3]

def verifier_troisieme_condition(a):
    return a[4] == a[5]

def verifier_quatrieme_condition(a):
    return a[0][0] == a[2][0]

def verifier_cinquieme_condition(a):
    return a[0][1] == a[4][0]

def verifier_sixieme_condition(a):
    return a[2][1] == a[4][1]

def verifier_toutes_conditions(a):
    return (verifier_premiere_condition(a) and
            verifier_deuxieme_condition(a) and
            verifier_troisieme_condition(a) and
            verifier_quatrieme_condition(a) and
            verifier_cinquieme_condition(a) and
            verifier_sixieme_condition(a))

def afficher_resultat(condition):
    print("yes" if condition else "no")

def main():
    lignes_brutes = lire_lignes()
    lignes_int = convertir_vers_entiers(lignes_brutes)
    listes_triees = trier_chacune(lignes_int)
    listes_triees_1 = trier_par_deuxieme_element(listes_triees)
    listes_triees_2 = trier_par_premier_element(listes_triees_1)
    resultat = verifier_toutes_conditions(listes_triees_2)
    afficher_resultat(resultat)

main()