MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**7)

# On nous donne M (le reste modulo MOD) et C (chaine chiffrée), on doit retrouver D (entier original)
# C est une "encodage" des chiffres de D avec une substitution 1-1 :
#   - Chaque chiffre de D est remplacé par un même chiffre selon une correspondance (bijection)
#   - Cette correspondance conserve la position (même chiffre dans même position donne même chiffre chiffré)
#   - Cela signifie une correspondance chiffre->chiffre chiffré
#   - Inversement, chiffre chiffré -> chiffre original aussi 1-1
#
# On veut retrouver un D au début sans zéro inutile (pas de leading zero sauf si D=0)
# et tel que D % MOD == M
#
# Stratégie :
# - On connaît la chaine cryptée C
# - On ne connaît pas la traduction, mais on sait que c'est une substitution bijective entre chiffres {0..9}
# - On doit trouver une correspondance chiffre_orig->chiffre_coded (montrée par C)
# - On veut décoder C en D possibles (on connait C donnée)
# - Le problème est donc de trouver une permutation (ou mapping) des chiffres origine vers le chiffrement C
#   inverse de cette substitution pour retrouver D
#
# Mais on a seulement C (chiffre crypté) et M (D mod MOD)
#
# On veut Deviner D en décodant C par un mapping chiffre_coded->chiffre_orig proposée,
# où le mapping est une injection 1-1 sur les digits distincts de C
#
# On note:
#   C : chaîne chiffée
#   D : la chaîne décodée (les chiffres originaux)
#
# Il faut des correspondances :
#   pour chaque chiffre dans C (chiffre crypté), on attribue un chiffre orig dans D
#   pas de conflit :
#       pas 1 chiffre origine multiple fois pour 2 chiffres cryptés different -> mapping bijection chiffre crypté -> chiffre origine
#
# Aussi, D sans 0 leading (sauf si D=0)
#
# On veut un D edge qui satisfait D % MOD == M
#
# Le problème est cher (|C| jusqu'à 10^5), donc backtracking standard est impossible.
#
# Approche pour un grand |C|:
#   C contient plusieurs digits, on veut un mapping chiffre crypté -> chiffre originaux (dans 0..9)
#   Le set des digits cryptés est au max 10
#
#   Donc on doit assigner à chaque digit crypté un digit originel (0..9) sans conflit
#   => les assignations possible sont permutations injectives parmi 10 chiffres.
#
#   On a au max 10 digits distinct dans C donc un nombre possible de permutations à tester est au plus 10! = 3.6 million
#   ce qui est trop lourd.
#
#   Cependant dans le pire cas, on peut réduire le nombre de choix en essayant un algo efficace :
#   - Pour les décodages, on peut déterminer l'ordre des chiffres cryptés observés dans C
#   - On peut appliquer un DFS avec élagage pour assigner à chaque digit crypté un digit origine
#   - En décodant progressivement C avec le mapping partiel, on calcule le reste modulo MOD de D partiellement
#   - Si à un moment le reste modulo ne peut plus correspondre à M, on stoppe la branche
#
#   L'important est de faire un DFS efficace et un calcul du reste modulo de D en temps O(n)
#
# Détail calcul modulo progressif :
#   Le nombre D est donné par chiffres d, D = int(D)
#   D mod MOD = ( (D mod MOD)*10 + prochain_chiffre) mod MOD
#
#   Ainsi, en déchiffrant C en D progressivement, on calcule modulo partiellement
#
# On pourra choisir un ordre d'exploration "chiffres cryptés" dans la position de C dans l'ordre d'apparition
#
# Contraintes et optimisations:
#   - D n'a pas de leading 0 sauf si D==0, donc pour le premier caractère de C, chiffre crypté, son chiffre origin doit ne pas être 0 sauf si C == "0"
#   - C peut être long (10^5), donc on ne peut pas recomputer modulo a chaque fois depuis 0,
#     il faut faire un calcul mod progressif en une passe per assignment step
#
# - On définit:
#   * chars_distinct = liste des digits distincts apparaissant dans C
#   * mapping: digit crypté -> digit origine (tentative)
#   * utilisé: liste indiquant si digit origine est déjà affecté
#
# Implémentation:
#
#   1) On récupère digits distincts S du C
#   2) On fera DFS sur ces chiffres distincts
#      pour chaque, on essaie tous les digits origine non utilisés
#      en tenant compte de la contrainte leading zero
#
#   3) Pour chaque assignment, on calcule D modulo MOD en parcourant C:
#      On ne veut pas recalculer tout à chaque étape, alors on essaye d'avancer progressivement.
#      => Pour grande |C|, recalcul au complet est trop long
#
# Solution:
#   - A chaque étape de dfs, on applique assignation sur les digit crypté
#   - on peut pré-calculer une array big des digits C (indices)
#   - On décode C en D (digits originaux) en remplaçant les digits cryptés selon mapping
#     Le mapping est partiel pendant dfs. On ne peut calculer modulo si mapping incomplet
#
#   - On garde la liste d'indices des positions dans C triée par digit crypté
#   - Ou mieux, on traite D uniquement quand mapping complet.
#
# Premier trie pour éliminer échecs rapides:
#   - Si on ne peut pas trouver de mapping qui donne D mod MOD == M, on renvoie -1
#
# Comme toute tentative bruteforce est trop lourde, on peut utiliser une technique de "résolution par backtracking + calcul modulo partiel"
#
# Mais solution optimale dans le temps est compliquée.
#
# Observation importante :
# Il y a jusqu'à 10 digits distinct dans C.
#
# Pour un nombre petit de digits distinct, bruteforce permutations est possible.
#
# Donc solution:
# - Identifier digits distincts dans C
# - S'il y a plus de 10 digits distincts, pas possible (en pratique impossible car digits entre 0-9)
# - Faire un backtracking sur les permutations possibles des digits origine {0..9} affectées à digits cryptés distincts
# - Pour chaque tentative, reconstituer D en remplaçant C[i] (digit crypté) par digit origine affecté
# - Vérifier pas leading zero (premier digit origin ne doit pas être 0 sauf si longueur 1)
# - Calculer D mod MOD et le comparer à M
# - S'il égal, on renvoie D (sous forme string)
# - Sinon test autre permutation
#
# Le nombre de permutations max est 10! = 3628800, ce qui peut être cher en Python.
#
# Mais la plupart des cas ont moins de digits distincts, donc l'exploration est bien plus rapide.
#
# On implémentera donc cette solution.


