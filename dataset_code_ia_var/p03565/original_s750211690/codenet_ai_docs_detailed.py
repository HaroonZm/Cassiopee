def inpl():
    """
    Lit une ligne depuis l'entrée standard, découpe la chaîne selon les espaces et convertit chaque élément en int.
    Retourne la liste des entiers.
    """
    return list(map(int, input().split()))

# Lecture de la chaîne source contenant potentiellement des '?'
Sd = input()
# Lecture de la chaîne cible à essayer de placer dans Sd
T = input()

def match(L):
    """
    Vérifie si une sous-chaîne L peut être remplacée par la chaîne T
    en respectant les caractères préexistants et les jokers '?'
    
    Args:
        L (str): Sous-chaîne de la chaîne source Sd de la même longueur que T

    Returns:
        bool: True si L peut être remplacée par T, False sinon
    """
    for l, t in zip(L, T):
        if l == "?":
            # Le caractère joker peut correspondre à n'importe quel caractère
            continue
        else:
            if l != t:
                # Si le caractère diffère et n'est pas '?', ce n'est pas une correspondance valide
                return False
            # Si le caractère correspond, poursuivre
    return True

# Liste pour stocker toutes les chaînes candidates valides
res = []

# Parcours tous les indices possibles pour insérer la chaîne T dans Sd,
# du dernier emplacement valide vers le premier (afin de privilégier la droite)
for i in range(len(Sd) - len(T) + 1)[::-1]:
    # Vérifie si l'emplacement à partir de i permet de placer T en respectant les contraintes
    if match(Sd[i:i+len(T)]):
        # Reconstruit une version potentielle de Sd avec T insérée à la position i
        # Remplace tous les '?' restants par 'a' pour obtenir le plus petit lexicographiquement
        candidate = (Sd[:i] + T + Sd[i+len(T):]).replace("?", "a")
        res.append(candidate)

# S'il existe des candidats valides, affiche le plus petit d'entre eux selon l'ordre lexicographique
if len(res):
    print(sorted(res)[0])
else:
    # Sinon, affiche "UNRESTORABLE" pour signaler l'impossibilité de restauration
    print("UNRESTORABLE")