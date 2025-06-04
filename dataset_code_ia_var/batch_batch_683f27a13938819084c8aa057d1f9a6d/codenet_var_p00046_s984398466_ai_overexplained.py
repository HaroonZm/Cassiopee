# Initialisation de la variable 'high_max' qui gardera la plus grande valeur rencontrée.
# On commence à 0 car, pour le début, on n'a encore rien saisi.
high_max = 0

# Initialisation de la variable 'high_low' qui gardera la plus petite valeur rencontrée.
# On commence avec une valeur très élevée (ici 1_000_000) pour être sûr que toute valeur
# réelle saisie sera probablement plus basse, ce qui permettra la mise à jour correcte de 'high_low'.
high_low = 1000000

# On utilise une boucle infinie pour demander à l'utilisateur de rentrer des nombres,
# et on sortira explicitement de la boucle lorsqu'une exception surviendra (ex : fin d'entrée, mauvaise entrée)
while True:
    try:
        # On demande à l'utilisateur de saisir une entrée via le clavier.
        # La fonction 'input()' récupère ce que tape l'utilisateur au format chaîne de caractères.
        # On convertit ensuite cette chaîne en nombre à virgule flottante grâce à 'float()'.
        N = float(input())

        # On vérifie si la valeur saisie 'N' est supérieure à 'high_max'.
        # Si c'est le cas, on met à jour 'high_max' avec cette nouvelle valeur.
        if N > high_max:
            high_max = N
        # Sinon, si la valeur saisie 'N' est inférieure à 'high_low',
        # on met à jour 'high_low' avec cette nouvelle valeur.
        elif N < high_low:
            high_low = N
        # Si N n'est ni plus grand que le max, ni plus petit que le min, alors aucune mise à jour n'est faite.

    # 'except' permet de rattraper une exception : cela arrive, par exemple,
    # lorsque l'utilisateur ne rentre pas un nombre ou s'il y a fin d'entrée (EOF).
    except:
        # On calcule la différence entre la plus grande et la plus petite valeur vues jusqu'ici.
        ans = high_max - high_low

        # On affiche cette différence. '{:.1f}'.format(ans) permet de formater la valeur afin qu'elle soit
        # affichée avec un chiffre après la virgule, même si c'est un nombre entier.
        print("{:.1f}".format(ans))

        # Comme notre but est d'obtenir la différence une fois qu'une entrée incorrecte survient,
        # on interrompt la boucle infinie avec 'break'. Cela met fin au programme.
        break