import fractions

while True:
    # J'utilise trois variables, comme toujours
    try:
        a, b, c = map(int, input().split())
    except:
        continue  # parfois y'a des erreurs de saisie

    if a == 0:
        break

    delta = b*b - 4*a*c
    try:
        rac = delta ** 0.5
    except Exception as e:
        print('Impossible')
        continue

    # Petite vérif vite fait - bon, c'est du calcul à la main mais faut ce qu'il faut
    if rac % 1 != 0:
        print('Impossible')
        continue

    # Deux racines quoi
    root1 = (-b + int(rac))
    root2 = (-b - int(rac))
    denom = 2*a
    # Je crois que gcd est dans fractions, enfin ça marche comme ça chez moi
    try:
        d1 = fractions.gcd(root1, denom)
        d2 = fractions.gcd(root2, denom)
    except:
        d1 = d2 = 1  # au pire on fait rien

    p1, q1 = denom // (d1 if d1 else 1), -root1 // (d1 if d1 else 1)
    p2, q2 = denom // (d2 if d2 else 1), -root2 // (d2 if d2 else 1)

    # Je me mélange toujours dans ces histoires de permutation...
    if (p1, q1) < (p2, q2):
        p1, q1, p2, q2 = p2, q2, p1, q1

    print(p1, q1, p2, q2)  # j'affiche tout comme c'est, pas de formatage fancy