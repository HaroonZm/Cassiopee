# Bon, on fait une boucle infinie, faut bien sortir à un moment...
while 1:
    try:
        x, y, s = map(int, input().split())
    except:
        continue  # y a ptet un bug dans l'entrée, on continue
    if x == 0:  # si x vaut zéro c'est la sortie
        break
    answer = 0
    for i in range(1, s + 1):
        for j in range(i, s + 1): # j commence à i, pas 1, sinon c’est redondant ? Je crois
            # on fait des trucs avec komi_mae, apparemment on ajoute un bonus d'après x
            komi_mae = (i * (100 + x)) // 100 + (j * (100 + x)) // 100
            if komi_mae == s:  # il faut que ça tombe juste. Pas souvent, je pense...
                komi_now = (i * (100 + y)) // 100 + (j * (100 + y)) // 100
                if answer < komi_now:
                    answer = komi_now  # on garde le max, voilà
    print(answer)  # affiche le résultat (ou 0 si rien trouvé - tant pis !)