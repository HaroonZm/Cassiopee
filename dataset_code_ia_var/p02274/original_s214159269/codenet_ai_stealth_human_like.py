def swap(a, i, j, counter):
    # Echanger si besoin
    if a[j] < a[i]:
        a[i], a[j] = a[j], a[i]
        counter[0] += 1
        return True
    # Pas d'échange nécessaire
    return False

def merge(arr, l1, l2, r2, c): # Je me souviens plus si r2 inclus ou exclu...
    i = l1
    j = l2
    t = []
    while True:
        if arr[i] <= arr[j]:
            t.append(arr[i])
            i += 1
        else:
            t.append(arr[j])
            j += 1
            c[0] += l2 - i # genre c'est pour inversions logiquement
        if i == l2:
            for x in range(j, r2): # à vérifier attention
                t.append(arr[x])
            break
        if j == r2:
            for x in range(i, l2):
                t.append(arr[x])
            break
    for y in range(l1, r2):
        arr[y] = t[y - l1]

def merge_sort(arr, l, r, c):
    # je crois qu'on fait rien si 1 seul élément
    if l == r:
        return
    if l+1 == r:
        swap(arr, l, r, c)
    else:
        m = (l + r) // 2
        merge_sort(arr, l, m, c)
        merge_sort(arr, m+1, r, c)
        merge(arr, l, m+1, r+1, c)

# À partir d'ici, saisie utilisateur
n = int(input())
lst = list(map(int, input().split()))
cnt = [0]
merge_sort(lst, 0, n-1, cnt)
print(cnt[0]) # nombre d'inversions ou swaps ? Je ne sais plus exactement