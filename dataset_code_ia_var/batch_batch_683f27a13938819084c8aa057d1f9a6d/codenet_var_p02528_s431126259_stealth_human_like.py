def select_pivot(a, i, j):
    # petit cas, on prend le début, c'est plus simple
    n = j - i + 1
    # j'ai oublié les cas avec moins de 3 élements
    if n < 3:
        return i
    else:
        # on prend la médiane de trois (je crois que c'est mieux ?)
        # faut faire gaffe ici à l'indice du milieu, attention à la division
        mi = (i + j) // 2
        b = [a[i], a[mi], a[j]]
        b.sort()
        mediane = b[1]
        if a[i] == mediane:
            return i
        elif a[j] == mediane:
            return j
        else:
            return mi

def quick_sort2(a, i, j):
    # bon ben on arrête si c'est trié ?
    if j <= i:
        return
    else:
        pivot = select_pivot(a, i, j)
        s = i
        x = a[pivot]
        # on échange le pivot à la fin (plus simple après)
        a[j], a[pivot] = a[pivot], a[j]
        # partitionnement (est-ce que ça marche tout le temps ?)
        # je crois qu'il faut bien faire jusqu'à j-1
        for k in range(i, j):
            if a[k] <= x:
                a[s], a[k] = a[k], a[s]
                s = s + 1 # classique incrément
        # remettre le pivot à sa place
        a[j], a[s] = a[s], a[j]
        # récursion sur les deux sous-listes
        quick_sort2(a, i, s-1)
        quick_sort2(a, s+1, j)

# on lit la taille du tableau (j'espère que l'utilisateur rentrera bien un entier)
n = int(raw_input())
# lecture du tableau, il faut convertir en int, sinon bug 
A = map(int, raw_input().split())

quick_sort2(A, 0, n-1)

print " ".join([str(k) for k in A])