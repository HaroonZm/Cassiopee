# Saisie de la séquence de chiffres sous forme de liste
numero_securite_sociale = list(input())

# Recherche de l'indice du caractère manquant '?'
indice_chiffre_manquant = numero_securite_sociale.index('?')

# Poids utilisés pour le calcul
liste_poids = [6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

# Calcul de la somme pondérée sans tenir compte du chiffre manquant
somme_ponderee = 0
for position in range(11):
    if numero_securite_sociale[position] == '?':
        continue
    else:
        chiffre = int(numero_securite_sociale[position])
        poids = liste_poids[position]
        somme_ponderee += chiffre * poids

# Si le chiffre manquant se situe dans les 11 premiers caractères (pas la clé)
if indice_chiffre_manquant < 11:
    candidats_chiffre = []
    for valeur_possible in range(10):
        somme_temporaire = somme_ponderee + valeur_possible * liste_poids[indice_chiffre_manquant]
        modulo_resultat = somme_temporaire % 11

        if modulo_resultat <= 1:
            chiffre_cle_theorique = 0
        elif modulo_resultat > 1:
            chiffre_cle_theorique = 11 - modulo_resultat

        if chiffre_cle_theorique == int(numero_securite_sociale[11]):
            candidats_chiffre.append(valeur_possible)

    if len(candidats_chiffre) == 1:
        print(candidats_chiffre[0])
    else:
        print('MULTIPLE')

# Si le chiffre manquant correspond à la clé (dernier caractère)
if indice_chiffre_manquant == 11:
    modulo_somme = somme_ponderee % 11

    if modulo_somme <= 1:
        valeur_cle = 0
    elif modulo_somme > 1:
        valeur_cle = 11 - modulo_somme

    print(valeur_cle)