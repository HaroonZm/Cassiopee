# Création d'un ensemble vide nommé S. Un ensemble est une structure de données qui stocke des éléments uniques, sans ordre particulier. 
S = set()

# Utilisation d'une boucle for pour répéter des instructions un certain nombre de fois.
# La fonction input() permet à l'utilisateur de saisir une valeur. Cette valeur est lue sous forme de chaîne de caractères.
# La fonction int() convertit cette chaîne de caractères en un entier.
# La fonction range() génère une suite d'entiers, ici allant de 0 à n-1, où n est le nombre saisi par l'utilisateur.
for i in range(int(input())):
    # Récupération d'une ligne de saisie utilisateur contenant deux entiers séparés par un espace.
    # input() lit une ligne sous forme de chaîne de caractères. 
    # split() divise cette chaîne en une liste de sous-chaînes à chaque espace rencontré.
    # map(int, ...) applique la fonction int() sur chaque élément de cette liste pour les convertir en entiers.
    # order et value sont assignés respectivement aux valeurs obtenues.
    order, value = map(int, input().split())

    # Vérification de la valeur de 'order' pour déterminer l'opération à effectuer.
    if order == 0:
        # Si order vaut 0, l'opération consiste à ajouter la valeur 'value' à l'ensemble S.
        # La méthode add() insère 'value' dans l'ensemble S UNIQUEMENT s'il n'existe pas déjà (propriété des ensembles).
        S.add(value)
        # Après l'ajout, on affiche le nombre d'éléments actuellement présents dans l'ensemble S.
        # La fonction len() retourne le nombre d'éléments dans S.
        print(len(S))
    else:
        # Si order n'est pas égal à 0 (par convention, ici ce sera 1), on doit vérifier si 'value' est déjà dans l'ensemble S.
        # L'opérateur 'in' teste l'appartenance d'un élément à une collection (ici un ensemble).
        # Si yes, 'value in S' sera True, sinon False.
        # Les instructions suivantes utilisent l'expression conditionnelle (ternaire) pour déterminer la valeur à afficher:
        #   - Si 'value' est dans S, alors on affiche 1, sinon on affiche 0.
        print(1 if value in S else 0)