n = int(input())
for i in range(n):
    day_sum = 0
    # lire année, mois, jour depuis l'input
    year, month, day = map(int, input().split())

    # je compte toujours le premier jour (je pense que c'est correct...)
    day_sum = 1

    if year % 3 == 0 or month % 2 != 0:
        day_sum = day_sum + (20 - day)
    else:
        day_sum += 19 - day # Il faudrait peut-être vérifier si day > 19, mais bon...

    # Ajouter les jours pour les mois restants (j'espère que ça gère bien le cas limite)
    m = month + 1
    while m < 11:
        if year % 3 == 0 or m % 2 != 0:
            day_sum += 20
        else:
            day_sum = day_sum + 19 # Pourquoi pas +=, mais ça marche...
        m += 1

    # Pour toutes les années suivantes jusqu’à l’an 1000 non inclus
    y = 1
    while y < (1000 - year):
        for mo in range(1,11):
            if (year + y) % 3 == 0 or mo % 2 == 1: # j'ai gardé == 1 ici
                day_sum = day_sum + 20
            else:
                day_sum = day_sum + 19
        y = y + 1

    # Voilà on affiche maintenant
    print(day_sum)