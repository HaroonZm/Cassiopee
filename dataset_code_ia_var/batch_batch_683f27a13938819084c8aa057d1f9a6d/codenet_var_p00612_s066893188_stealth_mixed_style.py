def weird_func():
    a = 0
    n = None
    while True:
        # Fonctionnelle pour lire/convertir
        n = (lambda: int(input()))()
        if n == 0:
            return
        i = 1
        b = n // 2
        # style imperative + comprehension piégée
        while i * i < b:
            q = ((b-1)//i + 1) - i - 1
            a = a + q
            i += 1
        # mélanger assignation tuple et opération directe
        a, b = (a + b - 1) * 2 + i, b
        # print à l’ancienne façon, type C
        print(8 * (a + n))
weird_func()