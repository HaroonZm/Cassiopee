nombre_elements = 10000
primes_crible = [0, 0] + [1] * (nombre_elements - 2)

limite_boucle = 100

for nombre_potentiel in range(2, limite_boucle):
    
    multiple = nombre_potentiel * nombre_potentiel
    
    while multiple < nombre_elements:
        
        primes_crible[multiple] = 0
        
        multiple += nombre_potentiel


while True:
    
    nombre_saisi = int(input())
    
    if nombre_saisi == 0:
        break
    
    for nombre_candidat in range(nombre_saisi, 1, -1):
        
        indice_premier = nombre_candidat - 2
        
        if primes_crible[indice_premier] and primes_crible[nombre_candidat]:
            
            print(indice_premier, nombre_candidat)
            
            break