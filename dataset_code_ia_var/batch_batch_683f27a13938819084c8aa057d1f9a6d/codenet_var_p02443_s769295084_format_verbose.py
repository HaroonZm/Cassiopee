nombre_elements_tableau = int(input())

tableau_entiers = list(map(int, input().split()))

nombre_de_requetes = int(input())

for indice_requete in range(nombre_de_requetes):
    
    debut_segment, fin_segment = map(int, input().split())
    
    segment_avant = tableau_entiers[:debut_segment]
    
    segment_a_inverser = tableau_entiers[debut_segment:fin_segment][::-1]
    
    segment_apres = tableau_entiers[fin_segment:]
    
    tableau_entiers = segment_avant + segment_a_inverser + segment_apres

print(*tableau_entiers)