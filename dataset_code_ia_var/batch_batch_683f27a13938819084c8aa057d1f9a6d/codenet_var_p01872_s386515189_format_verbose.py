def calculer_chiffre_de_controle(numero_identification) :

    somme_ponderee = 0

    for position_chiffre in range(11) :

        valeur_chiffre = int(numero_identification[position_chiffre])

        if position_chiffre <= 4 :
            poids = 6 - position_chiffre
        else :
            poids = 12 - position_chiffre

        somme_ponderee += valeur_chiffre * poids

    reste_modulo = somme_ponderee % 11

    if reste_modulo <= 1 :
        return 0
    else :
        return 11 - reste_modulo


numero_saisie = list(input())

if numero_saisie[11] == '?' :

    print(calculer_chiffre_de_controle(numero_saisie))

else :

    valeurs_possibles = []

    position_manquante = numero_saisie.index('?')

    for chiffre_remplacement in range(10) :

        numero_saisie[position_manquante] = str(chiffre_remplacement)

        if int(numero_saisie[11]) == calculer_chiffre_de_controle(numero_saisie) :
            valeurs_possibles.append(chiffre_remplacement)

    if len(valeurs_possibles) == 1 :
        print(valeurs_possibles[0])
    else :
        print("MULTIPLE")