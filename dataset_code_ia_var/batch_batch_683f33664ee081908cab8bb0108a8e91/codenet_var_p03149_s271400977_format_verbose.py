import sys

def lire_entree_utilisateur():
    return sys.stdin.readline().strip()

liste_entiers_saisis_par_utilisateur = list(map(int, lire_entree_utilisateur().split()))

ensemble_attendu_nombres = {1, 9, 7, 4}

ensemble_nombres_utilisateur = set(liste_entiers_saisis_par_utilisateur)

if ensemble_nombres_utilisateur == ensemble_attendu_nombres:
    print("YES")
else:
    print("NO")