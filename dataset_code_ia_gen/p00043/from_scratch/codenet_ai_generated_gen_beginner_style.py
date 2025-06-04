def can_form_triplets(counts):
    # Retourne True si on peut partitionner les cartes en tris selon la règle (triplets identiques ou séquences)

    def backtrack(counts):
        # Trouve le prochain index avec count > 0
        for i in range(1, 10):
            if counts[i] > 0:
                break
        else:
            return True  # tous traités

        # Essayer triplet identique
        if counts[i] >= 3:
            counts[i] -= 3
            if backtrack(counts):
                counts[i] += 3
                return True
            counts[i] += 3

        # Essayer suite i, i+1, i+2 si possible
        if i <= 7 and counts[i] > 0 and counts[i + 1] > 0 and counts[i + 2] > 0:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            if backtrack(counts):
                counts[i] += 1
                counts[i+1] += 1
                counts[i+2] += 1
                return True
            counts[i] += 1
            counts[i+1] += 1
            counts[i+2] += 1
        return False

    return backtrack(counts[:])

def is_valid_combination(cards):
    # cards est une liste de 14 chiffres
    from collections import Counter

    counts = [0]*10
    for c in cards:
        counts[c] += 1
        if counts[c] > 4:  # max 4 même chiffre
            return False

    # On doit trouver une paire (deux cartes identiques)
    for i in range(1, 10):
        if counts[i] >= 2:
            counts[i] -= 2  # on réserve la paire
            # Vérifier si le reste peut se partitionner en 4 triplets
            if can_form_triplets(counts):
                counts[i] += 2
                return True
            counts[i] += 2
    return False

import sys

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    cards = list(map(int,list(line)))
    result = []

    for x in range(1,10):
        if cards.count(x) >= 4:
            # pas possible d'ajouter ce chiffre
            continue
        new_cards = cards + [x]
        if is_valid_combination(new_cards):
            result.append(str(x))
    if result:
        print(" ".join(result))
    else:
        print(0)