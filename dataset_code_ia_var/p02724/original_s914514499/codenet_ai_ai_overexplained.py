# Demande à l'utilisateur de saisir un nombre entier, lira l'entrée au clavier sous forme de chaîne de caractères
# Ensuite, convertit cette chaîne de caractères en un entier grâce à la fonction int()
N = int(input())

# Calcule combien de fois 500 tient entièrement dans N
# L'opérateur // permet de faire une division entière (on ne garde que la partie entière, sans virgule)
# Par exemple, si N vaut 1350, N//500 donne 2 parce que 500 tient 2 fois dans 1350 (le reste n'est pas pris en compte)
A = N // 500

# Calcule maintenant combien reste-t-il dans N après avoir pris les parts de 500 déjà comptées
# Pour cela, on enlève à N la quantité prise par les 500, soit A*500
# On a alors "N - A*500"
# Ensuite, on cherche combien de fois 5 tient dans ce reste (division entière à nouveau)
B = (N - A * 500) // 5

# Calcule la somme finale de la manière suivante :
# "A" représente le nombre de parts de 500, chaque part "rapporte" 1000
# "B" représente le nombre de parts de 5 heures restantes, chaque part "rapporte" 5
# On multiplie ces quantités et fait l'addition
resultat = A * 1000 + B * 5

# Affiche le résultat final dans la console grâce à la fonction print()
# Cela écrit la valeur de la variable 'resultat' à l'écran
print(resultat)