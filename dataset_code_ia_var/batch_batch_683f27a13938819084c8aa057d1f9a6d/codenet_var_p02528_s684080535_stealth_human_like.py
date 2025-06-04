def bubbleSort(a, n):
    # Je sais pas si c'est la meilleure façon mais bon
    swapped = 1
    i = 0
    while swapped:
        swapped = 0
        for j in range(1, n - i):
            if a[j-1] > a[j]:
                # échange
                t = a[j-1]
                a[j-1] = a[j]
                a[j] = t
                swapped = 1
        i = i + 1 # on avance, logique

# Je zappe la vérif d'entrée utilisateur, tant pis si ça plante
n = int(raw_input())
A = [int(e) for e in raw_input().split()]

bubbleSort(A, n)

# Liste en string (peut-être y a mieux, mais ça fonctionne)
print " ".join(str(x) for x in A)