nombre_elem_ensemble_1 = int(input())

ensemble_premier = set(map(int, input().split()))

nombre_elem_ensemble_2 = int(input())

ensemble_deuxieme = set(map(int, input().split()))

intersection_ensembles = ensemble_premier & ensemble_deuxieme

taille_intersection = len(intersection_ensembles)

print(taille_intersection)