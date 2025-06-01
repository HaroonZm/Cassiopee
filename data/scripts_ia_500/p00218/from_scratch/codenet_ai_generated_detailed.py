# Solution pour le problème de クラス分け (classement des élèves) en Python
# Ce script lit plusieurs jeux de données jusqu'à ce qu'une ligne "0" soit rencontrée,
# puis pour chaque élève dans chaque dataset, calcule la classe (A, B, ou C) selon les règles données.

def determine_class(pm, pe, pj):
    """
    Détermine la classe d'un élève selon ses notes en mathématiques (pm),
    anglais (pe) et japonais (pj).

    Règles (ordre de priorité décroissant) :
    - Si une note est 100 => Classe A
    - Si la moyenne de math et anglais >= 90 => Classe A
    - Si la moyenne des 3 matières >= 80 => Classe A
    - Si la moyenne des 3 matières >= 70 => Classe B
    - Si la moyenne des 3 matières >= 50 et math ou anglais >= 80 => Classe B
    - Sinon => Classe C
    """
    # Vérification si 100 dans une matière
    if pm == 100 or pe == 100 or pj == 100:
        return 'A'

    avg_me = (pm + pe) / 2 # moyenne math et anglais
    avg_all = (pm + pe + pj) / 3 # moyenne de toutes les matières

    if avg_me >= 90:
        return 'A'
    if avg_all >= 80:
        return 'A'
    if avg_all >= 70:
        return 'B'
    if avg_all >= 50 and (pm >= 80 or pe >= 80):
        return 'B'
    # Sinon, classe C
    return 'C'


def main():
    import sys

    # Lecture ligne par ligne du stdin
    lines = sys.stdin.read().strip().split('\n')
    index = 0

    # On parcourt toutes les datasets jusqu'à rencontrer "0"
    while True:
        if index >= len(lines):
            break
        n = lines[index].strip()
        index += 1
        if n == '0':
            # Fin des données
            break

        n = int(n)
        # Pour chaque élève du dataset
        for _ in range(n):
            # Lire la ligne des 3 notes et convertir en entiers
            pm_str, pe_str, pj_str = lines[index].strip().split()
            index += 1
            pm, pe, pj = int(pm_str), int(pe_str), int(pj_str)

            # Calculer la classe et afficher
            c = determine_class(pm, pe, pj)
            print(c)

if __name__ == "__main__":
    main()