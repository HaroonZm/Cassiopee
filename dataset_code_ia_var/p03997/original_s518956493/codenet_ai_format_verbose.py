base_petite = int(input())
base_grande = int(input())
hauteur_trapeze = int(input())

somme_bases = base_petite + base_grande
produit_somme_hauteur = somme_bases * hauteur_trapeze
aire_trapeze = produit_somme_hauteur // 2

print(aire_trapeze)