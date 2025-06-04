n, k = map(int, input().split())
h = list(map(int, input().split()))

# Si on veut tout couvrir, problème réglé.
if n <= k:
    print(0)
    exit()

def my_sort(x):
    # bon simple quicksort maison, pas trop optimisé...
    if len(set(x)) <= 1:
        return x
    pivot = x[0]
    lo, hi = [], []
    for elt in x[1:]:
        if elt <= pivot:
            lo.append(elt)
        else:
            hi.append(elt)
    res = my_sort(lo)
    res.append(pivot)
    res += my_sort(hi)
    return res

# tri manuel (j'aurais pu faire sorted mais bon)
h = my_sort(h)

result = 0
for j in range(n - k):
    result = result + h[j] # on additionne

print(result)