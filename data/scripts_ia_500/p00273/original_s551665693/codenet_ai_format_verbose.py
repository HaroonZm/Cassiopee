nombre_de_test_cases = int(input())

for index_du_test_case in range(nombre_de_test_cases):
    
    nombre_de_crackers_x, nombre_de_crackers_y, nombre_de_boites_b, nombre_de_paquets_p = map(int, input().split())
    
    cout_avec_boites_et_paquets = nombre_de_crackers_x * nombre_de_boites_b + nombre_de_crackers_y * nombre_de_paquets_p
    
    cout_avec_reduction_statique = int((nombre_de_crackers_x * 5 + nombre_de_crackers_y * 2) * 0.8)
    
    cout_minimal_potentiel = cout_avec_boites_et_paquets
    
    if cout_avec_boites_et_paquets <= cout_avec_reduction_statique:
        print(cout_avec_boites_et_paquets)
        
    else:
        
        if 5 - nombre_de_boites_b > 0:
            cout_minimal_potentiel += (5 - nombre_de_boites_b) * nombre_de_crackers_x
            
        if 2 - nombre_de_paquets_p > 0:
            cout_minimal_potentiel += (2 - nombre_de_paquets_p) * nombre_de_crackers_y
        
        cout_final_avec_reduction = int(cout_minimal_potentiel * 0.8)
        
        print(min(cout_avec_boites_et_paquets, cout_final_avec_reduction))