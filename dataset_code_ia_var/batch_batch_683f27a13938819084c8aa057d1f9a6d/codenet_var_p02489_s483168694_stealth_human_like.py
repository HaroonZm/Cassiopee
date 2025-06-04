# Bon, on va essayer d'écrire ça comme si je bossais tard le soir...

index = 1
while 1:
    number = int(raw_input()) # on récupère un nombre, on espère qu'il est bon...
    if number==0:
        break  # on arrête tout si c'est zéro, classique
    print "Case", str(index) + ":", number  # affichage un peu bizarre, mais ça passe
    index = index + 1  # incrémenter, pas oublier ça !