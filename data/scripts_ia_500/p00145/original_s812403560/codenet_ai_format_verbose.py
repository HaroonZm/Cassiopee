nombre_cartes = int(input())

liste_cartes = []

for indice_carte in range(nombre_cartes):
    
    largeur, hauteur = map(int, input().split())
    
    liste_cartes.append((largeur, hauteur))


memoisation_couts = [[-1 for _ in range(nombre_cartes + 1)] for _ in range(nombre_cartes + 1)]


def calculer_cout_minimal(intervalle_gauche, intervalle_droit, cartes):
    
    if memoisation_couts[intervalle_gauche][intervalle_droit] == -1:
        
        if intervalle_gauche + 1 == intervalle_droit:
            
            memoisation_couts[intervalle_gauche][intervalle_droit] = 0
        
        else:
            
            cout_minimal = 1 << 32  
            
            for point_coupure in range(intervalle_gauche + 1, intervalle_droit):
                
                cout_courant = (
                    cartes[intervalle_gauche][0]
                    * cartes[point_coupure - 1][1]
                    * cartes[point_coupure][0]
                    * cartes[intervalle_droit - 1][1]
                    + calculer_cout_minimal(intervalle_gauche, point_coupure, cartes)
                    + calculer_cout_minimal(point_coupure, intervalle_droit, cartes)
                )
                
                if cout_courant < cout_minimal:
                    cout_minimal = cout_courant
            
            memoisation_couts[intervalle_gauche][intervalle_droit] = cout_minimal
    
    
    return memoisation_couts[intervalle_gauche][intervalle_droit]


cout_total_minimal = calculer_cout_minimal(0, nombre_cartes, liste_cartes)

print(cout_total_minimal)