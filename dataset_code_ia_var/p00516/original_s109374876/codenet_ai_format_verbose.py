# Lecture des entrées : nombre de candidats et nombre de notes
nombre_de_candidats, nombre_de_notes = map(int, input().split())

# Lecture des scores des candidats
liste_scores_candidats = [int(input()) for index_candidat in range(nombre_de_candidats)]

# Lecture des notes attribuées
liste_notes_attribuees = [int(input()) for index_note in range(nombre_de_notes)]

# Initialisation d'une liste de compteurs pour chaque candidat
compteur_attributions_notes = [0 for index_candidat in range(nombre_de_candidats)]

# Parcours de chaque note attribuée
for index_note in range(nombre_de_notes):
    note_courante = liste_notes_attribuees[index_note]
    for index_candidat in range(nombre_de_candidats):
        score_candidat = liste_scores_candidats[index_candidat]
        if score_candidat <= note_courante:
            compteur_attributions_notes[index_candidat] += 1
            break

# Recherche du nombre maximal d'attributions
maximum_notes_attribuees = max(compteur_attributions_notes)

# Recherche de l'indice du premier candidat ayant reçu ce nombre maximal de notes
indice_candidat_majoritaire = compteur_attributions_notes.index(maximum_notes_attribuees) + 1

# Affichage du résultat
print(indice_candidat_majoritaire)