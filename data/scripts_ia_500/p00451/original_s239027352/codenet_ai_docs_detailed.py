def longest_common_substring():
	"""
	Interaction en boucle pour lire deux chaînes de caractères et afficher la longueur 
	de leur plus longue sous-chaîne commune. 

	Le processus s'arrête lorsqu'une exception survient (fin d'entrée).
	"""
	while True:
		try:
			# Lecture des deux chaînes de caractères depuis l'entrée standard
			s, t = raw_input(), raw_input()

			# Assure que s est la chaîne la plus longue pour faciliter la recherche
			if len(s) < len(t):
				s, t = t, s

			ans = 0  # Initialisation de la longueur maximale trouvée de la sous-chaîne commune

			# Parcours de tous les indices de départ possibles dans t
			for sp in range(len(t)):
				# Si la longueur restante dans t est inférieure ou égale à la meilleure réponse actuelle, on arrête
				if len(t) - sp <= ans:
					break

				# Parcours des longueurs de sous-chaînes possibles à partir de la position sp
				for L in range(ans, len(t) - sp + 1):
					# Vérifie si la sous-chaîne t[sp:sp+L] est présente dans s
					if t[sp:sp+L] in s:
						ans = L  # Met à jour la plus longue sous-chaîne commune trouvée jusqu'à présent
					else:
						# Dès qu'une sous-chaîne n'est pas présente, plus besoin de vérifier les plus longues à partir de sp
						break

			print ans  # Affiche la longueur de la plus longue sous-chaîne commune trouvée
		except:
			# Sort de la boucle en cas d'erreur ou de fin d'entrée
			break