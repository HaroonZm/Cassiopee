nombre_elements_premier_ensemble = input()

ensemble_entiers_premier = set(map(int, input().split()))

nombre_elements_deuxieme_ensemble = input()

ensemble_entiers_deuxieme = set(map(int, input().split()))

difference_ensembles_ordonnee = sorted(list(ensemble_entiers_premier.difference(ensemble_entiers_deuxieme)))

if len(difference_ensembles_ordonnee) != 0:
    print('\n'.join(map(str, difference_ensembles_ordonnee)))