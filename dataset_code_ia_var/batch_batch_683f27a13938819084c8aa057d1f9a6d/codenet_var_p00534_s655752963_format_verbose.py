# Lecture du nombre de jours de formation et du nombre de jours disponibles
nombre_jours_formation, nombre_jours_disponibles = map(int, input().split())

# Lecture de la difficulté de chaque jour de formation
liste_difficultes_formations = [int(input()) for _ in range(nombre_jours_formation)]

# Lecture de la quantité d'apprentissage possible par jour disponible
liste_quantites_apprentissage = [int(input()) for _ in range(nombre_jours_disponibles)]

valeur_infinie = float("inf")

# Initialisation du tableau de programmation dynamique
cout_minimal = [
    [valeur_infinie for _ in range(nombre_jours_formation + 1)]
    for _ in range(nombre_jours_disponibles + 1)
]
cout_minimal[0][0] = 0

for indice_jour_disponible in range(nombre_jours_disponibles):

    cout_minimal[indice_jour_disponible + 1] = cout_minimal[indice_jour_disponible][0 : nombre_jours_formation + 1]

    for indice_formation_faite in range(nombre_jours_formation):

        if cout_minimal[indice_jour_disponible][indice_formation_faite] != valeur_infinie:
            nouveau_cout = (
                cout_minimal[indice_jour_disponible][indice_formation_faite]
                + liste_difficultes_formations[indice_formation_faite]
                * liste_quantites_apprentissage[indice_jour_disponible]
            )

            cout_minimal[indice_jour_disponible + 1][indice_formation_faite + 1] = min(
                cout_minimal[indice_jour_disponible + 1][indice_formation_faite + 1],
                nouveau_cout,
            )

# Affichage du coût minimum pour finir toutes les formations
print(cout_minimal[nombre_jours_disponibles][nombre_jours_formation])