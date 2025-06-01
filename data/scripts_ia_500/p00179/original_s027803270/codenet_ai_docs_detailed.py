from collections import deque

def encode_string_to_base3(s):
	"""
	Encode une chaîne composée des caractères 'r', 'g' et 'b' en un entier en base 3.

	Paramètres :
	s (str) : Chaîne à encoder, composée uniquement de 'r', 'g' et 'b'.

	Retourne :
	int : Représentation entière en base 3 où 'r' = 0, 'g' = 1, 'b' = 2.
	"""
	t = 0
	for char in s:
		t *= 3
		if char == "r":
			t += 0
		elif char == "g":
			t += 1
		elif char == "b":
			t += 2
	return t

def decode_base3_to_list(num, length):
	"""
	Décode un nombre entier en base 3 en une liste d'entiers représentant les chiffres.

	Paramètres :
	num (int) : Nombre entier codé en base 3.
	length (int) : Nombre de chiffres à extraire.

	Retourne :
	list[int] : Liste des chiffres en base 3, dans l'ordre du chiffre le plus à gauche au plus à droite.
	"""
	digits = []
	for _ in range(length):
		digits.append(num % 3)
		num //= 3
	# Les chiffres sont extraits du chiffre le moins significatif au plus significatif, donc on inverse la liste
	digits.reverse()
	return digits

def encode_list_to_base3(lst):
	"""
	Encode une liste de chiffres (0, 1, 2) en un entier en base 3.

	Paramètres :
	lst (list[int]) : Liste des chiffres à encoder (doit contenir uniquement 0, 1 ou 2).

	Retourne :
	int : Entier correspondant au nombre codé en base 3.
	"""
	num = 0
	for digit in lst:
		num = num * 3 + digit
	return num

def solve_color_sequence(s, used):
	"""
	Calcule le nombre minimal d'étapes pour uniformiser une séquence de caractères 'r', 'g', 'b' en appliquant
	une transformation spécifique sur des paires adjacentes différentes.

	La transformation : pour deux caractères adjacents différents, les remplacer par le troisième caractère différent
	de 'r', 'g' et 'b'. Par exemple, si la paire est ('r', 'g'), elle devient ('b', 'b').

	Paramètres :
	s (str) : Chaîne initiale composée de 'r', 'g', et 'b'.
	used (list[int]) : Liste utilisée pour marquer les états déjà visités, taille au moins 3**len(s).

	Retourne :
	int : Nombre minimal d'étapes pour uniformiser la chaîne, ou -1 si impossible.
	"""
	n = len(s)
	start_state = encode_string_to_base3(s)
	max_state = 3 ** n

	# Réinitialise la liste des états visités
	for i in range(max_state):
		used[i] = 0

	queue = deque()
	queue.append(start_state)
	used[start_state] = 1

	steps = 0
	while queue:
		size = len(queue)
		for _ in range(size):
			current = queue.popleft()
			# Décodage de l'état actuel en liste de couleurs chiffrées
			state_list = decode_base3_to_list(current, n)

			# Vérification si tous les caractères sont identiques (uniforme)
			if all(c == state_list[0] for c in state_list):
				return steps

			# Génération des nouveaux états possibles en appliquant les transformations sur paires adjacentes différentes
			for i in range(n - 1):
				if state_list[i] != state_list[i + 1]:
					# Calcule le nouveau caractère qui est différent des deux actuels
					new_color = 3 - state_list[i] - state_list[i + 1]
					# Applique la transformation
					original_i = state_list[i]
					original_i1 = state_list[i + 1]
					state_list[i] = new_color
					state_list[i + 1] = new_color

					next_state = encode_list_to_base3(state_list)

					if used[next_state] == 0:
						queue.append(next_state)
						used[next_state] = 1

					# Restaure l'état original pour essayer d'autres transformations
					state_list[i] = original_i
					state_list[i + 1] = original_i1
		steps += 1

	# Si on ne trouve pas d'état uniforme
	return -1

def main():
	"""
	Programme principal qui lit des chaînes en entrée jusqu'à rencontrer "0",
	et pour chaque chaîne calcule la minimalité des étapes de transformation pour uniformiser.
	"""
	# Taille maximale possible pour un input donné la longueur, 3**10 est une limite suffisante ici
	used = [0] * (3 ** 10)

	while True:
		s = raw_input()
		if s == "0":
			# Condition d'arrêt du programme
			break

		result = solve_color_sequence(s, used)
		if result == -1:
			print("NA")
		else:
			print(result)

if __name__ == "__main__":
	main()