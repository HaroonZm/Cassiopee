def print_board(A,n):
	# Fonction pour afficher le plateau A de taille n x n.
	# A est une liste de listes (matrice) contenant des entiers.
	# n est un entier représentant la dimension du plateau.
	for i in range(n):
		# Pour chaque ligne i (de 0 à n-1) du plateau A:
		s = ""  # Initialisation d'une chaîne vide s pour construire la ligne à afficher.
		for j in range(n):
			# Pour chaque colonne j (de 0 à n-1) dans la ligne i:
			st = str(A[i][j])  # Conversion de l'entier en chaîne de caractères.
			# Le but ici est d'ajouter des espaces devant le nombre pour l'aligner.
			if len(st) == 1:
				# Si le nombre a une longueur de 1 caractère (ex: "5")
				s += "   "  # Ajouter trois espaces pour que les chiffres s'alignent à droite.
			elif len(st) == 2:
				# Si le nombre a une longueur de 2 caractères (ex: "10")
				s += "  "  # Ajouter deux espaces devant.
			elif len(st) == 3:
				# Si le nombre a une longueur de 3 caractères (ex: "100")
				s += " "  # Ajouter un espace devant.
			# Ajouter le nombre converti à la chaîne s.
			s += st
		# Après avoir parcouru toute la ligne, afficher la chaîne s.
		print(s)

def check_leftdown(A,h,w,n):
	# Fonction pour calculer la nouvelle position (h, w) si on doit aller "en bas à gauche"
	# A est la matrice du plateau,
	# h et w sont les indices actuels de la position (hauteur, largeur),
	# n est la dimension de la matrice.
	if h + 1 > n - 1:
		# Si on essaie d'aller une ligne plus bas que la limite (hors plateau):
		# Cela signifie que l'on sort par le bas.
		# Selon la règle, on doit alors descendre d'une colonne vers la gauche.
		w -= 1  # On déplace la colonne vers la gauche.

		for x in range(n):
			# On cherche dans cette nouvelle colonne w une ligne x où la case est vide (0).
			if A[x][w] == 0:
				# Dès qu'on trouve une case vide, on met à jour h (la ligne) à cet indice x.
				h = x
				break  # On arrête la recherche.

	else:
		# Si on ne sort pas par le bas (on peut aller à la ligne suivante):
		if w - 1 < 0:
			# Si en allant à gauche on sort par la colonne (w-1 < 0),
			# c’est-à-dire qu'on dépasse le bord gauche du plateau:
			w = n  # On remet la colonne à n (hors limite à droite),
			h += 1  # et on descend d'une ligne.
		else:
			# Sinon, on peut aller en bas à gauche normalement.
			h += 1  # On descend d'une ligne (hauteur + 1).
			w -= 1  # On recule d'une colonne (largeur - 1).
	# Retourner la nouvelle position (h, w) calculée.
	return h,w

def check_rightdown(A,h,w,n):
	# Fonction pour calculer la nouvelle position (h, w) si on doit aller "en bas à droite"
	# A est la matrice du plateau,
	# h et w sont les indices actuels (hauteur, largeur),
	# n est la dimension du plateau.
	if h + 1 > n - 1:
		# Si on tente de descendre hors du plateau par le bas:
		if w + 1 > n - 1:
			# Si on dépasse aussi la colonne de droite,
			# on est totalement hors limite, rien à faire dans ce cas.
			# "None" ici sert à indiquer aucune action, simplement un espace réservé.
			None
		else:
			# Si on ne sort pas à droite, on déplace la colonne vers la droite.
			w += 1  # Colonne +1

		for x in range(n):
			# On cherche dans la colonne w une ligne x avec une case vide.
			if A[x][w] == 0:
				h = x  # Trouvé case vide, mise à jour de la ligne.
				break  # Stop à la première case vide.

	else:
		# Si on ne sort pas par le bas:
		if w + 1 > n - 1:
			# Si en allant vers la droite on sort du plateau,
			# on revient à la colonne 0 et on descend d'une ligne.
			w = 0
			h += 1
		else:
			# Cas normal où on peut aller en diagonale bas droite.
			h += 1  # Descendre d'une ligne.
			w += 1  # Avancer d'une colonne.

			if A[h][w] != 0:
				# Si la case visée est déjà occupée (pas zéro),
				# on doit alors vérifier la position en bas à gauche.
				h,w = check_leftdown(A,h,w,n)

	# Retourner la nouvelle position calculée.
	return h,w

if __name__ == '__main__':
	# Point d'entrée principal du script.
	# On répète indéfiniment jusqu'à ce que l'utilisateur saisisse 0 ou que la saisie soit terminée.
	while True:
		try:
			n = int(input())
			# Lire la dimension n du plateau, convertie en entier.

			if n == 0:
				# Si n vaut 0, on arrête la boucle et donc le programme.
				break

			# Initialisation d'une matrice n x n remplie de zéros.
			# La compréhension de liste crée une liste contenant n éléments,
			# chacun étant une liste de n zéros.
			A = [[0 for i in range(n)] for j in range(n)]

			# Nombre total d'éléments à placer sur le plateau.
			cnt = n * n

			for x in range(cnt):
				# On itère de 0 à cnt-1 pour remplir la matrice.
				if x == 0:
					# Pour la première valeur (x=0) on calcule le point de départ.
					mid = n // 2  # Calcul du milieu (division entière).
					h = mid + 1   # La ligne est le milieu + 1.
					w = mid       # La colonne est juste le milieu.
					A[h][w] = x + 1  # La valeur placée est 1 (pas 0)
				else:
					# Pour les suivantes, on calcule la prochaine position selon les règles.
					h,w = check_rightdown(A,h,w,n)
					A[h][w] = x+1  # On place la valeur x+1 à cette position.

			# Affichage final du plateau rempli.
			print_board(A,n)

		except EOFError:
			# Si on arrive à la fin du fichier (pas de plus d'input),
			# on sort proprement de la boucle while et termine le programme.
			break