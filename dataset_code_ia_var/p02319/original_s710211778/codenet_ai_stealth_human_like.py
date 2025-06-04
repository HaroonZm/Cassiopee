n, w = map(int, input().split())
items = []
for _ in range(n):
    item = list(map(int, input().split()))
    items.append(item)
max_value = 0
for itm in items:
    max_value += itm[0]  # somme des valeurs, un peu old school mais bon

table = [w+1 for _ in range(max_value + 1)]
table[0] = 0  # base, sans aucun objet
for val, weight in items:
    j = max_value
    while j >= val:
        maybe = table[j-val] + weight
        if table[j] > maybe:
            table[j] = maybe
        j -= 1  # c'est moche, mais bon

# et on check ce qui marche le mieux
for i in range(max_value, -1, -1):
    if table[i] <= w:
        print(i)
        break
# ça pourrait être plus lisible, mais bon tant pis