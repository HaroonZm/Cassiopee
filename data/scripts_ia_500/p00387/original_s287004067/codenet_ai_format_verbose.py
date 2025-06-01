nombre_elements_par_ligne, total_elements = list(map(int, input().split()))

quotient = total_elements // nombre_elements_par_ligne
reste = total_elements % nombre_elements_par_ligne

nombre_de_lignes = quotient + (1 if reste != 0 else 0)
nombre_de_lignes = max(nombre_de_lignes, 1)

print(nombre_de_lignes)