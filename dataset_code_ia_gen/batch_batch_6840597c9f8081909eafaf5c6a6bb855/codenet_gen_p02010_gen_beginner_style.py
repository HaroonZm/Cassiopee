N = int(input())
S = input()

# On va essayer toutes les nouvelles chaînes possibles en modifiant les caractères un par un,
# mais ce serait trop long pour 1000 caractères, donc on fait une approche naïve :

# L'idée simple pour un débutant :
# - On vérifie toutes les combinaisons possibles où on remplace tous les '+' invalides et les chiffres invalides.
# - On teste seulement des formules avec un certain nombre de '+' placés (entre 0 et len(S)-1)
# - Pour simplifier, on va essayer de générer une formule valide en remplaçant tous les caractères un par un,
#   en testant pour chaque position s'il vaut mieux mettre un chiffre (différent de '+')
#   ou un '+' s'il n'est pas en début ou fin et ne crée pas deux '+' consécutifs.
# - Ensuite on calcule si la somme est <= N.
# - On conserve le minimum de remplacements.

# Comme solution simplifiée, on va :
# 1. Générer toutes les positions possibles pour les '+'s (de 0 à un maximum limité)
# 2. Autour de ces positions, générer les nombres correspondants
# 3. Calculer les remplacements nécessaires
# 4. Vérifier validité et somme

# Puisqu'il s'agit d'un code "débutant" et non optimal, on limite le nombre maximum de '+' à 5 pour éviter explosion combinatoire.

from itertools import combinations

def is_valid_number(num_str):
    # Pas de leading zero sauf si c'est "0"
    return len(num_str) == 1 or (num_str[0] != '0')

def sum_parts(parts):
    s = 0
    for p in parts:
        if not is_valid_number(p):
            return None
        s += int(p)
    return s

def cost_of_replacement(orig, new):
    cost = 0
    for o,nc in zip(orig,new):
        if o != nc:
            cost += 1
    return cost

L = len(S)
min_replacement = -1

# Limiter max + à 5 pour la simplicité et éviter explosion combinatoire
max_plus = min(5, L-1)

for plus_count in range(max_plus+1):
    # récupérer toutes les positions possibles du '+' (indices où on place("+"))
    for plus_pos in combinations(range(1,L), plus_count): # pas en début
        # création d'une formule selon la position des '+'
        parts = []
        prev = 0
        for ppos in plus_pos:
            parts.append(S[prev:ppos])
            prev = ppos
        parts.append(S[prev:L])

        # On va modifier chaque partie pour qu'elle soit un nombre valide (pas de leading zero sauf '0', chiffres seuls)
        # pour chaque partie, si premier char pas chiffre ou '0' illégal, on remplace par '1' ...
        valid_parts = []
        part_replacement_cost = 0
        valid = True
        for part in parts:
            # On va forcer la partie à être un nombre valide, en modifiant le moins possible
            if len(part)==0:
                valid = False
                break
            chars = list(part)
            # Première lettre doit être chiffre non zero ou '0' si partie simple
            # On choisit un chiffre possible minimisant la modification
            min_cost = None
            best_num = None
            for d in '0123456789':
                if d == '0' and len(part) >1:
                    # leading zero interdit
                    continue
                c = 0
                if chars[0]!=d:
                    c+=1
                # pour le reste des chiffres
                for i in range(1,len(part)):
                    if not chars[i].isdigit():
                        # On remplace par '0' (arbitraire)
                        c+=1
                # On regarde aussi si on modifie les autres chiffres (sauf premier)
                for i in range(1,len(part)):
                    if chars[i] != '0':
                        c += 1 if chars[i] != '0' else 0
                # en fait on remplace tous sauf premier par '0'
                # correction : on peut garder les chiffres s'ils sont déjà chiffres. limite naïf on remplace par 0 si pas chiffre
                # On va simplifier : remplacer tout sauf premier par '0'
                # Donc on compte combien sont modifiés
                mod_rest = 0
                for i in range(1,len(part)):
                    if not chars[i].isdigit():
                        mod_rest +=1
                    else:
                        if chars[i]!='0':
                            mod_rest +=1
                c = (1 if chars[0]!=d else 0) + mod_rest
                if (min_cost is None) or (c<min_cost):
                    min_cost = c
                    best_num = d + '0' * (len(part)-1)
            if best_num is None:
                valid = False
                break
            part_replacement_cost += min_cost
            valid_parts.append(best_num)
        if not valid:
            continue
        # On vérifie que la positions des '+' est ok (pas + au début ou fin et pas ++)
        # Dans cette construction elle ne le sera pas puisque plus_pos dans 1..L-1 et pas consécutifs (car combinaisons).
        # En plus on ne modifie pas les + positions ici, mais S peut avoir + ou non
        # On ajoute aussi le replacement des + à la position plus_pos
        formula_repl_cost = 0
        # On met la nouvelle formule
        # On reconstruit la formule avec les meilleurs parts et + aux positions plus_pos
        new_formula = [''] * L
        for i in range(L):
            new_formula[i] = '0'  # initial placeholder
        # On remplit les parts
        pos = 0
        for part in valid_parts:
            for c in part:
                new_formula[pos] = c
                pos+=1
            if pos < L:
                new_formula[pos] = '+'
                pos+=1
        # Si on a mis un + après dernier, on enlève
        if pos > L:
            continue
        # si pos < L, on remplit le reste par chiffres '0'
        for i in range(pos,L):
            new_formula[i] = '0'
        new_formula_str = ''.join(new_formula[:L]).rstrip('+')
        # calcul du coût de replacement dans la chaîne finale (on compte chaque différence)
        repl_cost = 0
        # remplacer les positions de '+' selon plus_pos, sinon chiffre
        # pour la solution "débutante" on va comparer char par char avec le "new_formula_str"
        # On fait simple : on crée la formule exacte avec plus_pos :
        #  - On marque les positions des '+' en plus_pos
        #  - entre on met les chiffres construits
        # En fait code est un peu confus, on simplifie :
        # reconstruire la formule avec valid_parts et '+'
        built_form = ''
        for i, part in enumerate(valid_parts):
            built_form += part
            if i < len(valid_parts)-1:
                built_form += '+'
        if len(built_form)!=L:
            # Il faut modifier la taille, donc pas valide : car on ne change pas la taille
            if len(built_form) > L:
                continue
            # sinon on complète par '0' pour avoir la même taille
            built_form = built_form + '0'*(L-len(built_form))
        # compter remplacement
        repl_cost = 0
        for i in range(L):
            if S[i] != built_form[i]:
                repl_cost += 1
        # vérifier validité
        # on a déjà validé valid_parts
        # somme
        s = 0
        for vp in valid_parts:
            s += int(vp)
        if s <= N:
            if min_replacement == -1 or repl_cost < min_replacement:
                min_replacement = repl_cost

print(min_replacement)