texte_source = input()
motif_cible = input()

MODULO_PUISSANCE = 10 ** 9 + 7

nombre_de_sous_sequences = [0] * (len(motif_cible) + 1)
nombre_de_sous_sequences[0] = 1

for caractere_source in texte_source:
    for indice_motif in range(len(motif_cible) - 1, -1, -1):
        if caractere_source == motif_cible[indice_motif]:
            nombre_de_sous_sequences[indice_motif + 1] = (
                nombre_de_sous_sequences[indice_motif + 1] + nombre_de_sous_sequences[indice_motif]
            ) % MODULO_PUISSANCE

print(nombre_de_sous_sequences[-1])