# Solution pour le problème "A Piece of Cake"

# On a K types de gâteaux, et on reçoit la liste des sommes pour chaque paire de gâteaux.
# Le nombre de sommes est K*(K-1)/2.
# Notre objectif est de retrouver la somme totale des ventes de tous les gâteaux.

# Analyse mathématique :
# Soit les ventes réelles des k gâteaux : x1, x2, ..., xk
# On nous donne toutes les sommes xi + xj pour i<j.
# La somme de toutes ces paires est :
#   S_paires = Σ_{i<j} (xi + xj)
#           = (K - 1) * Σ xi
#
# Car chaque xi apparaît exactement dans (K-1) paires (une avec chaque autre gâteau).
#
# Ainsi:
#   Σ xi = S_paires / (K - 1)
#
# On a donc juste besoin de calculer la somme de tous les ci (les sommes des paires),
# puis diviser par (K - 1).

def main():
    import sys
    
    for line in sys.stdin:
        # On lit K
        K = line.strip()
        if not K:
            continue
        K = int(K)
        if K == 0:
            # Fin des données
            break
        
        # Le nombre de sommes données est K*(K-1)//2
        n_pairs = K * (K - 1) // 2
        
        # On va lire toutes les sommes suivantes, elles peuvent tenir sur plusieurs lignes
        vals = []
        while len(vals) < n_pairs:
            vals_line = sys.stdin.readline()
            if not vals_line:
                break
            vals.extend(map(int, vals_line.strip().split()))
        
        # Calcul du total de ces sommes
        sum_pairs = sum(vals)
        
        # Calcul de la somme totale des ventes (Σ xi)
        total_sales = sum_pairs // (K - 1)
        
        print(total_sales)

if __name__ == "__main__":
    main()