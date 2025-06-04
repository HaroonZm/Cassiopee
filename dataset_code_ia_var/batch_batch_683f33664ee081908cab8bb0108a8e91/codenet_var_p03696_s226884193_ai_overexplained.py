# Demande à l'utilisateur d'entrer une valeur entière qui sera stockée dans la variable 'n'
# Même si elle n'est pas utilisée plus tard dans ce code, nous la lisons ici par conformité à l'original
n = int(input())

# Demande à l'utilisateur d'entrer une chaîne de caractères et la stocke dans la variable 's'
s = input()

# Initialise deux variables à zéro :
# 'l_num' va compter le nombre de parenthèses ouvrantes '(' en trop qui n'ont pas de correspondance
# 'r_num' va compter le nombre de parenthèses fermantes ')' en trop qui n'ont pas de correspondance
l_num, r_num = 0, 0

# Démarre une boucle 'for' pour itérer sur chaque caractère de la chaîne 's'
for i in s:
    # Si le caractère courant 'i' est une parenthèse ouvrante '('
    if i == '(':
        # On incrémente le compteur 'l_num' car on a une parenthèse ouvrante à gérer
        l_num += 1
    # Si le caractère courant 'i' n'est pas '(' donc probablement ')'
    # et s'il n'y a pas de parenthèse ouvrante à fermer ('l_num' est inférieur ou égal à 0)
    elif l_num <= 0:
        # On incrémente le compteur 'r_num' pour dire qu'une parenthèse fermante en trop a été trouvée
        r_num += 1
    else:
        # Si 'i' est une parenthèse fermante ')' et qu'il existe au moins une parenthèse ouvrante à fermer (l_num > 0)
        # Alors on décrémente 'l_num' pour indiquer qu'une parenthèse ouvrante a trouvé sa correspondance
        l_num -= 1

# À ce stade :
# 'r_num' contient le nombre de parenthèses ouvrantes '(' à ajouter au début de la chaîne pour équilibrer le surplus de ')'
# 'l_num' contient le nombre de parenthèses fermantes ')' à ajouter à la fin de la chaîne pour équilibrer le surplus de '('

# Construction de la chaîne équilibrée et affichage du résultat :
# - '(' * r_num : crée une chaîne composée de 'r_num' parenthèses ouvrantes
# - s : c'est la chaîne d'origine
# - ')' * l_num : crée une chaîne composée de 'l_num' parenthèses fermantes
# - L'opérateur '+' sert à concaténer les chaînes entre elles dans l'ordre indiqué
print('(' * r_num + s + ')' * l_num)