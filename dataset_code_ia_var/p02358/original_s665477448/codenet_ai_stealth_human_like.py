import sys
import bisect

# Bon, on va essayer de résoudre ce problème carré...
def main():
    N = int(sys.stdin.readline())
    data = []
    for _ in range(N):
        # On lit tous les entiers en une fois
        line = sys.stdin.readline()
        data.append(list(map(int, line.strip().split())))
    
    # Décomposons pour "plus de clarté"
    X1 = [row[0] for row in data]
    Y1 = [row[1] for row in data]
    X2 = [row[2] for row in data]
    Y2 = [row[3] for row in data]

    # On passe tout ça à compress, un peu de magie
    all_X = compress(X1, X2)
    all_Y = compress(Y1, Y2)

    # Toujours plus de 0
    mat = [[0 for _ in range(len(all_X))] for __ in range(len(all_Y))]

    # On met à jour les coins des rectangles dans la matrice
    for i in range(N):
        mat[Y1[i]][X1[i]] += 1
        mat[Y2[i]][X2[i]] += 1
        mat[Y2[i]][X1[i]] -= 1
        mat[Y1[i]][X2[i]] -= 1

    # un peu de cumul horizontal
    for r in range(len(mat)):
        for c in range(1, len(mat[0])):
            mat[r][c] = mat[r][c] + mat[r][c-1]

    # puis vertical
    for r in range(1, len(mat)):
        for c in range(len(mat[0])):
            mat[r][c] += mat[r-1][c]

    ans = 0

    # On boucle dans la matrice pour ajouter les aires occupées
    for r in range(len(mat)-1):
        for c in range(len(mat[0])-1):
            if mat[r][c] > 0:
                # Ouais, les +1 pour all_X, all_Y ici
                dx = all_X[c+1] - all_X[c]
                dy = all_Y[r+1] - all_Y[r]
                ans += dx * dy

    print(ans)
    
def compress(A, B):
    # Compresser, c'est la vie
    store = []
    for x in (A + B):
        store.append(x)
        # J'ai la flemme de gérer les delta ici :-)
    store = sorted(set(store))
    for i in range(len(A)):
        A[i] = bisect.bisect_left(store, A[i])
        B[i] = bisect.bisect_left(store, B[i])
    return store

if __name__ == '__main__':
    main()