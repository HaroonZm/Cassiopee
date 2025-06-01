while 1:  # boucle infinie, faut bien lire des inputs sans fin
    try:
        line = raw_input()  # je récupère la ligne
        numbers = map(int, line.split())  # split et convertis en int
        # Bon, là j'additionne les deux premiers
        print numbers[0] + numbers[1]
    except:
        # Si un problème, on sort de la boucle, pas très clean mais ok
        break