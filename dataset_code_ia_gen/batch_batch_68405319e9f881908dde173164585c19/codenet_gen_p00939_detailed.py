from functools import lru_cache

# On reçoit en entrée une séquence de chiffres s (string)
s = input().strip()
n = len(s)
digits = list(map(int, s))

# Pré-calcul de la valeur entière de la séquence
def int_value(seq):
    val = 0
    for d in seq:
        val = val * 10 + d
    return val

target_sum = sum(digits)
# Comme prod peut devenir très grand, on travaille avec int directement
target_prod = 1
for d in digits:
    target_prod *= (d + 1)
target_int = int_value(digits)

# On va compter le nombre de séquences t = t1t2...tn tels que
# t < s dans l'ordre défini : soit sum(t) < sum(s)
# soit sum(t) = sum(s) et prod(t) < prod(s)
# soit sum(t) = sum(s), prod(t) = prod(s) et int(t) < int(s)

# Pour éviter d'exploser l'état de prod(t) (car max prod peut être immense pour n=14),
# on utilise une astuce : on factorise le produit en base 1-10,
# ici on garde le produit exact car on peut le comparer directement (entier lange)
# Mais pour économiser de la mémoire on utilise un cache avec max taille

@lru_cache(None)
def dp(pos, sum_so_far, prod_so_far, is_less):
    # pos : position actuel (0..n)
    # sum_so_far : somme des chiffres jusqu'à pos-1 (max 9*14=126)
    # prod_so_far : produit des (d_i+1)
    # is_less : booléen si on a déjà pris un chiffre strictement inférieur à s[pos-1]
    if pos == n:
        # On a construit une séquence t complète de longueur n
        # On compte ce t ssi t < s selon l'ordre - mais on a pris soin de ne compter que ceux < s
        # Ici le compte est implicite dans la construction.
        # On compte 1 pour chaque séquence rencontrée (parce qu'on ne construit que < s)
        return 1

    res = 0
    limit = digits[pos] if not is_less else 9  # si is_less=False on ne peut pas dépasser digits[pos]
    # On masque la condition is_less qui 
    for d in range(limit + 1):
        new_sum = sum_so_far + d
        # On peut faire un branche mémoire
        # Si new_sum > target_sum, alors sum(t)>sum(s), donc t > s pour ordre => pas compte
        if new_sum > target_sum:
            # On ne compte pas car condition 1 échoue (on veut sum(t)<sum(s))
            # sauf cas égal, on continue pour égal uniquement
            continue

        new_prod = prod_so_far * (d + 1)
        # Si new_sum < target_sum alors forcément t < s (condition 1)
        # On peut donc prendre tous les d sauf limite imposée par is_less si is_less est False
        if new_sum < target_sum:
            # Peut continuer librement, is_less devient True car somme plus faible < sum(s)
            # donc t < s et on peut mettre is_less=True
            res += dp(pos + 1, new_sum, new_prod, True)
        else:
            # new_sum == target_sum, il faut comparer le produit
            if new_prod < target_prod:
                # prod(t) < prod(s) donc t < s
                res += dp(pos + 1, new_sum, new_prod, True)
            elif new_prod == target_prod:
                # prod égale - on utilise int numérique
                # Il faut comparer la séquence construite t avec s
                # On détermine si déjà on est strictement inférieur au préfixe s
                # ou égal encore
                # condition is_less qui indique si on est déjà inférieur strict
                # ici on rajoute la contrainte int(t) < int(s)
                # on peut gérer en utilisant is_less statut aussi.
                # Mais pas encore décidé car on construit le nombre pas directement.
                # On suit l'ordre lex de la séquence numérique (int)
                # Si d < digits[pos], alors on prend t < s assuré
                # Si d == digits[pos], alors on garde is_less = is_less
                # Si d > digits[pos], impossible car limit = digits[pos] si is_less=False

                next_is_less = is_less or (d < digits[pos])
                res += dp(pos + 1, new_sum, new_prod, next_is_less)
            else:
                # prod(t) > prod(s) => t > s
                # on arrête cette branche car elle ne compte pas
                continue

    return res

# On calcule donc le nombre de séquences t < s selon l'ordre défini
count_less = dp(0, 0, 1, False)

print(count_less)