# Programme pour construire un index de livre à partir d'une liste de paires (mot, numéro de page)

# Approche :
# 1. Lire les entrées jusqu'à la fin (ou jusqu'à 100 entrées).
# 2. Pour chaque paire (mot, page), stocker le numéro de page dans une structure de données associée au mot.
# 3. Éviter les doublons de pages pour un même mot.
# 4. Une fois la lecture terminée, trier les mots par ordre alphabétique.
# 5. Pour chaque mot, trier la liste des pages et l'afficher.

# Remarque : le programme suppose que les entrées sont fournies via l'entrée standard (stdin).

import sys

def main():
    # Dictionnaire pour stocker les pages par mot
    index = {}

    # Lecture des entrées
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue  # Ignore les lignes vides
        # Séparer en mot et page
        parts = line.split()
        if len(parts) != 2:
            continue  # Ignore les lignes mal formées
        word, page_str = parts
        # Vérifier contraintes
        if len(word) > 30:
            continue  # Ignore le mot si trop long
        try:
            page = int(page_str)
        except ValueError:
            continue  # Ignore si la page n'est pas un entier valide
        if page > 1000 or page < 1:
            continue  # Ignore les numéros de pages invalides

        # Stockage dans le dictionnaire
        if word not in index:
            index[word] = set()  # Utilisation d'un set pour éviter les doublons de pages
        index[word].add(page)

    # Affichage des résultats
    for word in sorted(index.keys()):
        pages = sorted(index[word])
        print(word)
        print(' '.join(str(p) for p in pages))

if __name__ == "__main__":
    main()