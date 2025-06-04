base_petite = int(input("Entrez la longueur de la petite base du trapèze : "))
base_grande = int(input("Entrez la longueur de la grande base du trapèze : "))
hauteur_trapeze = int(input("Entrez la hauteur du trapèze : "))

aire_trapeze = int(((base_petite + base_grande) * hauteur_trapeze) / 2)

print(aire_trapeze)