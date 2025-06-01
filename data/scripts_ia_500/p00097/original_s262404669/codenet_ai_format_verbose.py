tableau_comptage = [[0] * 1001 for ligne in range(10)]

tableau_comptage[0][0] = 1

for somme_actuelle in range(101):
    
    for nombre_elements in range(9, 0, -1):
        
        for valeur_somme in range(somme_actuelle, 1000):
            
            tableau_comptage[nombre_elements][valeur_somme] += tableau_comptage[nombre_elements - 1][valeur_somme - somme_actuelle]

while True:
    
    entree_somme, nombre_elements_utilises = map(int, raw_input().split())
    
    if entree_somme == 0 and nombre_elements_utilises == 0:
        break
    
    print tableau_comptage[entree_somme][nombre_elements_utilises]