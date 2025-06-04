mod = 10 ** 9 + 7  # Définition du modulo pour éviter les débordements dans les calculs

n = int(input())
H = list(map(int, input().split()))

def solve(h):
    """
    Calcule la valeur requise selon une logique dynamique basée sur la liste de hauteurs `h`.
    Les différentes parties du calcul dépendent de la configuration locale des hauteurs.

    Args:
        h (List[int]): Liste des hauteurs (sous-liste de la liste globale H, sans les '1').

    Returns:
        int: Le nombre total de façons possibles selon les règles données, modulo `mod`.
    """
    if not h:
        # Cas de base: Une séquence vide a une seule façon triviale
        return 1
    elif len(h) == 1:
        # Si une seule hauteur, le résultat est 2^hauteur (tous les sous-ensembles des étages)
        return pow(2, h[0], mod)
    
    N = len(h)  # Nombre d'éléments dans la sous-liste

    # Compression des valeurs de hauteur pour permettre une indexation efficace dans le dp
    a = [h[i] for i in range(N)]
    a = list(set(a))  # Éliminer les doublons
    a.sort()
    comp = {i: e+1 for e, i in enumerate(a)}  # Dictionnaire: hauteur -> index compressé (>0)
    data = {comp[e]: e for e in comp.keys()}  # Inverse: index compressé -> hauteur
    data[0] = 1  # Correction d'initialisation, utilisé comme valeur de base
    
    # Initialisation de la table de programmation dynamique
    # dp[i][j]: nombre de façons jusqu'à ième position avec hauteur index j
    dp = [[0 for _ in range(len(a)+1)] for _ in range(N)]
    
    # Initialisation de la première transition selon les relations de la séquence
    i = 0
    if h[i+1] >= h[i]:
        # Cas où la prochaine hauteur est plus grande ou égale
        id = comp[h[i]]
        id2 = comp[h[i+1]]
        for j in range(id, id2+1):
            dp[i][j] = 2  # Deux façons de construire cette configuration
        for j in range(0, id):
            dp[i][j] = 1  # Une seule façon pour les indices plus bas
    else:
        # Cas où la prochaine hauteur est plus petite
        id = comp[h[i+1]]
        for j in range(0, id):
            dp[i][j] = pow(2, h[i]-h[i+1], mod)
        dp[i][id] = 2 * (pow(2, h[i]-h[i+1], mod) - 1)
        dp[i][id] %= mod
        id2 = comp[h[i]]
        dp[i][id] += 2  # Ajoute 2 façons supplémentaires pour la configuration maximale
        dp[i][id] %= mod

    # Remplissage progressif de la DP pour chaque position dans la séquence
    for i in range(1, N-1):
        if h[i+1] >= h[i]:
            id = comp[h[i]]
            id2 = comp[h[i+1]]
            # Si la hauteur suivante est supérieure ou égale, multiplier par 2 pour les nouvelles options
            for j in range(id, id2+1):
                dp[i][j] = (2 * dp[i-1][id]) % mod
            # Les autres indices conservent leurs valeurs précédentes
            for j in range(0, id):
                dp[i][j] = dp[i-1][j]
        else:
            id = comp[h[i+1]]
            id2 = comp[h[i]]
            # Cas où la hauteur diminue
            for j in range(0, id):
                dp[i][j] = (pow(2, h[i]-h[i+1], mod) * dp[i-1][j]) % mod
            for j in range(id, id2):
                low = data[j]
                up = data[j+1] - 1
                dp[i][id] += dp[i-1][j] * pow(2, h[i]-up, mod) * (pow(2, up-low+1, mod)-1)
            dp[i][id] %= mod
            dp[i][id] += 2 * dp[i-1][id2]
            dp[i][id] %= mod

    # Calcul final de la réponse pour cette portion
    ans = 0
    id = comp[h[-1]]
    for i in range(0, id):
        low = data[i]
        up = data[i+1] - 1
        ans += dp[N-2][i] * pow(2, h[-1]-up, mod) * (pow(2, up-low+1, mod) - 1)
        ans %= mod
    ans += 2 * dp[N-2][id]
    ans %= mod
    return ans

# Prise en compte des portions séparées par les '1' dans H
ans = pow(2, H.count(1), mod)  # Chaque '1' offre 2 possibilités indépendantes

# Index de toutes les positions où la valeur est '1'
check = [i for i in range(n) if H[i] == 1]
# Créer des bornes de découpage de la liste principale H
check = [-1] + check + [n]

# Pour chaque sous-séquence comprise entre les '1', appliquer la fonction solve
for i in range(len(check)-1):
    l, r = check[i], check[i+1]
    ans *= solve(H[l+1:r])
    ans %= mod

print(ans)  # Affichage du résultat final