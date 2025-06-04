texte_entree = input()

pas_de_saut = int(input())

texte_reduit = texte_entree[::pas_de_saut]

print(texte_reduit)