nombre_decalage = int(input())

texte_original = input()

texte_chiffre = ""

for index_caractere in range(len(texte_original)):
    
    code_ascii_caractere = ord(texte_original[index_caractere])
    
    code_ascii_decale = code_ascii_caractere + nombre_decalage
    
    if code_ascii_decale <= 90:
        texte_chiffre += chr(code_ascii_decale)
    else:
        texte_chiffre += chr(code_ascii_decale - 26)

print(texte_chiffre)