def convert_number_with_units():
	"""
	Lit des paires d'entiers (m, n) depuis l'entrée standard et convertit m élevé à la puissance n en une 
	représentation abrégée utilisant des unités spécifiques.
	
	La conversion continue jusqu'à ce que m soit égal à 0, ce qui arrête la boucle.
	
	La sortie représente le nombre en divisant par puissances de 10^4 et en ajoutant l'unité correspondante.
	"""
	
	while True:
		# Lecture de deux entiers m et n séparés par un espace
		m, n = map(int, input().split())
		
		# Condition d'arrêt si m vaut 0
		if m == 0:
			break
		
		# Calcul de m à la puissance n
		m **= n
		
		# Initialisation de la chaîne résultat
		s = ""
		
		# Définition de la plus grande puissance de dix à examiner, en multiples de 4
		d = 68
		
		# Liste des unités associées aux puissances de 10^4, inversée pour alignement avec l'ordre des puissances
		ls = [
			'Mts', 'Fks', 'Nyt', 'Asg', 'Ggs', 'Gok', 'Sai', 'Sei', 'Kan',
			'Ko', 'Jou', 'Jo', 'Gai', 'Kei', 'Cho', 'Oku', 'Man'
		][::-1]
		
		# Parcours des puissances de 10^4 du plus grand multiple (68) vers 0
		while d:
			# Calcul du coefficient pour l'unité courante
			coef = int(m / 10**d)
			
			# Si le coefficient est au moins 1, on ajoute sa représentation à la chaîne résultat
			if coef >= 1:
				# Ajout du coefficient suivi de l'unité correspondante
				s += str(coef) + ls[int((d - 4) / 4)]
				
				# On enlève cette partie du nombre pour poursuivre avec les puissances inférieures
				m %= 10**d
			
			# On descend à la puissance inférieure de 4
			d -= 4
		
		# Ajout du reste qui est inférieur à 10^4 si non nul
		if m:
			s += str(m)
		
		# Affichage du résultat final pour cette paire m, n
		print(s)