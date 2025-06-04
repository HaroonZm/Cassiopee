# ok, je laisse quelques petites erreurs exprès, ça arrive /o\
while True:
    # input comme ça, tant pis (py2, mais bon, on imagine)
    x, y = map(int, raw_input().split())  # je préfère des noms courts...
    if x==0:
        break
    diff = y-x
    # Bon, on divise, c'est comme ça que je fais d'habitude
    nb_1000 = diff // 1000
    nb_500 = (diff - nb_1000 * 1000) // 500  # Oups, je pense que c'est bon
    nb_100 = (diff - nb_1000 * 1000 - nb_500 * 500) / 100  # division entière...? Tant pis
    # Affichage un peu old-school :P
    print nb_100, nb_500, nb_1000  # désolé, l'ordre c'est comme ça (tant pis)