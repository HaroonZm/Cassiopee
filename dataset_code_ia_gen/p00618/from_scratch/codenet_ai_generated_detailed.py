import sys

def main():
    input = sys.stdin.readline  # Lecture rapide des entrées

    while True:
        n, U = map(int, input().split())
        if n == 0 and U == 0:
            break

        credits = [0] * n       # Liste des crédits de chaque cours
        prereqs = [0] * n       # Prérequis sous forme de bitmask

        for i in range(n):
            data = list(map(int, input().split()))
            c = data[0]
            k = data[1]
            prereq_list = data[2:] if k > 0 else []

            credits[i] = c
            # Construire un bitmask des prérequis
            mask = 0
            for p in prereq_list:
                mask |= (1 << p)
            prereqs[i] = mask

        # On va tester toutes les combinaisons possibles de cours (jusqu'à 2^n)
        # et vérifier pour chacune :
        #  - si tous les prérequis des cours choisis sont aussi dans la sélection
        #  - si la somme des crédits >= U
        # Parmi celles qui satisfont les conditions, on garde la taille minimale
        ans = n  # maximum n cours

        # Parcours de tous les sous-ensembles possibles
        # Pour chaque sous-ensemble S, on vérifie :
        #  - pour chaque cours i dans S, prereqs[i] subset de S
        #  - somme credits dans S >= U
        # On cherche la taille minimale de S qui satisfait
        for subset in range(1 << n):
            total_credits = 0
            valid = True
            for i in range(n):
                if (subset & (1 << i)) != 0:
                    # Le cours i est choisi, vérifier prérequis
                    # prereqs[i] doit être inclus dans subset
                    if (prereqs[i] & subset) != prereqs[i]:
                        valid = False
                        break
                    total_credits += credits[i]
            if valid and total_credits >= U:
                # compter le nombre de cours dans subset
                count = bin(subset).count('1')
                if count < ans:
                    ans = count

        print(ans)

if __name__ == '__main__':
    main()