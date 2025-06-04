# Demande à l'utilisateur de saisir une ligne de texte, par exemple : "1 2 3 4 5 6"
# La fonction input() lit l'entrée de l'utilisateur sous forme de chaîne de caractères.
# La fonction split() découpe cette chaîne en une liste de sous-chaînes, en séparant par défaut sur les espaces.
# La fonction map() applique la fonction int() à chaque élément de la liste, transformant chaque chaîne en entier.
# Les résultats du map() (qui est un itérateur) sont directement "dépaquetés" dans les variables a, b, c, d, e, f.
a, b, c, d, e, f = map(int, input().split())

# Calcule la somme pondérée :
#   - a est multiplié par 1       (car c'est une unité)
#   - b est multiplié par 5       (car chaque b représente une pièce de 5)
#   - c est multiplié par 10      (chaque c une pièce de 10)
#   - d est multiplié par 50      (chaque d une pièce de 50)
#   - e est multiplié par 100     (chaque e un billet de 100)
#   - f est multiplié par 500     (chaque f un billet de 500)
# On additionne toutes ces valeurs pour obtenir la somme totale d'argent.
total = a + 5 * b + 10 * c + 50 * d + 100 * e + 500 * f

# Vérifie si la somme d'argent totale est supérieure ou égale à 1000.
# Si c'est le cas (la condition est vraie), alors on doit afficher '1'.
# Sinon (la condition est fausse), on affiche '0'.
if total >= 1000:
    # Affiche la chaîne de caractères '1' dans la console (ce qui indique le succès de la condition).
    print('1')
else:
    # Affiche la chaîne de caractères '0' dans la console (ce qui indique l'échec de la condition).
    print('0')