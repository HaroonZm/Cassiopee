nombre_de_cartes = int(raw_input())

cartes_dimension = [[] for _ in range(nombre_de_cartes)]

cout_minimal = {}

for index_carte in range(nombre_de_cartes):
    
    cartes_dimension[index_carte] = map(int, raw_input().split())
    
    cout_minimal[(index_carte, index_carte)] = 0

for longueur_sequence in range(1, nombre_de_cartes):
    
    for position_debut in range(nombre_de_cartes - longueur_sequence):
        
        position_fin = position_debut + longueur_sequence
        
        cout_minimal[(position_debut, position_fin)] = min(
            
            [
                cartes_dimension[position_debut][0] * cartes_dimension[separation][1] * cartes_dimension[separation + 1][0] * cartes_dimension[position_fin][1]
                + cout_minimal[(position_debut, separation)]
                + cout_minimal[(separation + 1, position_fin)]
                for separation in range(position_debut, position_fin)
            ]
        )

print cout_minimal[(0, nombre_de_cartes - 1)]