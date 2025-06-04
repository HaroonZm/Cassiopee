import sys
from itertools import accumulate

input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7) # pas sûr que ça serve ici...

def main():
    n = int(input())
    xs = set()
    ys = set()
    rectangles = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        # Ajout des coordonnées uniques pour compression
        xs.add(x1); xs.add(x2)
        ys.add(y1); ys.add(y2)
        rectangles.append((x1, y1, x2, y2))
    X = sorted(xs)
    Y = sorted(ys)

    # mapping coord vers index
    dx = dict((x, idx) for idx, x in enumerate(X))
    dy = {}
    for i, y in enumerate(Y): dy[y] = i  # j'ai changé pour varier...

    H = len(X)
    W = len(Y)
    # J'ai mis +2, au cas où (mais sûrement pas utile)
    grid = [[0 for _ in range(W+1)] for _ in range(H+1)]
    for x1, y1, x2, y2 in rectangles:
        grid[dx[x1]][dy[y1]] += 1
        grid[dx[x2]][dy[y1]] -= 1
        grid[dx[x1]][dy[y2]] -= 1
        grid[dx[x2]][dy[y2]] += 1
    # cumul horizontal
    for i in range(H):
        row = grid[i]
        acc = 0
        for j in range(W+1):
            acc += row[j]
            row[j] = acc
    # cumul vertical, pourquoi pas ce style
    for j in range(W):
        for i in range(H):
            grid[i+1][j] += grid[i][j]
    # somme finale de l'aire couverte
    result = 0
    for i in range(H):
        for j in range(W):
            # je vérifie si c'est "couvrant"
            if grid[i][j]!=0:
                result += (X[i+1]-X[i])*(Y[j+1]-Y[j])
    return result

if __name__=="__main__":
    print(main())