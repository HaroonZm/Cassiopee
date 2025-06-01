nombre_elements, _, _ = map(int, input().split())

liste_elements = list(range(nombre_elements))
indice_courant = 0

valeurs_premier_tour = map(int, input().split())

for valeur in valeurs_premier_tour:
    
    if valeur & 1:
        indice_courant -= valeur
    else:
        indice_courant += valeur
    
    indice_courant %= nombre_elements
    
    del liste_elements[indice_courant]
    
    nombre_elements -= 1

valeurs_deuxieme_tour = map(int, input().split())

for valeur in valeurs_deuxieme_tour:
    
    presence = int(valeur in liste_elements)
    
    print(presence)