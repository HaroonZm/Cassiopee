import sys

def main():
    sys.setrecursionlimit(10**6)
    inf = float('inf')
    mod = 10**9+7

    # Fonctions d'entrée simplifiées
    def I():
        return int(input())

    def LI():
        return list(map(int, input().split()))

    def LI_():
        return [int(x)-1 for x in input().split()]

    N = I()
    X = LI()
    M = I()
    A = LI_()

    # Tableau pour vérifier l'existence de chaque nombre
    exist = [0] * 2021
    for num in X:
        exist[num] += 1

    # Pour chaque a dans A, essaye d'incrémenter X[a] si possible
    for a in A:
        valeur = X[a]
        if valeur == 2019 or exist[valeur+1]:
            continue
        else:
            exist[valeur+1] += 1
            exist[valeur] -= 1
            X[a] += 1

    # Affiche chaque valeur de X sur une nouvelle ligne
    for x in X:
        print(x)

if __name__ == '__main__':
    main()