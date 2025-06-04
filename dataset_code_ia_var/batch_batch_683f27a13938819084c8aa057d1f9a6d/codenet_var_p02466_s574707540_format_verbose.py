nombre_elements_premier_ensemble = input()

elements_premier_ensemble = set(
    map(int, input().split())
)

nombre_elements_deuxieme_ensemble = input()

elements_deuxieme_ensemble = set(
    map(int, input().split())
)

elements_uniquement_dans_un_ensemble = elements_premier_ensemble.symmetric_difference(
    elements_deuxieme_ensemble
)

elements_ordonnes = sorted(elements_uniquement_dans_un_ensemble)

for element in elements_ordonnes:
    print(element)