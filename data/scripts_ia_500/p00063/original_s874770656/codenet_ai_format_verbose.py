nombre_de_palindromes=0

while True:
    
    try:
        chaine_entree = str(input())
        
        if chaine_entree == chaine_entree[::-1]:
            nombre_de_palindromes += 1
            
    except:
        break

print(nombre_de_palindromes)