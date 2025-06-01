nombre_palindromes = 0

while True:
    
    try:
        
        chaine_utilisateur = input()
        
        if chaine_utilisateur == chaine_utilisateur[::-1]:
            nombre_palindromes += 1
            
    except:
        break

print(nombre_palindromes)