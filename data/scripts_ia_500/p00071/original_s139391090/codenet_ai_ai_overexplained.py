from itertools import chain  # Importe la fonction 'chain' du module 'itertools', utilisée pour combiner plusieurs itérables en un seul

# Création d'une liste 'explosion' qui contient des entiers allant de -3 à 3, sauf zéro, puis suivi de six zéros
# Le 'range(-3, 4)' génère une séquence d'entiers de -3 à 3 inclus
# La compréhension de liste '[i for i in range(-3, 4) if i]' garde seulement les entiers différents de 0
# Ensuite on ajoute '[0] * 6', soit six zéros consécutifs, ce qui étend la liste
explosion = [i for i in range(-3, 4) if i] + [0] * 6

# Définition de la fonction 'bomb' qui prend deux arguments, les coordonnées x et y
def bomb(x, y):
	# On modifie l'élément de la variable globale 'field' à la position y (ligne), x (colonne) en le mettant à zéro
	# Cela représente probablement l'explosion d'une bombe qui vide ou détruit la case
	field[y][x] = 0
	
	# On parcourt simultanément deux listes : 'explosion' et sa version inversée 'reversed(explosion)'
	# La fonction 'zip' crée des paires (dx, dy) d'éléments issus respectivement des deux listes
	for dx, dy in zip(explosion, reversed(explosion)):
		# Calcul des nouvelles coordonnées 'nextX' et 'nextY' déterminées par l'ajout de ces décalages dx et dy à x et y
		nextX = x + dx
		nextY = y + dy
		
		# Vérification que ces coordonnées 'nextX' et 'nextY' sont dans les limites valides, ici entre 0 et 7 inclus (car range(0,8) produit 0 à 7)
		if nextX in range(0, 8) and nextY in range(0, 8):
			# Si la case 'field[nextY][nextX]' vaut 1, on rappelle récursivement la fonction 'bomb' sur cette case
			# Cela simule probablement la propagation de l'explosion vers les cases contenant 1
			if field[nextY][nextX] == 1:
				bomb(nextX, nextY)
			# Quelle que soit la valeur initiale, on met la case 'field[nextY][nextX]' à 0 après l'explosion
			field[nextY][nextX] = 0

# Boucle principale qui s'exécute un nombre de fois donné par la fonction 'input()'
# 'xrange' est une fonction Python 2 qui génère une séquence d'entiers sans stocker la liste entière en mémoire (plus efficace)
for i in xrange(input()):
	# Lecture d'une entrée non utilisée ('raw_input()' lit une ligne de texte depuis l'entrée standard)
	raw_input()
	
	# Création de la variable 'field' qui est une liste de listes (une matrice 8x8)
	# Chaque sous-liste est créée par la conversion en entiers de chaque caractère lu sur une ligne d'entrée
	# On fait cela 8 fois pour obtenir 8 lignes
	field = [[int(c) for c in raw_input()] for j in range(8)]
	
	# Lecture et conversion des coordonnées x et y depuis l'entrée standard, en soustrayant 1 pour passer d'un index de base 1 à base 0
	x = input() - 1
	y = input() - 1
	
	# Appel de la fonction 'bomb' sur ces coordonnées, ce qui modifie 'field' en fonction des règles expliquées précédemment
	bomb(x, y)
	
	# Affichage du texte "Data N:" où N est le numéro courant de l'itération (i+1 car i commence à 0)
	print "Data %d:" % (i + 1)
	
	# Pour chaque ligne 'f' dans 'field', on convertit chaque entier en chaîne et on rassemble tous ces caractères en une seule chaîne
	# Puis on imprime cette chaîne (une ligne du champ modifié)
	for f in field:
		print "".join(str(i) for i in f)