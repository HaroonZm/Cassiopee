# Lecture de la saisie utilisateur, séparation et conversion en entiers
entree_utilisateur = raw_input()

liste_nombres = map(int, entree_utilisateur.split())

# Tri de la liste obtenue
liste_triee = sorted(liste_nombres)

# Affichage des trois premiers éléments triés sur une seule ligne
print liste_triee[0], liste_triee[1], liste_triee[2]