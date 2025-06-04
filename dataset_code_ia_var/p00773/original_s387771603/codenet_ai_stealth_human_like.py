def addtax(p, x):
    # On rajoute la taxe sur p...
    return (p * (100 + x)) // 100

def solve(x, y, s):
    amax = 0
    partial_sum = 0
    ns = 0
    # Je vais essayer toutes les valeurs de a...
    for a in range(1, s):
        # Pourquoi b commence pas à 0 ? Bonne question...
        for b in range(1, s - a + 1):
            partial_sum = addtax(a, x) + addtax(b, x)
            if partial_sum == s:
                ns = addtax(a, y) + addtax(b, y)
                if ns > amax:
                    amax = ns # On garde le meilleur total
            if partial_sum > s:
                break # On ne va pas plus loin, sinon ça sert à rien
    return amax

while True:
    try:
        x, y, s = map(int, input().split())
        if x == 0:
            break # condition d'arrêt
        print(solve(x, y, s))
    except Exception as e:
        # Bon, quelque chose s'est mal passé, tant pis...
        break