import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 10**9 + 7

# On nous donne une permutation p de taille N.
# Le problème décrit une suite de transformations sur la permutation x, initialisée à l'identité (1,2,...,N).
# À chaque itération, on remplace x par y où y(i) = p(x(i)).
# On accumule la somme des éléments de la sous-liste x[l_i:r_i], et on teste si x[l_i:r_i] est la séquence consécutive (l_i,...,r_i).
# Si oui, on arrête et on affiche (ret mod 10^9+7).
# Sinon, on répète la mise à jour de x et le processus à partir du prochain query.

# Observations clefs :
# - La mise à jour x = y revient à appliquer p à x, i.e. x = p ◦ x
# - Initialement, x = id
# - Après k itérations : x = p^k (puissance k de p, composée k fois)
# - Le test sur le segment x[l:r] cherche à savoir si x[l..r] == range(l, r+1)

# L'énoncé garantit que p^k = id pour un certain k ≤ 40, pour toute position i.
# Donc la permutation p est de période ≤40.

# Cela signifie que la séquence x après k itérations est périodique avec une période ≤ 40.

# Solution efficace:
# 1. Pré-calcule toutes les puissances p^k pour k=0..max_k (max_k = 40)
#    Chaque p^k sera une permutation de [1..N].
# 2. Pour chaque p^k, calcule une pré-somme pour faire la somme segmentaire rapidement.
# 3. Pour chaque query (l,r), on cherche la plus petite k (itération) telle que x[l:r] == [l..r].
#    - x correspond à p^k
#    - Tester si segment p^k[l-1:r] == [l..r] implique une comparaison de segment
# 4. On appliquera les queries dans l'ordre, et on maintiendra un compteur global ret de la somme accumulée.
#    - Pour chaque query, on devra avancer k à partir du précédent max k
#    - En fait, on peut faire plus simple : 
#      puisque le processus global s'arrête quand on a trouvé un segment égal à [l_i..r_i],
#      on peut simuler les étapes itératives en avançant k de 0 à max_k,
#      à chaque étape k, on ajoutera à ret la somme sur [l_i,r_i] de p^k et on testera la condition.
#    - Or Q peut être grand (10^4), on ne veut pas faire naïvement 40 * 10^4 passages

# Optimisation supplémentaire :
# - Comme max_k ≤ 40, on peut pré-calculer pour chaque k la totalité de p^k
# - Pour chaque position, créer un tableau val_pos[k][i] = p^k[i]
# - Pour each query, pour k=0..max_k, on fait le test
# - To speed up, on peut chercher k minimal pour que p^k[l:r] == [l..r] seulement
#   En pratique, cela recomporte peu.
# - Mais étant donné les contraintes max_k=40, Q=10^4, N=10^5, c'est faisable
#   avec un algorithme efficace en mémoire (lecture optimisée et somme segmentaire via préfixes)

# Implémentation :

def compose(p, q):
    """Compose deux permutations p et q (0-based indices)"""
    return [p[q_i - 1] for q_i in q]

def is_consecutive_segment(arr, l, r):
    # Vérifie si arr[l:r+1] == [l+1, l+2, ..., r+1]
    # arr zero-based
    expected = range(l + 1, r + 2)
    for i, val in enumerate(arr[l:r+1]):
        if val != expected[i]:
            return False
    return True

def main():
    N, Q = map(int, input().split())
    p = [int(input()) for _ in range(N)]
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    max_k = 40  # d'après l'énoncé, p^k = id pour k ≤ 40

    # Pré-calcul des puissances p^k
    # p_powers[k] donnera la permutation p^k (0-based indices)
    # p_powers[0] = id
    p_powers = [list(range(1, N + 1))]
    for k in range(1, max_k + 1):
        # p^k = p o p^{k-1}
        new_perm = [p[val - 1] for val in p_powers[-1]]  # compose p avec p^{k-1}
        p_powers.append(new_perm)

    # Calcul des préfixes pour chaque k afin de faire somme sur segments rapidement
    prefix_sums = []
    for k in range(max_k + 1):
        ps = [0] * (N + 1)
        arr = p_powers[k]
        for i in range(N):
            ps[i + 1] = ps[i] + arr[i]
        prefix_sums.append(ps)

    ret = 0
    # Pour chaque requête, on simule depuis k=0 jusqu'à max_k
    # = on cherche la plus petite k tq segment p^k[l-1:r] == [l..r]
    # On cumule les sommes x(l_i)+..+x(r_i) = sum segment de p^k[l-1:r]
    for l, r in queries:
        found = False
        for k in range(max_k + 1):
            # somme sur [l,r]
            s = prefix_sums[k][r] - prefix_sums[k][l - 1]
            ret += s
            if ret >= MOD:
                ret %= MOD
            # test égalité segment
            if is_consecutive_segment(p_powers[k], l - 1, r - 1):
                print(ret % MOD)
                found = True
                break
        if not found:
            # En théorie jamais car p^k = id avec k ≤ 40
            # Mais on doit afficher ret même si on ne break pas?
            # L'énoncé précise "terminer"
            # Ici, on continue simplement au prochain query
            # Par sécurité, on peut aussi print ret
            print(ret % MOD)

if __name__ == "__main__":
    main()