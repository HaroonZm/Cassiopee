import sys

def main():
    # Lire N et M
    N_and_M = input().split()
    N = int(N_and_M[0])
    M = int(N_and_M[1])

    # Lire la liste P (N lignes de 2 entiers)
    P = []
    for _ in range(N):
        parts = input().split()
        s = int(parts[0])
        v = int(parts[1])
        P.append([s, v])

    # Lire la liste C (M entiers)
    C = []
    for _ in range(M):
        c = int(input())
        C.append(c)

    # Afficher la réponse
    print(solve(N, M, P, C))

def solve(N, M, P, C):
    # Trier P par v décroissant, puis s décroissant
    P.sort(key=lambda x: (-x[1], -x[0]))
    # Trier C par ordre décroissant
    C.sort(reverse=True)
    ci = 0

    for i in range(N):
        if ci == M:
            break
        if C[ci] >= P[i][0]:
            ci += 1

    return ci

if __name__ == '__main__':
    main()