def combs_mod(n, k, mod):
    # Cette fonction calcule la liste des combinaisons modulo 'mod'.
    # Elle renvoie une liste 'ans' où ans[i] = nCi % mod, pour i allant de 0 à k inclus.
    
    # On crée une liste d'inverses modulaires de chaque entier de 1 à k inclus.
    # C'est nécessaire pour pouvoir diviser par i modulo 'mod'.
    # On initialise d'abord la liste avec des 1, taille k+1 car on part de 0 à k.
    inv = [1] * (k + 1)
    
    # On parcourt tous les entiers de 1 à k pour remplir la table des inverses.
    for i in range(1, k + 1):
        # pow(i, mod-2, mod) calcule l'inverse multiplicatif de i modulo 'mod' grâce au petit théorème de Fermat.
        inv[i] = pow(i, mod - 2, mod)
    
    # On prépare une liste pour stocker tous les coefficients binomiaux modulaires de 0 à k.
    ans = [1] * (k + 1)
    # nC0 = 1 donc ans[0] = 1 (déjà mis par l'initialisation).
    
    # On calcule chaque coefficient binomial nCi à partir de nC(i-1) (relation de récurrence).
    for i in range(1, k + 1):
        # On utilise la formule récurrente : nCi = nC(i-1) * (n + 1 - i) / i
        # On multiplie par l'inverse de i car la division n'existe pas directement en arithmétique modulaire.
        ans[i] = ans[i - 1] * (n + 1 - i) * inv[i] % mod
    
    # On retourne la liste complète des coefficients binomiaux modulo 'mod'.
    return ans

def solve():
    # Cette fonction résout le problème principal en utilisant combs_mod pour les nCr modulo 'mod'.
    
    # On définit un grand nombre premier comme mod, pour les opérations modulaires (utilisé dans beaucoup de problèmes de combinatoire).
    mod = 998244353
    
    # On lit deux entiers depuis l'entrée standard : N et K.
    # 'map' applique 'int' à chaque élément du résultat de split (découpage de la ligne d'entrée).
    N, K = map(int, input().split())
    
    # On initialise la réponse à 0.
    ans = 0
    
    # Si K < N, il ne peut pas y avoir de solution valide (condition spécifique au problème).
    if K < N:
        return ans
    
    # On pré-calcule tous les coefficients binomiaux nécessaires via combs_mod,
    # pour accélérer les calculs dans la prochaine boucle.
    com = combs_mod(K, K, mod)        # com[r] vaut KCr modulo mod, pour 0 <= r <= K
    com2 = combs_mod(K - 1, K - 1, mod)  # com2[r] vaut (K-1)Cr modulo mod, pour 0 <= r <= K-1
    
    # On itère sur toutes les valeurs possibles de r de 0 à K inclus.
    for r in range(K + 1):
        b = K - r     # 'b' est défini comme différence entre K et r.
        dif = r - b   # 'dif' est la différence entre r et b.
        
        # Si dif < 0 ou bien r < N, on passe à l'itération suivante (cas impossible ou pas intéressant).
        if dif < 0 or r < N:
            continue
        elif dif == 0:
            # Si dif == 0, alors r == b, on a un cas particulier.
            # On ajoute com2[r] à l'accumulateur de réponse.
            ans += com2[r]
            # S'il y a au moins 2, on retire com2[N-2] pour ajuster le résultat dans ce cas précis.
            if N >= 2:
                ans -= com2[N - 2]
        elif dif < N:
            # S'il y a moins de N de différence, on ajoute la différence entre deux coefficients binomiaux.
            # Cela permet de ne compter que les cas souhaités.
            ans += com[r] - com[N - 1 - dif]
        else:
            # Sinon, on ajoute simplement com[r].
            ans += com[r]
        
        # On fait le modulo tout de suite pour éviter les débordements et garder la réponse dans l'intervalle [0, mod-1].
        ans %= mod
    
    # Après avoir parcouru toutes les valeurs de r, on retourne la réponse obtenue.
    return ans

# On exécute solve() et affiche le résultat en utilisant print.
print(solve())