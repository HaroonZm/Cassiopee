def calculer_cout_minimal(poids_total):
    
    cout_minimal = 1e9
    
    for nombre_bottes_500g in range(poids_total // 500 + 1):
        
        poids_restant_apres_500g = poids_total - nombre_bottes_500g * 500
        
        for nombre_bottes_300g in range(poids_restant_apres_500g // 300 + 1):
            
            poids_restant_apres_300g = poids_restant_apres_500g - nombre_bottes_300g * 300
            
            if poids_restant_apres_300g % 200 == 0:
                
                nombre_bottes_200g = poids_restant_apres_300g // 200
                
                combinaison_bottes = [nombre_bottes_200g, nombre_bottes_300g, nombre_bottes_500g]
                
                cout_combinaison = calculer_cout_combinaison(combinaison_bottes)
                
                if cout_combinaison < cout_minimal:
                    
                    cout_minimal = cout_combinaison
                    
    return cout_minimal


def calculer_cout_combinaison(nombre_bottes_par_type):
    
    prix_unitaire = [380, 550, 850]
    reduction_proportionnelle = [0.2, 0.15, 0.12]
    seuil_reduction = [5, 4, 3]
    
    cout_total = 0
    
    for index_type in range(3):
        
        quantite = nombre_bottes_par_type[index_type]
        
        facteur_reduction = int(quantite / seuil_reduction[index_type]) * reduction_proportionnelle[index_type]
        
        cout_produit = prix_unitaire[index_type] * quantite * (1 - facteur_reduction)
        
        cout_total += cout_produit
        
    return cout_total


while True:
    
    poids_saisi = input()
    
    if poids_saisi == '0':
        break
    
    poids = int(poids_saisi)
    
    cout_minimal_total = calculer_cout_minimal(poids)
    
    print(int(cout_minimal_total))