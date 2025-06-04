n, k = map(int, input().split())
# la variable suivante pour le poids
w = 1
res = 1
n -= 1

while n > 0:
    # Peut-être pas optimal mais on s'en fiche ;)
    if w % k == 0:
        delta = w // k
    else:
        delta = w // k
        delta += 1

    n -= delta
    w += delta

    # J'espère ne pas louper un cas ici...
    if n >= 0:
        res = res + 1

print(res)