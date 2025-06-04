# Demande à l'utilisateur de saisir une valeur au clavier (sous forme de texte)
# La fonction input() attend que l'utilisateur entre quelque chose puis appuie sur Entrée
# Le résultat de input() est toujours une chaîne de caractères (string)
n = int(input())  # Convertit la chaîne de caractères obtenue en un entier (int) en utilisant la fonction int()
                  # La variable n stocke donc une valeur numérique entière

# Divise la valeur de n par 3
# L'opérateur de division (/) retourne toujours un nombre à virgule flottante (float) même si n est divisible par 3
result = n / 3  # Par exemple, si n vaut 9, alors result sera égal à 3.0 (un float, pas un int)

# Calcule le cube de result, c'est-à-dire l'élève result à la puissance 3
# L'opérateur ** est l'opérateur de puissance en Python
final_result = result ** 3  # Si result vaut 3, final_result vaudra 27 (car 3 × 3 × 3 = 27)

# Affiche le résultat final à l'écran pour que l'utilisateur puisse le voir
# La fonction print() affiche ce qui est passé entre parenthèses
print(final_result)  # Imprime la valeur de final_result sur la console