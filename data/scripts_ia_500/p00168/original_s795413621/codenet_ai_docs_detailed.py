def up(n):
	"""
	Calcule la n-ième valeur d'une séquence définie par des conditions initiales
	et une relation de récurrence.

	La séquence commence avec les trois premiers éléments fixés à 1, 2 et 4.
	Chaque élément suivant est la somme des trois éléments précédents.

	Par exemple:
		up(1) = 1
		up(2) = 2
		up(3) = 4
		up(4) = up(1) + up(2) + up(3) = 1 + 2 + 4 = 7
		...

	Args:
		n (int): L'indice de la valeur à calculer dans la séquence.

	Returns:
		int: La n-ième valeur de la séquence.
	"""
	# Initialisation d'une liste goal de taille n avec des zéros
	goal = [0 for i in range(n)]
	# Affectation des trois premières valeurs fixes
	goal[:3] = [1, 2, 4]
	# Calcul des valeurs suivantes à partir de la somme des trois précédentes
	for i in range(3, n):
		goal[i] = sum(goal[i-3:i])
	# Retourne la dernière valeur calculée, celle à l'indice n-1
	return goal[-1]

while True:
	"""
	Boucle infinie demandant une entrée utilisateur, traitant l'entrée,
	et affichant un résultat jusqu'à ce que l'entrée soit zéro,
	ce qui interrompt la boucle.
	"""
	# Lecture de l'entrée utilisateur comme un entier
	n = int(raw_input())
	# Condition d'arrêt : si l'entrée est 0, on sort de la boucle
	if n == 0:
		break
	# Calcul de la valeur avec la fonction up
	val = up(n)
	# Application de la formule sur la valeur retournée
	# (val // 10 + 1) // 365 + 1 correspond à une transformation numérique spécifique
	result = ((val // 10 + 1) // 365) + 1
	# Affichage du résultat final
	print(result)