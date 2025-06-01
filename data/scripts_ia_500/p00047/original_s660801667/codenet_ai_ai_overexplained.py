import sys  # Importe le module sys qui permet d'interagir avec le système, notamment pour lire des entrées standard

# Initialisation d'une liste appelée 'fe' contenant trois éléments : "A", "B" et "C"
# Cette liste représente une séquence ordonnée où chaque position a une signification
fe = ["A", "B", "C"]

# Boucle for qui lit ligne par ligne les entrées provenant de l'entrée standard (stdin)
# 'sys.stdin' est un objet qui permet de lire tout ce qui est tapé ou fourni en entrée, généralement depuis le terminal ou un fichier redirigé
# Pour chaque ligne input reçue, la variable 'line' contiendra cette ligne sous forme de chaîne de caractères (string)
for line in sys.stdin:
	# On enlève le dernier caractère de la ligne avec line[:-1].
	# En général, ce dernier caractère est un saut de ligne "\n" que l'on ne souhaite pas conserver.
	# Puis on divise cette chaîne résultante en une liste de sous-chaînes (strings) selon la virgule comme séparateur avec .split(",")
	# Par exemple, si line vaut "A,B\n", line[:-1] sera "A,B" et la méthode split(",") transformera cela en ["A", "B"]
	num = line[:-1].split(",")  # Liste contenant deux éléments, par exemple ['A', 'B']

	# L'instruction conditionnelle vérifie d'abord si le premier élément de la liste 'num' vaut "A"
	if num[0] == "A":
		# Si le second élément vaut "B", alors on exécute un échange des valeurs dans la liste 'fe' entre les indices 0 et 1
		if num[1] == "B":
			# On stocke temporairement la valeur à l'indice 0 dans la variable 'tako' pour éviter sa perte lors de l'échange
			tako = fe[0]
			# On remplace la valeur à l'indice 0 par celle qui se trouve à l'indice 1
			fe[0] = fe[1]
			# On place la valeur temporaire initiale stockée dans 'tako' à l'indice 1
			fe[1] = tako
		else:
			# Si le second élément n'est pas "B" (donc ici implicitement "C"), on échange les valeurs à l'indice 0 et 2
			tako = fe[0]
			fe[0] = fe[2]
			fe[2] = tako

	# Sinon, si le premier élément de 'num' est "B"
	elif num[0] == "B":
		# Si le second élément est "A", on échange les valeurs aux indices 1 et 0 de 'fe'
		if num[1] == "A":
			tako = fe[1]
			fe[1] = fe[0]
			fe[0] = tako
		else:
			# Sinon, (implicite second élément "C"), on échange les valeurs aux indices 1 et 2
			tako = fe[1]
			fe[1] = fe[2]
			fe[2] = tako

	# Sinon, si le premier élément est "C"
	elif num[0] == "C":
		# Si le second élément est "A", on échange les valeurs aux indices 0 et 2
		if num[1] == "A":
			tako = fe[0]
			fe[0] = fe[2]
			fe[2] = tako
		else:
			# Sinon (implicite second élément "B"), on échange les valeurs aux indices 1 et 2
			tako = fe[1]
			fe[1] = fe[2]
			fe[2] = tako

# Après la fin de toutes les lectures et échanges, on cherche l'indice où se trouve la valeur "A" dans la liste 'fe'
# La méthode .index("A") retourne la position (indice) de la première occurrence de "A" dans 'fe'
if fe.index("A") == 0:
	# Si "A" est à l'indice 0, on affiche la lettre "A" sur la sortie standard
	print "A"
elif fe.index("A") == 1:
	# Si "A" est à l'indice 1, on affiche "B"
	print "B"
else:
	# Sinon, cela signifie que "A" est à l'indice 2, on affiche "C"
	print "C"