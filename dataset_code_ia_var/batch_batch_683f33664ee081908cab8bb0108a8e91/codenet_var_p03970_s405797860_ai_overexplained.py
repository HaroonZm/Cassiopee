# Demande à l'utilisateur de saisir une chaîne de caractères au clavier.
# raw_input() lit une ligne de texte entrée par l'utilisateur dans la console.
# La chaîne lue est ensuite stockée dans la variable 's'.
s = raw_input()

# Initialise une variable qui contient la chaîne de référence à comparer.
# Cette variable 'true_s' contient la chaîne 'CODEFESTIVAL2016' que l'on considère correcte.
true_s = 'CODEFESTIVAL2016'

# Initialise un compteur d'erreurs à 0.
# Ce compteur 'error_number' va compter le nombre de positions où les caractères de 's'
# sont différents de ceux de 'true_s'.
error_number = 0

# Début d'une boucle for qui va itérer 16 fois puisque la longueur de 'true_s' est 16 caractères.
# La fonction range(16) crée un objet itérable allant de 0 inclus à 16 exclus.
# À chaque itération, la variable i prend une valeur de 0 à 15, qui représente un indice de la chaîne.
for i in range(16):
    # Vérifie si le caractère à la position i dans la chaîne saisie 's'
    # est différent du caractère à la même position dans la chaîne de référence 'true_s'.
    if s[i] != true_s[i]:
        # Si les caractères sont différents, cela signifie qu'il y a une erreur à cette position.
        # On incrémente alors le compteur d'erreurs de 1.
        error_number += 1

# Affiche le nombre total d'erreurs trouvées.
# La fonction print affiche la valeur de 'error_number' dans la console.
print error_number