tableau_a, tableau_b, tableau_c = [0] * 200, [0] * 200, [0] * 200

def supprimer_valeurs_dupliquees(liste_valeurs, taille_liste):
    
    for indice_courant in range(taille_liste - 1):
        
        if not liste_valeurs[indice_courant]:
            continue
        
        valeur_courante = liste_valeurs[indice_courant]
        
        for indice_suivant in range(indice_courant + 1, taille_liste):
            
            if valeur_courante == liste_valeurs[indice_suivant]:
                liste_valeurs[indice_courant] = 0
                liste_valeurs[indice_suivant] = 0

if __name__ == '__main__':
    
    nombre_elements = int(input())
    
    for index in range(nombre_elements):
        valeur_a, valeur_b, valeur_c = map(int, input().split())
        tableau_a[index] = valeur_a
        tableau_b[index] = valeur_b
        tableau_c[index] = valeur_c
    
    supprimer_valeurs_dupliquees(tableau_a, nombre_elements)
    supprimer_valeurs_dupliquees(tableau_b, nombre_elements)
    supprimer_valeurs_dupliquees(tableau_c, nombre_elements)
    
    for index in range(nombre_elements):
        print(tableau_a[index] + tableau_b[index] + tableau_c[index])