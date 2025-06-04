# Affiche à l'écran le résultat du calcul 2 élevé à la puissance (2 plus la conversion en entier de l'entrée utilisateur), puis on soustrait 2 à ce résultat

# Demande à l'utilisateur de saisir une valeur via le clavier, sous forme de chaîne de caractères (string)
# La fonction input() affiche une invite (ici vide) et récupère ce que l'utilisateur tape jusqu'à la validation par 'Entrée'

user_input = input()  # L'utilisateur saisit une valeur, qui est stockée sous forme de chaîne dans la variable 'user_input'

# Convertit la chaîne de caractères fournie par l'utilisateur en entier grâce à la fonction int()
user_input_as_int = int(user_input)  # Par exemple, si l'utilisateur tape '3', on obtient l'entier 3

# Ajoute 2 à la valeur entière fournie par l'utilisateur
exponent = 2 + user_input_as_int  # Par exemple, si user_input_as_int vaut 3, alors exponent vaudra 5

# Calcule 2 élevé à la puissance 'exponent'
power_result = 2 ** exponent  # '**' signifie 'puissance de' en Python. Par exemple, 2 ** 5 = 32

# Soustrait 2 au résultat du calcul précédent
final_result = power_result - 2  # Par exemple, 32 - 2 = 30

# Affiche le résultat final sur la console
print(final_result)  # La fonction print() affiche ce qui est passé entre les parenthèses