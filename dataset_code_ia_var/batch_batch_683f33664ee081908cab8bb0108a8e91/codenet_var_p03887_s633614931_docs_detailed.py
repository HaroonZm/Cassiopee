def fast_pow(x, y):
    """
    Calcule la puissance rapide de x à la puissance y sous le modulo MOD.
    Cette méthode exponentie rapidement grâce à l'exponentiation binaire.

    Args:
        x (int): La base.
        y (int): L'exposant.

    Returns:
        int: (x ^ y) % MOD
    """
    if y == 0:
        return 1
    # Exponentiation binaire : divise le problème par 2 à chaque étape
    p = fast_pow(x, y // 2) % MOD
    p = p * p % MOD
    if y % 2:
        p = p * x % MOD
    return p

def inverse(k):
    """
    Calcule l'inverse modulaire de k sous le modulo MOD.
    Utilise le petit théorème de Fermat supposant que MOD est premier.

    Args:
        k (int): Le nombre à inverser.

    Returns:
        int: L'inverse de k modulo MOD.
    """
    return fast_pow(k, MOD - 2)

def comb(n, k):
    """
    Calcule le coefficient binomial C(n, k) modulo MOD.

    Args:
        n (int): Le nombre d'éléments totaux.
        k (int): Le nombre d'éléments à choisir.

    Returns:
        int: Le coefficient binomial C(n, k) mod MOD.
    """
    if k < 0 or k > n:
        return 0
    # Utilise les pré-calculs de FACT et INVERSE_FACT pour calculer C(n, k)
    return FACT[n] * INVERSE_FACT[n - k] % MOD * INVERSE_FACT[k] % MOD

# Modulo utilisé pour tous les calculs
MOD = 1000000007

# Lecture des quatre paramètres d'entrée
n, a, b, c = map(int, input().split())

# Pré-calcul des factorielles et factorielles inverses pour des calculs rapides
FACT = [0] * (n + 1)         # FACT[i] = i! % MOD
INVERSE_FACT = [0] * (n + 1) # INVERSE_FACT[i] = 1 / (i! % MOD)

FACT[0] = 1
INVERSE_FACT[0] = 1
for i in range(1, n + 1):
    FACT[i] = FACT[i - 1] * i % MOD
    INVERSE_FACT[i] = inverse(FACT[i])

# Variable pour stocker la réponse finale
ans = 0

# Si b n'est pas pair, le résultat est 0 (impossible)
if b % 2 != 0:
    print(0)
    exit()

# Parcourt toutes les combinaisons valides de y (sous-ensemble commun à a et c) et de z (multiplicité > 1 dans c)
for y in range(0, min(a + 1, c + 1)):
    # 'z' correspond au nombre d'éléments apports multiples dans la décomposition de c (par groupe de 3)
    for z in range(0, (c - y) // 3 + 1):
        x = a - y                          # Éléments propres à 'a'
        rest3 = c - y - 3 * z              # Reste à répartir au sein de 'c' après avoir retiré les groupes de y et de 3*z

        # Condition d'arrêt quand il reste un reste non nul à répartir alors que b = 0
        if b == 0 and rest3 != 0:
            continue

        # Nombre de façons d'organiser les x, y, z éléments (permutations avec répétition)
        cur_ans = FACT[x + y + z] * INVERSE_FACT[x] % MOD
        cur_ans = cur_ans * INVERSE_FACT[y] % MOD
        cur_ans = cur_ans * INVERSE_FACT[z] % MOD

        # Nombre de façons de répartir b / 2 éléments parmi x + y + z + 1 "boîtes" (combinaison avec répétitions)
        cur_ans = cur_ans * comb(x + y + z + 1 + b // 2 - 1, b // 2) % MOD

        # Façons de placer le reste des éléments rest3 dans b / 2 "boîtes"
        cur_ans = cur_ans * comb(b // 2 + rest3 - 1, rest3) % MOD

        # Ajout à la somme totale modulo MOD
        ans = (ans + cur_ans) % MOD

# Affichage de la réponse finale
print(ans)