nombre_unites_par_paquet, nombre_unites_requises = map(int, input("Entrez le nombre d'unités par paquet et le nombre total d'unités requises, séparés par un espace : ").split())

nombre_de_paquets_necessaires = (nombre_unites_requises + nombre_unites_par_paquet - 1) // nombre_unites_par_paquet

print(nombre_de_paquets_necessaires)