ensemble_entiers_uniques = set(
    map(
        int,
        input("Entrez une liste d'entiers séparés par des espaces : ").split()
    )
)

nombre_elements_uniques = len(ensemble_entiers_uniques)

print(nombre_elements_uniques)