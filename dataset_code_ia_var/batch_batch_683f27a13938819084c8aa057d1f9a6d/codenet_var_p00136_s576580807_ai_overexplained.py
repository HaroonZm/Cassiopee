# Création d'une liste 'C' qui contient 6 éléments, tous initialisés à 0.
# Cette liste servira à compter le nombre d'occurrences dans chaque catégorie.
C = [0] * 6

# Boucle for pour itérer un nombre de fois déterminé par la saisie de l'utilisateur.
# '[0] * int(raw_input())' génère une liste dont la longueur dépend du nombre lu à l'entrée,
# chaque élément de cette liste n'est pas utilisé ('_' comme variable fictive).
for _ in [0] * int(raw_input()):
    # Lecture d'une ligne de l'utilisateur, attendue sous la forme 'entier.entier' (par exemple 165.53).
    # La fonction 'raw_input()' lit la ligne en tant que chaîne de caractères.
    # '.split('.')' sépare la chaîne en deux parties autour du point, renvoie une liste de deux chaînes.
    # 'map(int, ...)' convertit chacune des deux sous-chaînes en entier.
    a, b = map(int, raw_input().split('.'))
    
    # Calcul de l'indice dans la liste 'C' à incrémenter selon la température 'a'.
    # '(a - 160) / 5' calcule combien de fois 5 rentre dans la différence entre 'a' et 160.
    # 'max([0, (a - 160) / 5])' retourne la valeur la plus grande entre 0 et le résultat ci-dessus,
    # pour s'assurer que l'indice ne soit jamais négatif.
    # À noter : en Python 2, la division entre deux entiers est une division entière.
    # Donc, (a - 160) / 5 tronque la partie décimale.
    index = max([0, (a - 160) / 5])
    
    # On augmente de 1 la valeur stockée dans 'C' à la position 'index'.
    C[index] += 1

# Boucle sur les indices de 0 à 5 (inclus) pour afficher le résultat.
for i in range(6):
    # 'i+1' donne le numéro de la catégorie (de 1 à 6).
    # 'C[i]' est le nombre d'occurrences pour cette catégorie,
    # donc '*' * C[i]' crée une chaîne contenant autant de '*' que la valeur de 'C[i]'.
    # Le format '%d:%s' permet d'afficher le numéro de catégorie suivi du graphique en étoiles.
    print '%d:%s' % (i + 1, '*' * C[i])