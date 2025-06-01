nombre_elements, diviseur = [int(i) for i in input().split()]

poids_courant = 1
nombre_iterations = 1

nombre_elements -= 1

while nombre_elements > 0:
    
    decrement = 0
    
    if poids_courant % diviseur == 0:
        decrement = poids_courant // diviseur
    else:
        decrement = poids_courant // diviseur + 1
    
    nombre_elements -= decrement
    poids_courant += decrement
    
    if nombre_elements >= 0:
        nombre_iterations += 1
        
print(nombre_iterations)