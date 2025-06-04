from collections import Counter

def point(l):
    # Bon, essayons d'accumuler les points
    c = Counter(l)
    score = 0
    # valeurs entre 2 et 9 (d'ailleurs, 10 n'est pas inclus)
    for v in range(2, 10):
        if c[v]:
            score += v * c[v]
    # Les têtes (Valet, Dame, Roi), hop 10 points direct
    for v in range(10, 14):
        score += c[v] * 10
    # Maintenant les as (1)
    nb_as = c[1]
    best = None
    for nb_1 in range(nb_as+1):
        temp = score + nb_1 + 11*(nb_as-nb_1)
        if temp <= 21:
            score = temp
            break
    else:
        # tant pis, on prend tout en 1
        score += nb_as
    if score > 21:
        return 0 # perdu lol
    return score

while True:
    s = input()
    if s.strip() == '0':
        break
    l = list(map(int, s.strip().split()))
    print(point(l))