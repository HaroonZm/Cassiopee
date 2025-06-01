# AOJ 0160 Delivery Fee
# Python3 2018.6.18 bal4u

# tbl est une liste contenant les frais de livraison possibles,
# chaque position i dans la liste correspond à un palier de frais.
# Par exemple, tbl[0] = 600 signifie que le frais minimal est 600,
# tbl[1] = 800 signifie un palier supérieur à 800, etc.
tbl = [600, 800, 1000, 1200, 1400, 1600]

# Une boucle infinie while True commence, cela signifie
# que le programme tournera jusqu'à ce qu'une condition d'arrêt soit rencontrée.
while True:
	# Lecture de l'entrée utilisateur convertie en entier,
	# représentant le nombre de colis à traiter.
	n = int(input())
	# Si l'utilisateur saisit 0, cela signifie que le programme doit s'arrêter,
	# donc on utilise break pour sortir de la boucle infinie.
	if n == 0:
		break

	# Initialisation de la variable fee à 0.
	# Cette variable va cumuler le total des frais de livraison pour tous les colis.
	fee = 0

	# Une boucle for va s'exécuter n fois,
	# c’est-à-dire une fois par colis à traiter.
	for i in range(n):
		# Lecture d'une ligne d'entrée qui contient 4 entiers séparés par des espaces :
		# x, y, h, w représentent respectivement deux dimensions, une hauteur et un poids.
		# La fonction input() lit la ligne, split() sépare la chaîne en quatre éléments,
		# map(int, ...) convertit chaque élément en entier,
		# list(...) transforme le résultat en liste pour pouvoir affecter facilement aux variables.
		x, y, h, w = list(map(int, input().split()))

		# Calcul de la somme s des dimensions x, y, h.
		# Cette somme est utilisée pour déterminer la catégorie de taille du colis.
		s = x + y + h

		# On vérifie si le colis respecte certaines conditions:
		# si la somme s des dimensions est inférieure ou égale à 160,
		# et si le poids w est inférieur ou égal à 25,
		# alors le colis peut être tarifé selon la grille prédéfinie.
		if s <= 160 and w <= 25:
			# Initialisation de k1 et k2 à 0.
			# k1 correspondra à un index basé sur la taille (s),
			# k2 correspondra à un index basé sur le poids (w).
			k1 = k2 = 0

			# si la somme s des dimensions est inférieure ou égale à 60,
			# alors k1 reste 0, le palier minimal.
			if s <= 60:
				k1 = 0
			else:
				# Sinon, on calcule un palier supérieur en soustrayant 61 à s,
				# puis en divisant par 20, on prend la partie entière de la division.
				# On ajoute 1 car l'indexation commence après le palier minimal.
				k1 = (s - 61) // 20 + 1

			# si le poids w est inférieur ou égal à 2 kg,
			# alors k2 reste 0, correspondant au palier minimal.
			if w <= 2:
				k2 = 0
			else:
				# Sinon, on calcule un palier poids avec une formule similaire:
				# on soustrait 1, divise par 5 en quotient entier, puis ajoute 1.
				k2 = (w - 1) // 5 + 1

			# Le palier final k1 est le plus grand entre k1 et k2,
			# ce qui signifie qu'on applique la pénalité maximale entre taille et poids.
			if k1 < k2:
				k1 = k2

			# On ajoute au total fee la valeur dans tbl correspondant à l'index k1,
			# c'est-à-dire le montant des frais pour ce colis.
			fee += tbl[k1]

	# Après avoir traité tous les colis, on affiche le total fee correspondant.
	print(fee)