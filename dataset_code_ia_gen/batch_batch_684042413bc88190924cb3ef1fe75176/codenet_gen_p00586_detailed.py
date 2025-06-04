# Solution Python pour le problème "A + B Problem"
# L'approche :
# - Lire chaque ligne de l'entrée standard jusqu'à la fin de fichier (EOF)
# - Pour chaque ligne, extraire les deux entiers A et B
# - Calculer la somme A + B
# - Afficher la somme
# Les contraintes sont respectées car on n'a pas besoin d'aucune structure particulière, juste une lecture ligne par ligne.

import sys

def main():
    for line in sys.stdin:
        # Nettoyer la ligne pour éviter les problèmes d'espaces ou de retour à la ligne
        line = line.strip()
        if not line:
            continue
        # Extraire les deux entiers A et B
        parts = line.split()
        # On s'assure qu'on a bien deux éléments
        if len(parts) != 2:
            continue
        try:
            A = int(parts[0])
            B = int(parts[1])
        except ValueError:
            # Si la conversion échoue, on ignore la ligne
            continue
        # Calculer et afficher la somme
        print(A + B)

if __name__ == "__main__":
    main()