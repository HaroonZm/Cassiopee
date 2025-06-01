if __name__ == '__main__':
    
    nombre_entier = int(input())
    
    for exposant_puissance in range(21):
        
        valeur_puissance_deux = pow(2, exposant_puissance)
        
        if nombre_entier < valeur_puissance_deux:
            
            if exposant_puissance == 0:
                
                print(1)
                
            else:
                
                puissance_precedente = pow(2, exposant_puissance - 1)
                
                print(puissance_precedente)
                
            break
        
        elif nombre_entier == valeur_puissance_deux:
            
            print(valeur_puissance_deux)
            
            break