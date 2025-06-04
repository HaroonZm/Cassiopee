nombre_total_elements, nombre_de_retirades = map(int, input().split())

liste_entiers = list(map(int, input().split()))

somme_des_plus_petits_elements = 0

for indice_retirade in range(nombre_de_retirades):
    
    plus_petit_element = min(liste_entiers)
    
    somme_des_plus_petits_elements += plus_petit_element
    
    liste_entiers.remove(plus_petit_element)

print(somme_des_plus_petits_elements)