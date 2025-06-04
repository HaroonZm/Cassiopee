# Crée une liste 'a' contenant quatre éléments, tous initialisés à 0. 
# Cette liste va servir de compteur pour chaque groupe sanguin.
a = [0, 0, 0, 0]

# Crée une liste 'aa' contenant les différentes valeurs possibles de groupes sanguins sous forme de chaînes de caractères.
# L'ordre ici est important car il va permettre de faire le lien avec la liste des compteurs 'a' ci-dessus.
aa = ["A", "B", "AB", "O"]

# Débute une boucle infinie, ce qui signifie que le code à l'intérieur de cette boucle va s'exécuter à plusieurs reprises
# jusqu'à ce qu'une instruction 'break' soit rencontrée pour interrompre la boucle.
while True:
  try:
    # Attend une entrée de l'utilisateur via la fonction input().
    # La fonction input() permet de saisir une chaîne de caractères depuis la console.
    s = input()
  except:
    # Si une exception se produit (par exemple si l'utilisateur fait Ctrl+D ou s'il n'y a plus d'entrée disponible),
    # le programme quitte la boucle grâce au mot-clé 'break'.
    break
  # La variable 's' contient une chaîne de caractères ayant un format du type 'nom,groupe_sanguin'.
  # La méthode split(",") va découper cette chaîne de caractères en une liste de deux éléments, 
  # en utilisant la virgule comme séparateur.
  b, c = s.split(",")
  # Ici, 'b' correspond au nom (qui n'est pas utilisé par la suite) et 'c' au groupe sanguin.
  # La méthode index() appliquée à la liste 'aa' retourne l'indice (la position)
  # correspondant à la valeur de 'c' dans cette liste (par exemple, pour "B", index retournera 1).
  # Ensuite, 'a[aa.index(c)] += 1' va incrémenter la valeur du compteur (dans la liste 'a') correspondant
  # au groupe sanguin indiqué par 'c'.
  a[aa.index(c)] += 1

# Démarre une boucle utilisant la fonction range(4), qui va générer les valeurs 0, 1, 2 et 3. 
# Cette boucle va donc s'exécuter exactement 4 fois, une fois pour chaque élément de la liste 'a'.
for i in range(4):
  # Affiche sur une ligne séparée la valeur de chaque compteur, c'est-à-dire le nombre d'occurences de chaque groupe sanguin.
  # L'indice 'i' permet de parcourir tour à tour chaque compteur de la liste 'a'.
  print(a[i])