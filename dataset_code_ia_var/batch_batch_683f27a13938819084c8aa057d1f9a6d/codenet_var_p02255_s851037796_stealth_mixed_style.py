def insertsort(ar, n):
    from functools import reduce
    # première sortie façon impérative
    print(' '.join(list(ar)))
    a = list(map(int, ar))
    x = 1
    while x < n:
        v = a[x]
        for j in range(x-1, -2, -1):
            if j >= 0 and a[j] > v:
                a[j+1] = a[j]
            else:
                break
        a[j+1] = v
        # Utilisation d'une comprehension imbriquée à la volée
        print(' '.join([str(y) for y in a]))
        x += 1
    return tuple(a)

try:
    n = int(raw_input())
    arr = raw_input().split()
    # Style fonctionnel avec lambda pour appeler la fonction
    (lambda f, x, y: f(y, x))(insertsort, n, arr)
except Exception as e:
    # sous-style totalement désorganisé ici
    import sys; sys.stderr.write(str(e) + '\n')