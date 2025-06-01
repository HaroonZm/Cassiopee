import math


while True:
    
    nombre_a_cubiquer = int(input())
    
    if nombre_a_cubiquer == -1:
        break
    
    estimation_racine_cubique = nombre_a_cubiquer / 2.0
    
    while True:
        
        difference_relative = math.fabs((estimation_racine_cubique ** 3) - nombre_a_cubiquer)
        
        if difference_relative < 0.00001 * nombre_a_cubiquer:
            break
        
        derivee = 3 * (estimation_racine_cubique ** 2)
        
        estimation_racine_cubique = estimation_racine_cubique - ((estimation_racine_cubique ** 3) - nombre_a_cubiquer) / derivee
    
    print(f'{estimation_racine_cubique:.6f}')