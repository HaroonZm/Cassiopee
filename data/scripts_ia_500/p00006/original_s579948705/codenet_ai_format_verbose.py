ligne_entree = raw_input().strip()

caracteres_inverses = reversed(ligne_entree)

somme_caracteres = reduce(lambda caractere_cumule, caractere_courant: caractere_cumule + caractere_courant, caracteres_inverses)

print(somme_caracteres)