# Lecture du nombre de participants et du nombre de nouvelles valeurs
nombre_participants, nombre_nouvelles_valeurs = map(int, raw_input().split())

# Lecture de toutes les valeurs (anciennes et nouvelles)
liste_valeurs = [input() for indice_valeur in range(nombre_participants + nombre_nouvelles_valeurs)]

# Initialisation du dictionnaire pour compter le nombre de victoires de chaque participant
compteur_victoires_participant = {indice_participant: 0 for indice_participant in range(nombre_participants)}

# Pour chaque nouvelle valeur, détermination du participant battu et incrémentation
for indice_nouvelle_valeur in range(nombre_participants, nombre_participants + nombre_nouvelles_valeurs):
    
    for indice_participant in range(nombre_participants):
        
        if liste_valeurs[indice_nouvelle_valeur] >= liste_valeurs[indice_participant]:
            
            compteur_victoires_participant[indice_participant] += 1
            break

# Recherche du participant ayant le plus grand nombre de victoires
participant_avec_max_victoires = sorted(
    compteur_victoires_participant.items(),
    key=lambda element_tuple: element_tuple[1],
    reverse=True
)[0][0]

# Affichage de l'indice du participant (en commençant à 1)
print participant_avec_max_victoires + 1