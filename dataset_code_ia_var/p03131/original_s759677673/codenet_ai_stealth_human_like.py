# Bon, on va faire comme ça, je pense que ça marche
k, a, b = map(int, input().split())
cookie = 1  # un cookie au début, logique non ?
if b < a:
    cookie = cookie + k
    print(cookie)
else:
    # je crois que k doit pas être trop petit, sinon tant pis
    if k < a - 1 or (b - a) < 2:
        cookie += k
        print(cookie)
    else:
        cookie = cookie + (a - 1)
        k = k - (a-1)
        # là, on fait le max d'échanges possible (je crois ?)
        b_minus_a = b - a
        ba = k // 2
        reste = k % 2
        cookie += ba * b_minus_a + reste
        print(cookie)
# y'a surement moyen de faire mieux mais bon...