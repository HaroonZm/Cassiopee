# Lecture des deux entiers séparés par un espace depuis l'entrée utilisateur
first_integer_input, second_integer_input = [int(user_input) for user_input in input().split()]

# Calcul du produit des deux entiers
product_of_integers = first_integer_input * second_integer_input

# Affichage du résultat du produit
print(product_of_integers)