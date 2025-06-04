from collections import defaultdict, Counter

def lire_liste_entiers_depuis_input():
    return list(map(int, input().split()))

nombre_entiers, modulo = lire_liste_entiers_depuis_input()
liste_entiers = sorted(lire_liste_entiers_depuis_input())

comptage_entiers = Counter(liste_entiers)

effectifs_par_reste = defaultdict(int)
demi_paires_par_reste = defaultdict(int)

for valeur, nombre_occur in comptage_entiers.items():
    reste = valeur % modulo
    effectifs_par_reste[reste] += nombre_occur
    demi_paires_par_reste[reste] += nombre_occur // 2

total_paires = effectifs_par_reste[0] // 2

for increment in range(1, modulo):
    complementaire = modulo - increment
    if increment < complementaire:
        nombre_paires_possibles = min(effectifs_par_reste[increment], effectifs_par_reste[complementaire])
        nombre_demi_paires = (
            min((effectifs_par_reste[increment] - nombre_paires_possibles) // 2, demi_paires_par_reste[increment]) +
            min((effectifs_par_reste[complementaire] - nombre_paires_possibles) // 2, demi_paires_par_reste[complementaire])
        )
        total_paires += nombre_paires_possibles + nombre_demi_paires
    elif increment == complementaire:
        total_paires += effectifs_par_reste[increment] // 2
    else:
        break

print(total_paires)