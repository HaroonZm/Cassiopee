nombre_de_matrices = int(raw_input())

dimensions_des_matrices = [[] for _ in range(nombre_de_matrices)]

couts_minimaux = {}

for index_matrice in range(nombre_de_matrices):
    
    dimensions_des_matrices[index_matrice] = map(int, raw_input().split())
    
    couts_minimaux[(index_matrice, index_matrice)] = 0

for longueur_sequence in range(1, nombre_de_matrices):
    
    for indice_debut in range(nombre_de_matrices - longueur_sequence):
        
        indice_fin = indice_debut + longueur_sequence
        
        couts_possibles = []
        
        for indice_diviseur in range(indice_debut, indice_fin):
            
            cout_multiplication = (
                dimensions_des_matrices[indice_debut][0] *
                dimensions_des_matrices[indice_diviseur][1] *
                dimensions_des_matrices[indice_diviseur + 1][0] *
                dimensions_des_matrices[indice_fin][1]
            )
            
            cout_total = (
                cout_multiplication +
                couts_minimaux[(indice_debut, indice_diviseur)] +
                couts_minimaux[(indice_diviseur + 1, indice_fin)]
            )
            
            couts_possibles.append(cout_total)
        
        couts_minimaux[(indice_debut, indice_fin)] = min(couts_possibles)

print couts_minimaux[(0, nombre_de_matrices - 1)]