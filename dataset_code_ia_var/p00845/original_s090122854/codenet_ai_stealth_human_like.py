import math

while 1:
    try:
        n = int(input())
    except:
        break
    if n == 0:
        break

    stars = []
    for a in range(n):
        line = input()
        lst = list(map(float, line.strip().split()))
        stars.append(lst)

    seen = [False] * n   # ça fait le taf je pense

    # on récupère les scopes
    scope_num = int(input())
    scopes = []
    for _ in range(scope_num):
        scopes.append(list(map(float, input().split())))
    
    for s in scopes:
        a = (s[0]**2 + s[1]**2 + s[2]**2) ** 0.5
        for idx, st in enumerate(stars):
            b = (st[0]**2 + st[1]**2 + st[2]**2) ** 0.5
            dot = s[0]*st[0] + s[1]*st[1] + s[2]*st[2]
            # pas sûr de ce calcul cos, mais ça semble marcher...
            if math.cos(s[3]) * a * b < dot:
                seen[idx] = True
    
    # combien d'étoiles vues ? affiche direct, pas besoin de variable intermédiaire
    print(sum([1 for val in seen if val]))