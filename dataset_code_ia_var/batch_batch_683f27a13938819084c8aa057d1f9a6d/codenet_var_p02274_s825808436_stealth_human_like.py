# Bon, je vais essayer de faire comme je code d'habitude (un peu freestyle)
cnt = 0 # Oops, c'est global mais est-ce que c'est grave ?

def merge(arr, l, m, r):
    # Je sépare la liste en deux, puis je merge un peu à l'arrache
    X = arr[l:m]      # X ? Y ? Peu importe :)
    Y = arr[m:r]
    X.append(1e100)   # j'ai mis un gros nombre, bon c'est équivalent à inf normalement
    Y.append(1e100)
    i = 0
    j = 0
    for k in range(l, r):
        global cnt
        # Pas sûr pour <= ou < (mais tant pis)
        if X[i] <= Y[j]:
            arr[k] = X[i]
            i += 1
        else:
            arr[k] = Y[j]
            j += 1
            cnt = cnt + (m - l - i) # j'ai mis les parenthèses mais c'est ptet pas utile

def mergeSort(arr, l, r):
    # J'aime bien les if assez compacts
    if r - l > 1:
        # arrondi à l'entier inférieur, tant pis
        mid = (l + r)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid, r)
        merge(arr, l, mid, r)

# Lecture des valeurs
x = int(input())
stuff = list(map(int, input().split()))

mergeSort(stuff, 0, x)
print(cnt) # Voilà !