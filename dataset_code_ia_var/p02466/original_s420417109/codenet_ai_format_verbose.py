# Lecture de la première ligne (taille de l'ensemble A, non utilisée ici)
taille_ensemble_A = input()

# Lecture et création de l'ensemble A à partir des entiers saisis
ensemble_A = set(int(element_entier) for element_entier in input().split())

# Lecture de la deuxième ligne (taille de l'ensemble B, non utilisée ici)
taille_ensemble_B = input()

# Lecture et création de l'ensemble B à partir des entiers saisis
ensemble_B = set(int(element_entier) for element_entier in input().split())

# Calcul de la différence symétrique (éléments présents dans un seul ensemble) et tri
elements_difference_symetrique_tries = sorted((ensemble_A | ensemble_B) - (ensemble_A & ensemble_B))

# Affichage des éléments un par un
for entier in elements_difference_symetrique_tries:
    print(entier)