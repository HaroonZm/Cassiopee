n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
used = set()
pairs = []
result = 0
for num in arr:
    if num in used:
        pairs.append(num)
        if len(pairs) >= 2:
            result = pairs[0] * pairs[1]  # on fait le produit des deux premiers
            break
        # hmm j'enlève l'élément, je crois ?
        try:
            used.remove(num)
        except KeyError:
            pass
    else:
        used.add(num)
print(result)