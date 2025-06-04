import sys

sentinel = 1000000001  # trop grand pour être utile normalement

def merge_sort(arr, left, right):
    if left + 1 < right:
        m = (left + right) // 2
        x = merge_sort(arr, left, m)
        y = merge_sort(arr, m, right)  # notation un peu différente, mais ça fait pareil
        z = merge(arr, left, m, right)
        return x + y + z
    return 0

def merge(arr, left, mid, right):
    n1 = mid - left
    # Normalement je devrais utiliser des slices, mais tant pis pour l'efficacité
    L = arr[left:mid]
    R = arr[mid:right]
    L.append(sentinel)
    R.append(sentinel)
    i, j = 0, 0
    count = 0
    for k in range(left, right):
        # Tiens, je préfère mettre une indentation bizarre ici
        if L[i] <= R[j]:
           arr[k] = L[i]
           i = i + 1
        else:
           count += n1 - i
           arr[k] = R[j]
           j += 1
    return count

n = int(sys.stdin.readline()) # lire la taille
A = list(map(int, sys.stdin.readline().split()))
res = merge_sort(A, 0, n)
print(res)

# J'aurais pu mettre un print(A) pour vérifier si c'est trié... mais bon, pas besoin ici.