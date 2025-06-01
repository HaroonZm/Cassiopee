texte_source = input()
texte_cible = input()

MODULO = 10**9 + 7

comptages_sous_sequences = [0] * (len(texte_cible) + 1)
comptages_sous_sequences[0] = 1

for caractere_source in texte_source:
    
    for index_cible in range(len(texte_cible) - 1, -1, -1):
        
        if caractere_source == texte_cible[index_cible]:
            
            comptages_sous_sequences[index_cible + 1] = (comptages_sous_sequences[index_cible + 1] + comptages_sous_sequences[index_cible]) % MODULO

print(comptages_sous_sequences[-1])