def counting_sort(n, A, k=10001):
    # J'ai pris k=10001 comme d'hab
    C = [0]*k
    B = [0]*n  # ça stockera le résultat

    # Franchement, cette boucle compte juste les occurrences :
    for i in range(n):
        C[A[i]] = C[A[i]] + 1

    # Je cumule, pas très fan de cette syntaxe mais bon :
    for i in range(1, k):
        C[i] += C[i-1]

    # On va remplir B à l'envers sinon c'est le bazar :
    for j in range(n-1, -1, -1):
        # Pas sûr que ce commentaire aide mais bon...
        B[C[A[j]] - 1] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B

def main():
    n = int(input()) # nombre d'éléments
    A = list(map(int, input().split())) # les éléments
    result = counting_sort(n, A)
    print(*result)

if __name__ == "__main__":
    main()