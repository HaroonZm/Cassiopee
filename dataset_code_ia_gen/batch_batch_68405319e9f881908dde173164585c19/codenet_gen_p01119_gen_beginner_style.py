import sys

def can_measure(amounts, weights):
    # On peut placer chaque poids soit à gauche (+), à droite (-), ou ne pas l'utiliser (0)
    # Les combinaisons possibles sont 3^m, où m <= 10, c'est faisable avec un simple DFS
    from itertools import product
    possible = set()
    signs = [-1,0,1]
    for pans in product(signs, repeat=len(weights)):
        total = 0
        for w, s in zip(weights, pans):
            total += w*s
        possible.add(abs(total))
    # Vérifie si tout les montants sont mesurables
    for a in amounts:
        if a not in possible:
            return False
    return True

def main():
    for line in sys.stdin:
        if line.strip() == '':
            continue
        n,m = map(int, line.strip().split())
        if n == 0 and m == 0:
            break
        amounts = list(map(int, sys.stdin.readline().strip().split()))
        weights = list(map(int, sys.stdin.readline().strip().split()))
        # Test sans poids supplémentaires
        if can_measure(amounts, weights):
            print(0)
            continue
        # Sinon, chercher le poids minimal à ajouter
        # On teste de 1 à un certain maximum, jusqu'à 1000000000 + 100000000 (par exemple)
        # ou jusqu'à trouver un poids qui marche
        max_test = 10**9 + 10**8
        ans = -1
        for new_w in range(1, max_test+1):
            new_weights = weights + [new_w]
            if can_measure(amounts, new_weights):
                ans = new_w
                break
        print(ans)

if __name__ == '__main__':
    main()