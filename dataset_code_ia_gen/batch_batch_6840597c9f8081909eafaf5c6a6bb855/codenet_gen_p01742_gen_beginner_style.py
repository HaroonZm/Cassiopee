MOD = 10**9 + 7

n = int(input())
s = [input() for _ in range(n)]

# Pour comparer deux mots en tenant compte des '?'
# Renvoie -1 si a < b, 0 si indéterminé, 1 si a > b
def cmp_words(a, b):
    la, lb = len(a), len(b)
    for i in range(min(la, lb)):
        ca, cb = a[i], b[i]
        if ca != '?' and cb != '?':
            if ca < cb:
                return -1
            elif ca > cb:
                return 1
        elif ca != '?' and cb == '?':
            # cb peut être n'importe quelle lettre, on ne sait pas exactement
            continue
        elif ca == '?' and cb != '?':
            continue
        else:
            # les deux sont '?'
            continue
    if la < lb:
        return -1
    elif la > lb:
        return 1
    else:
        return 0

# Fonction récursive pour compter les façons de remplacer les '?' 
# dans s[idx] à partir des bornes inf et sup (limites lex) données par les mots précédents et suivants
def count_ways(idx, prefix):
    if idx == n:
        return 1
    cur = list(s[idx])
    prev = prefix
    ways = 0

    # On va essayer toutes les possibilités pour le mot cur en remplaçant les '?'
    # On le fait par backtracking simple

    # On génère tous les mots possibles pour cur compatibles avec les contraintes lex ordre :
    # prev < cur < s[idx+1] (ou infini si idx+1 == n)
    # Comme c'est compliqué, on essaye de générer mot par mot en respectant lex ordre par rapport au prev et next si possible

    # On récupère les bornes lex pour cur :
    # lower_bound = prev < cur
    # upper_bound = s[idx+1] si idx+1 < n sinon None

    lower = prev
    upper = s[idx+1] if idx +1 < n else None

    # On va générer tous les mots possibles en remplaçant '?'
    # On fait un backtracking en comparant avec lower et upper

    def backtrack(pos, word, lower_fixed, upper_fixed):
        # pos: position actuelle
        # word: mot en construction
        # lower_fixed: indique si on a déjà dépassé lower (donc plus besoin de respecter strictement lower)
        # upper_fixed: idem pour upper
        if pos == len(cur):
            # mot complet, on doit vérifier la longueur par rapport à bounds
            # mais en fait on a controlé par la comparaison dans backtrack donc ok
            ways = 1
            return ways
        ways = 0
        c = cur[pos]

        low_c = lower[pos] if pos < len(lower) else None
        high_c = upper[pos] if upper and pos < len(upper) else None

        for chnum in range(ord('a'), ord('z')+1):
            ch = chr(chnum)
            # vérifier que ch respecte

            # si c n'est pas '?' on impose ch == c
            if c != '?' and ch != c:
                continue

            # condition lower_fixed
            if not lower_fixed:
                if low_c is not None:
                    if ch < low_c:
                        # ch trop petit
                        continue
                    elif ch > low_c:
                        next_lower_fixed = True
                    else:
                        next_lower_fixed = False
                else:
                    next_lower_fixed = True
            else:
                next_lower_fixed = True

            # condition upper_fixed
            if not upper_fixed:
                if high_c is not None:
                    if ch > high_c:
                        continue
                    elif ch < high_c:
                        next_upper_fixed = True
                    else:
                        next_upper_fixed = False
                else:
                    next_upper_fixed = True
            else:
                next_upper_fixed = True

            ways += backtrack(pos+1, word+ch, next_lower_fixed, next_upper_fixed)
        return ways % MOD

    # lower doit être strictement inférieur à cur, donc au premier endroit où differe on veut ch > lower[pos]
    # upper doit être strictement superieur a cur, donc au premier endroit differe ch < upper[pos]
    # Avec les flags lower_fixed et upper_fixed on contrôle la stricte supériorité lex
    # Pour le lower on veut cur > lower donc au premier caractère différent, ch > low_c
    # Pour le upper on veut cur < upper donc au premier caractère différent, ch < high_c

    # Pour le first char on doit s'assurer strictement supérieur à lower et strictement inférieur à upper
    # Cette gestion dans backtrack.

    #Mais on doit gérer la stricte comparaison. Ici on a ≤ dans comparaisons mais on veut < strict

    # On modifie le backtrack pour gérer cela :

    # On modifie les flags lower_strict_ok, upper_strict_ok. Au début, les deux à False.

    def backtrack2(pos, lower_strict_ok, upper_strict_ok):
        if pos == len(cur):
            # pour la longueur des mots, pour l'ordre lex :
            # si pas strictement plus grand que lower et pas strictement plus petit que upper, on rejete
            if not lower_strict_ok:
                return 0
            if upper is not None and not upper_strict_ok:
                return 0
            return 1
        ways = 0
        c = cur[pos]

        low_c = lower[pos] if pos < len(lower) else None
        high_c = upper[pos] if upper and pos < len(upper) else None

        for chnum in range(ord('a'), ord('z')+1):
            ch = chr(chnum)
            if c != '?' and ch != c:
                continue
            # vérifier lower
            if low_c is not None:
                if lower_strict_ok:
                    # plus besoin de comparer
                    pass
                else:
                    if ch < low_c:
                        continue
                    elif ch > low_c:
                        n_lower_strict_ok = True
                    else:
                        n_lower_strict_ok = False
            else:
                # lower pas définie ici, considéré ok
                n_lower_strict_ok = True

            # vérifier upper
            if high_c is not None:
                if upper_strict_ok:
                    pass
                else:
                    if ch > high_c:
                        continue
                    elif ch < high_c:
                        n_upper_strict_ok = True
                    else:
                        n_upper_strict_ok = False
            else:
                n_upper_strict_ok = True

            ways += backtrack2(pos+1, n_lower_strict_ok, n_upper_strict_ok)
            ways %= MOD

        return ways

    # pour idx==0, pas de lower, donc lower = ""
    # on met lower = "" si idx==0
    lb = s[idx-1] if idx > 0 else ""
    ways = backtrack2(0, False, False)
    return ways % MOD

res = 1
for i in range(n):
    res = (res * count_ways(i, s[i-1] if i > 0 else "")) % MOD
print(res)