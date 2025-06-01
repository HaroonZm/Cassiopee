import sys
def lire_entree():
    return sys.stdin

def traiter_ligne(ligne):
    return list(map(int, ligne.split()))

def creer_ensemble_a_b_c(a, b, c):
    return {a, b, c}

def creer_ensemble_range(a, b):
    return set(range(1, 21 - a - b))

def difference_ensembles(ensemble1, ensemble2):
    return ensemble1 - ensemble2

def taille_ensemble(ensemble):
    return len(ensemble)

def verifier_condition(taille):
    return taille < 3.5

def choisir_resultat(condition):
    return ['YES', 'NO'][condition]

def afficher_resultat(resultat):
    print(resultat)

def main():
    for x in lire_entree():
        a, b, c = traiter_ligne(x)
        ensemble_abc = creer_ensemble_a_b_c(a, b, c)
        ensemble_range = creer_ensemble_range(a, b)
        difference = difference_ensembles(ensemble_range, ensemble_abc)
        taille = taille_ensemble(difference)
        condition = verifier_condition(taille)
        resultat = choisir_resultat(condition)
        afficher_resultat(resultat)

main()