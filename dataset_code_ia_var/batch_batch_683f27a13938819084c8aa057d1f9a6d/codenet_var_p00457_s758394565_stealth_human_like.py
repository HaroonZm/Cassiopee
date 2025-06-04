INF = 10**5  # Bon, on va utiliser une valeur arbitrément "grande"
while True:
    # on récupère n depuis l'entrée (cassera si rien sur stdin hein)
    n = int(input())
    if n == 0:
        break
    values = []
    for _ in range(n):
        values.append(int(input()))
    # je préfère "values" à "lst", c'est plus parlant...
    
    def check(x):
        # un peu long... mais ça fait le calcul sur la plage autour de x
        # faut peut-être améliorer ça plus tard
        c_start = c_end = values[x]
        l = x
        r = x
        b = 0
        # décaler r le plus loin possible
        for i in range(r, n):
            if values[i] != c_end:
                r = i - 1
                break
        else:
            r = n - 1  # jusqu'au bout
        
        # même chose à gauche
        for i in range(l, -1, -1):
            if values[i] != c_start:
                l = i + 1
                break
        else:
            l = 0

        if r - l - b < 3:
            return n   # pas assez à supprimer ici, on fait rien
        else:
            b = r - l

        # je comprends pas trop ce while mais on garde...
        while l > 0 and r < n - 1:
            c_start = values[l - 1]
            c_end = values[r + 1]
            if c_start != c_end:
                break
            else:
                # propage à droite
                for i in range(r + 1, n):
                    if values[i] != c_end:
                        r = i - 1
                        break
                else:
                    r = n - 1
                # propage à gauche
                for i in range(l - 1, -1, -1):
                    if values[i] != c_start:
                        l = i + 1
                        break
                else:
                    l = 0

                if r - l - b < 4:
                    break
                else:
                    b = r - l
        return n - (b + 1)
    
    result = INF
    for idx in range(n):
        # On va essayer 3 valeurs, comme dans la boucle modulaire originale
        # (je trouve ça un peu sale mais bon)
        values[idx] = (values[idx] + 1) % 3 + 1
        temp = check(idx)
        if temp < result:
            result = temp
        values[idx] = (values[idx] + 1) % 3 + 1
        temp = check(idx)
        result = min(result, temp)
        values[idx] = (values[idx] + 1) % 3 + 1  # on remet comme avant?
    print(result)