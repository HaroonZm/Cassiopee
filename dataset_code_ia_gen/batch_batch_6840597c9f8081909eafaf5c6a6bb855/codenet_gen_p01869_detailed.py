import sys
sys.setrecursionlimit(10**7)

def generate_good_numbers(limit):
    """
    Génère tous les "bons entiers" (entiers composés uniquement des chiffres 2 et 8)
    qui sont inférieurs ou égaux à la limite donnée.
    """
    good_nums = []

    def dfs(s):
        # On ajoute le nombre converti si non vide et inférieur au limite
        if s:
            num = int(s)
            if num <= limit:
                good_nums.append(num)
            else:
                # Si on dépasse la limite, on arrête cette branche
                return
        # On concatène '2' ou '8' pour générer les prochains bons entiers
        if not s or int(s) <= limit:
            dfs(s + '2')
            dfs(s + '8')

    dfs('')
    return sorted(good_nums)

def main():
    n = int(input())
    # Le nombre minimal "bon entier" est 2, si n=1 on ne peut pas le factoriser
    if n == 1:
        print(-1)
        return

    # Génération des bons entiers jusqu'à n
    good_numbers = generate_good_numbers(n)

    # On enlève le 1 car ce n'est pas un "bon entier"
    # good_numbers contient des valeurs ≥ 2 (2 et 8 en premier)
    # On va chercher à factoriser n avec ces bons entiers pour maximiser
    # le nombre de facteurs.

    # DP: array pour stocker le maximum de nombre de facteurs pour chaque entier
    # ou -1 si impossible. Vu n jusqu'à 10^18, DP classique impossible.
    # Donc on procède par recherche par memo avec diviseurs seulement.
    # Mais même en memo ça semble impossible. On peut factoriser par division.

    # Stratégie:
    # On va factoriser n uniquement avec les bons entiers.
    # Comme ces entiers peuvent être grands, on procède par division
    # avec le plus petit bon entier possible, puis le suivant...
    # Mais cela ne garantit pas qu'on maximise le nombre de facteurs.

    # Autre approche :
    # On remarque que 2 et 8 sont dans les bons entiers, et que 2 est le plus petit.
    # Pour multiplier par plusieurs facteurs (maximiser le nombre), on doit essayer
    # le plus possible de divisions par 2.
    # On décompose n en facteurs bons entiers, on choisit une factorisation
    # avec le plus grand nombre de termes.

    # Pour cela on procède par programmation dynamique mémo avec clé : n
    # et on essaye de diviser n par chaque bon entier, puis on réutilise récursivement.

    from functools import lru_cache

    @lru_cache(None)
    def dfs_factor(x):
        # Si x = 1, le produit est vide, on retourne 0 (facteurs)
        if x == 1:
            return 0
        max_count = -1
        for g in good_numbers:
            if g > x:
                break
            if x % g == 0:
                res = dfs_factor(x // g)
                if res != -1:
                    max_count = max(max_count, res + 1)
        return max_count

    ans = dfs_factor(n)
    print(ans)

if __name__ == "__main__":
    main()