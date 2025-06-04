nombre_de_caracteres_a_decaler = int(input())

chaine_a_chiffrer = input()

alphabet_majuscule = [chr(ord('A') + index_lettre) for index_lettre in range(26)]

chaine_chiffree = []

for caractere in chaine_a_chiffrer:
    
    code_ascii_decale = (ord(caractere) + nombre_de_caracteres_a_decaler - ord('A')) % 26 + ord('A')
    
    caractere_chiffre = chr(code_ascii_decale)
    
    chaine_chiffree.append(caractere_chiffre)

chaine_chiffree_jointe = "".join(chaine_chiffree)

print(chaine_chiffree_jointe)