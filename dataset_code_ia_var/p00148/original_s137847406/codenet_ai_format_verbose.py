liste_de_chiffres_format_code = [39] + list(range(1, 39))

while True:

    try:
        saisie_utilisateur = input()
        entier_saisi_par_utilisateur = int(saisie_utilisateur)
        indice_liste_code = entier_saisi_par_utilisateur % 39
        valeur_pour_code = liste_de_chiffres_format_code[indice_liste_code]
        code_formate = "3C{0:02d}".format(valeur_pour_code)
        print(code_formate)

    except:
        break