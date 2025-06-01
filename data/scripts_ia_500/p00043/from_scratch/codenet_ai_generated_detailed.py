import sys
from collections import Counter

def can_form_melds(counter):
    """
    Cette fonction vérifie si l'ensemble restant de cartes (représenté par un compteur) 
    peut être entièrement divisé en groupes de 3 cartes, 
    chaque groupe étant soit un triplet (3 cartes identiques) 
    soit une séquence consécutive de 3 cartes distinctes.
    """
    # copie pour ne pas modifier l'original
    c = counter.copy()
    for num in range(1, 10):
        # tant que c[num] > 0, on essaie de former des groupements
        while c[num] > 0:
            # essayer d'abord de former un triplet
            if c[num] >= 3:
                c[num] -= 3
            # sinon essayer une séquence num, num+1, num+2
            elif num <= 7 and c[num+1] > 0 and c[num+2] > 0:
                c[num] -= 1
                c[num+1] -= 1
                c[num+2] -= 1
            else:
                # ni triplet ni séquence possible ici
                return False
    return True

def can_complete_puzzle(counter):
    """
    Vérifie si avec la distribution des cartes dans 'counter' (14 cartes),
    on peut satisfaire la condition du puzzle :
    - un "pair" (deux mêmes chiffres)
    - et 4 groupes de 3 chiffres soit triplets soit séquences consécutives
    """
    # on recherche la paire (deux mêmes cartes)
    for num in range(1, 10):
        if counter[num] >= 2:
            # tenter de retirer la paire
            c = counter.copy()
            c[num] -= 2
            # vérifier si le reste peut être formé en 4 groupes de 3
            if can_form_melds(c):
                return True
    return False

def process_line(line):
    # compter les chiffres donnés
    digits = list(map(int, list(line.strip())))
    counter = Counter(digits)
    result = []
    for add_num in range(1, 10):
        # vérifier la limite 4 occurrences
        if counter[add_num] == 4:
            continue # on ne peut pas ajouter ce numéro
        c = counter.copy()
        c[add_num] += 1
        # vérifier puzzle complétable
        if can_complete_puzzle(c):
            result.append(add_num)
    if not result:
        print(0)
    else:
        print(" ".join(map(str, result)))

def main():
    input_lines = [l.strip() for l in sys.stdin if l.strip()]
    for line in input_lines:
        process_line(line)

if __name__ == "__main__":
    main()