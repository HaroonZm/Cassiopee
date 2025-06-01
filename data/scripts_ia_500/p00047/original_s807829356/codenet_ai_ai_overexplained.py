import sys

# Initialisation d'un dictionnaire nommé 'arr' contenant des clés de type chaîne de caractères ('A', 'B', 'C') 
# associées à des valeurs entières (1, 0, 0). Cela sert à stocker un état binaire (0 ou 1) pour chaque élément.
arr = {'A': 1, 'B': 0, 'C': 0}

# Utilisation d'une boucle 'for' pour itérer sur chaque ligne lue à partir de l'entrée standard (sys.stdin).
# L'entrée standard est généralement le flux d'entrée du programme (par exemple, ce que l'utilisateur tape ou un fichier redirigé).
for line in sys.stdin:
    # La méthode 'split' est appelée sur la chaîne de caractères 'line' pour diviser cette chaîne en une liste
    # d'éléments, séparés par la virgule ','.
    # Cela signifie que si la ligne est "A,B\n" après le split on obtient ['A', 'B\n'].
    s = line.split(',')
    
    # 'n' prend la première partie de la liste 's', correspond à l'élément avant la première virgule.
    n = s[0]
    
    # 'm' prend le premier caractère de la deuxième partie de la liste 's'.
    # On utilise ici l'index [0] parce que la deuxième partie peut contenir aussi le caractère de nouvelle ligne '\n'.
    # Prendre seulement le premier caractère permet donc de retirer ce '\n' et ne garder que la lettre.
    m = s[1][0]
    
    # Vérifie si l'état associé à la clé 'n' dans le dictionnaire 'arr' est 1, ou si celui associé à 'm' est 1.
    # Si la condition est vraie (donc au moins un des deux a la valeur 1),
    # alors on modifie l'état de ces deux entrées avec une opération spécifique.
    if arr[n] == 1 or arr[m] == 1:
        # On fait une mise à jour de la valeur à la clé 'n' dans 'arr'.
        # On ajoute 1 à la valeur actuelle (qui est soit 0 soit 1),
        # puis on applique l'opération modulo 2 pour alterner entre 0 et 1 (bascule binaire).
        arr[n] = (arr[n] + 1) % 2
        
        # Pareil pour la clé 'm' : on inverse également sa valeur entre 0 et 1.
        arr[m] = (arr[m] + 1) % 2

# Après la lecture et le traitement de toutes les lignes d'entrée,
# on parcourt tous les couples clé/valeur dans le dictionnaire 'arr' avec la méthode items().
for k, v in arr.items():
    # On vérifie si la valeur associée à la clé 'k' est égale à 1.
    if v == 1:
        # Si la condition est remplie, on imprime la clé (une des lettres 'A', 'B' ou 'C').
        # Cela produit la sortie finale du programme, indiquant quels éléments restent à l'état 1.
        print(k)