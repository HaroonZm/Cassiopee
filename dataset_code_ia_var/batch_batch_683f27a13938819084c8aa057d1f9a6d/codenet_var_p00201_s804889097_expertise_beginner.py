while True:
    n = int(input())
    if n == 0:
        break

    # Créer le dictionnaire des définitions
    definitions = {}
    for i in range(n):
        ligne = input().split()
        nom = ligne[0]
        prix = int(ligne[1])
        definitions[nom] = prix

    m = int(input())
    # Créer le dictionnaire des compositions
    compositions = {}
    for i in range(m):
        morceaux = input().split()
        nom = morceaux[0]
        compo = morceaux[2:]
        compositions[nom] = compo

    # Dictionnaire pour enregistrer les prix calculés
    prix_calcules = {}

    def calculer_prix(nom):
        if nom in prix_calcules:
            return prix_calcules[nom]
        if nom not in compositions:
            prix_calcules[nom] = definitions[nom]
            return definitions[nom]
        total = 0
        for sous_nom in compositions[nom]:
            total += calculer_prix(sous_nom)
        resultat = min(total, definitions[nom])
        prix_calcules[nom] = resultat
        return resultat

    demande = input()
    resultat = calculer_prix(demande)
    print(resultat)