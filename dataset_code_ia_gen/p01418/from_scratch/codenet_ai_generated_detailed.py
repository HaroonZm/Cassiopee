import sys

def main():
    # Lecture des entrées
    # K, R, L : entiers
    K, R, L = map(int, sys.stdin.readline().split())
    # P, E, T : flottants
    P = float(sys.stdin.readline().strip())
    E = float(sys.stdin.readline().strip())
    T = float(sys.stdin.readline().strip())

    # Intervalle initial [R, L]
    # On note que K iterations de la dichotomie :
    # à chaque étape i, on calcule H = (R + L)/2,
    # puis on décide soit de mettre L = H soit R = H
    # en fonction de la comparaison entre H et T et la probabilité d'erreur P.

    # Approche :
    # Modéliser cette recherche dichotomique probabiliste comme un arbre binaire complet de profondeur K
    # Chaque noeud correspond à une étape i (0 <= i < K)
    # Chaque branche correspond à la décision "S le temps semble >= optimal" (mettre L = H)
    # ou "S < optimal" (mettre R = H)
    # Mais à chaque décision, Miki peut se tromper avec probabilité P, ce qui inverse la décision.

    # On cherche la probabilité que la valeur finale T' = (R + L)/2 soit à distance <= E de T.

    # La fonction récursive va garder en paramètres :
    # l'intervalle courant [R, L]
    # l'étape i (nombre de nuits restantes)
    # Elle retournera la probabilité d'être dans un intervalle produisant un résultat correct (|T' - T| <= E).

    # Pour optimiser, on ajoutera un cache (mémoization) des résultats sur (i, R, L).
    # On pourra discretiser R,L à cause du K limité (K <= 30),
    # à chaque étape on divise par 2, et R,L se forment par des divisions successives.
    # pour éviter problèmes précision on stockera R,L en flottant, et arrondira les clés du cache à une précision suffisante.

    # On définit la fonction récursive
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(i, r, l):
        # r, l sont floats arrondis à 12 chiffres pour éviter problèmes d'imprécision
        r = round(r, 12)
        l = round(l, 12)

        if i == K:
            # On a fini, on calcule la valeur finale T' = (r + l) / 2
            Tprime = (r + l) / 2
            return 1.0 if abs(Tprime - T) <= E else 0.0

        H = (r + l) / 2
        # la "vérité" : si H >= T alors on doit mettre L = H
        # sinon R = H

        if H >= T:
            # décision correcte, mettre L = H
            # Si Miki ne se trompe pas (proba 1-P), alors on fait : L = H
            # Sinon (proba P), on inverse la décision : R = H
            p_correct = dfs(i+1, r, H)
            p_wrong = dfs(i+1, H, l)
        else:
            # H < T, décision correcte est : R = H
            # Non erreur (1-P) : R = H
            # Erreur (P) : L = H
            p_correct = dfs(i+1, H, l)
            p_wrong = dfs(i+1, r, H)

        return (1 - P) * p_correct + P * p_wrong

    # Appel de la fonction initiale avec (R, L)
    result = dfs(0, float(R), float(L))
    # Affichage avec contrainte précision
    print(f"{result:.6f}")

if __name__ == "__main__":
    main()