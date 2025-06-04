# Demander à l'utilisateur de saisir des valeurs séparées par des espaces
entered_values = input().split()

# Trier les valeurs par ordre décroissant (du plus grand au plus petit)
entered_values.sort(reverse=True)

# Prendre les deux premiers éléments et les mettre bout à bout
combined = str(entered_values[0]) + str(entered_values[1])

# Convertir le résultat en nombre entier
number1 = int(combined)

# Prendre le troisième élément et le convertir en entier
number2 = int(entered_values[2])

# Additionner les deux nombres et afficher le résultat
print(number1 + number2)