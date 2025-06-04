nombre_de_lignes_a_traiter = int(input())

ensemble_de_groupes_uniques = set()

for index_ligne in range(nombre_de_lignes_a_traiter):
    
    elements_de_la_ligne = map(int, input().split())
    
    groupe_trie = tuple(sorted(elements_de_la_ligne))
    
    ensemble_de_groupes_uniques.add(groupe_trie)

nombre_groupes_duplicates = nombre_de_lignes_a_traiter - len(ensemble_de_groupes_uniques)

print(nombre_groupes_duplicates)