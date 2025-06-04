import itertools

nombre_elements_liste = int(input())

liste_entiers = list(map(int, input().split()))

paires_deux_elements = itertools.combinations(liste_entiers, 2)

for premier_element, second_element in paires_deux_elements:
    
    difference_absolue = abs(premier_element - second_element)
    
    reste_modulo_nombre_elements_moins_un = difference_absolue % (nombre_elements_liste - 1)
    
    if reste_modulo_nombre_elements_moins_un == 0:
        
        print(premier_element, second_element)
        
        break