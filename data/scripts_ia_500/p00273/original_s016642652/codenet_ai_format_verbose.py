nombre_de_cas_tests = int(input())

for indice_cas_test in range(nombre_de_cas_tests):
    
    prix_unitaire_biere, prix_unitaire_pizza, quantite_biere, quantite_pizza = map(int, input().split())
    
    montant_achat_sans_modification = prix_unitaire_biere * quantite_biere + prix_unitaire_pizza * quantite_pizza
    
    if quantite_biere >= 5 and quantite_pizza >= 2:
        montant_total_apres_remise = int(montant_achat_sans_modification * 0.8)
        print(montant_total_apres_remise)
    
    else:
        quantite_biere_ajustee = quantite_biere if quantite_biere >= 5 else 5
        quantite_pizza_ajustee = quantite_pizza if quantite_pizza >= 2 else 2
        
        montant_achat_avec_quantites_minimum = prix_unitaire_biere * quantite_biere_ajustee + prix_unitaire_pizza * quantite_pizza_ajustee
        
        montant_total_apres_remise = int(montant_achat_avec_quantites_minimum * 0.8)
        
        if montant_achat_sans_modification <= montant_total_apres_remise:
            print(montant_achat_sans_modification)
        else:
            print(montant_total_apres_remise)