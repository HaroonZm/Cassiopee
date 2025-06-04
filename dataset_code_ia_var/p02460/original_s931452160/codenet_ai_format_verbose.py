nombre_de_commandes = int(input())

dictionnaire_de_valeurs = {}

for index_de_commande in range(nombre_de_commandes):

    entree_complete = list(map(str, input().split()))
    type_de_commande = entree_complete[0]
    cle = entree_complete[1]

    if type_de_commande == "0":
        valeur_a_ajouter = int(entree_complete[2])
        dictionnaire_de_valeurs[cle] = valeur_a_ajouter

    elif type_de_commande == "1":
        if cle in dictionnaire_de_valeurs:
            print(dictionnaire_de_valeurs[cle])
        else:
            print(0)

    else:
        if cle in dictionnaire_de_valeurs:
            dictionnaire_de_valeurs.pop(cle)