from itertools import permutations

def main():
    M = int(input())
    C = input()
    MOD = 10**9 + 7

    digits_crypt = sorted(set(C))  # chiffres cryptés distincts dans C, par ordre
    n = len(digits_crypt)

    # Map les digits cryptés à des indices 0..n-1
    idx_map = {d:i for i,d in enumerate(digits_crypt)}

    # On prépare un tableau d'indices du chiffre crypté pour chaque position dans C (ex: [digit_index])
    crypt_idx_arr = [idx_map[c] for c in C]

    digits_orig = [str(i) for i in range(10)]

    # On souhaite tester permutations des digits origine sur digits distinct cryptés
    # vérification leading zero : premier char crypté ne doit pas être 0 en origine sauf si |C|==1
    first_crypt_digit = C[0]
    first_idx = idx_map[first_crypt_digit]

    # On pré-calcule une fonction pour calculer D mod MOD à partir du mapping
    def calc_mod(mapping):
        # mapping : liste longueur n, mapping[i] : digit origine assigné à digits_crypt[i]
        # reconstruire D mod MOD
        res = 0
        for i in range(len(C)):
            d_orig = mapping[crypt_idx_arr[i]]
            res = (res*10 + d_orig) % MOD
        return res
    
    # On pré-calcule un callback pour construire string D par mapping
    def build_D(mapping):
        return ''.join(str(mapping[crypt_idx_arr[i]]) for i in range(len(C)))

    # On va tenter les permutations
    # pour toutes permutations p of digits_orig length n taken without repetition
    # avec contrainte que p[first_idx] != 0 ou si |C|==1 on accepte 0

    # Optimisation: on ne teste que permutations qui respectent la contrainte leading zero
    # On peut générer permutations et filter sur critère

    digits_orig_int = list(range(10))

    for perm in permutations(digits_orig_int, n):
        # leading zero check
        if perm[first_idx] == 0 and len(C) > 1:
            continue

        # mapping possible
        if calc_mod(perm) == M:
            # build and print D
            D_str = build_D(perm)
            print(D_str)
            return

    print(-1)

if __name__ == "__main__":
    main()