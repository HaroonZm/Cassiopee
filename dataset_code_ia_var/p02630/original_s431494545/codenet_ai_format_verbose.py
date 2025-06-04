nombre_elements = int(input())

liste_entiers = list(map(int, input().split()))

dictionnaire_occurrences = {}

for indice_element in range(nombre_elements):
    element_actuel = liste_entiers[indice_element]
    if element_actuel not in dictionnaire_occurrences:
        dictionnaire_occurrences[element_actuel] = 1
    else:
        dictionnaire_occurrences[element_actuel] += 1

nombre_requetes = int(input())

somme_actuelle = sum(liste_entiers)

for indice_requete in range(nombre_requetes):
    valeur_a_remplacer, nouvelle_valeur = map(int, input().split())
    nombre_occurrences = dictionnaire_occurrences.get(valeur_a_remplacer, 0)
    
    somme_actuelle = somme_actuelle - (nombre_occurrences * valeur_a_remplacer)
    somme_actuelle = somme_actuelle + (nombre_occurrences * nouvelle_valeur)
    
    print(somme_actuelle)
    
    if nouvelle_valeur in dictionnaire_occurrences:
        dictionnaire_occurrences[nouvelle_valeur] += nombre_occurrences
    else:
        dictionnaire_occurrences[nouvelle_valeur] = nombre_occurrences
    
    dictionnaire_occurrences[valeur_a_remplacer] = 0