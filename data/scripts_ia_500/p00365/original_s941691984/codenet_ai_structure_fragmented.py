def lire_entiers():
    return map(int, input().split())

def conditions_initiales(b, e, c, f):
    return b == e and c == f

def calcul_premier_resultat(a, d):
    return abs(a - d)

def comparer_a_et_d(a, d):
    if a > d:
        return "a_sup_d"
    elif a < d:
        return "a_inf_d"
    else:
        return "a_egal_d"

def calculer_num_nu(a_d_relation, b, c, e, f):
    if a_d_relation == "a_sup_d":
        num = 100 * b + c
        nu = 100 * e + f
    elif a_d_relation == "a_inf_d":
        num = 100 * e + f
        nu = 100 * b + c
    else:
        num = None
        nu = None
    return num, nu

def comparaison_finale(num, nu, a, d):
    if num is None or nu is None:
        return 1
    elif num > nu:
        return abs(a - d) + 1
    else:
        return abs(a - d)

def afficher_resultat(valeur):
    print(valeur)

def main():
    a, b, c = lire_entiers()
    d, e, f = lire_entiers()
    if conditions_initiales(b, e, c, f):
        afficher_resultat(calcul_premier_resultat(a, d))
        return
    a_d_relation = comparer_a_et_d(a, d)
    if a_d_relation == "a_egal_d":
        afficher_resultat(1)
        return
    num, nu = calculer_num_nu(a_d_relation, b, c, e, f)
    resultat = comparaison_finale(num, nu, a, d)
    afficher_resultat(resultat)

main()