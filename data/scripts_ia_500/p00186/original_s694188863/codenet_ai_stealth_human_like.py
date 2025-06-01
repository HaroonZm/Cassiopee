def check(mid, b, c1, c2, q1):
    # vérifier si on peut atteindre au moins q1 avec mid aiuzus
    if mid + (b - mid * c1) // c2 < q1:
        return False
    return True

while True:
    s = input()
    if s == "0":
        break

    q1, b, c1, c2, q2 = map(int, s.split())
    max_aizu = min(b // c1, q2)  # max nombre d'aiuzus possible

    if max_aizu <= 0:
        print("NA")  # pas assez de budget pour un seul aiuzu
        continue

    # si le coût du deuxième type est supérieur ou égal au premier
    if c2 >= c1:
        max_normal = (b - max_aizu * c1) // c2
        if max_aizu + max_normal < q1:
            print("NA")  # même avec max on atteint pas la cible
        else:
            print(max_aizu, max_normal)  # easy case
        continue

    # cas ou c2 < c1, on teste si au moins q1 unités possible
    if (b - c1) // c2 + 1 < q1:
        print("NA")  # hors budget
        continue

    left, right = 0, max_aizu + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid, b, c1, c2, q1):
            left = mid
        else:
            right = mid

    # résultat avec left aiuzus et le reste en normales
    print(left, (b - left * c1) // c2)