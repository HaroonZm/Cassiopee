import sys  # Importe le module système permettant d'accéder à stdin

# Lit chaque ligne de l'entrée standard jusqu'à EOF,
# puis pour chaque ligne, fait ceci :
# - Utilise split(',') pour couper la chaîne en morceaux autour des virgules,
#   ce qui crée une liste de chaînes correspondant à chaque valeur numérique sur la ligne.
# - map(int, ...) convertit chaque chaîne obtenue en entier.
# - list(...) convertit l'itérable résultant en une vraie liste Python d'entiers.
# - [ ... for e in sys.stdin ] fait une compréhension de liste, donc on applique ce traitement à chaque ligne du flux d'entrée.
s = [list(map(int, e.split(','))) for e in sys.stdin]

# Boucle sur toutes les lignes de s à partir de la deuxième (index 1 inclus) jusqu'à la dernière.
# range(1, len(s)) génère une séquence de valeurs de 1 jusqu'à len(s)-1.
for i in range(1, len(s)):
    # k reçoit le nombre d'éléments (colonnes) dans la i-ème ligne de s.
    k = len(s[i])
    # b reçoit la valeur booléenne k > len(s[i-1])
    # Cela signifie : est-ce que la ligne actuelle (s[i]) est plus longue que la précédente (s[i-1]) ?
    # En Python, True équivaut à 1 et False à 0 si on l’utilise comme un entier.
    b = k > len(s[i-1])
    # Boucle sur chaque colonne de la ligne actuelle, donc pour chaque indice j allant de 0 à k-1 inclus.
    for j in range(k):
        # Calcule t comme étant j - b.
        # Si b vaut True (1), alors t = j-1 ; sinon t = j.
        t = j - b
        # On va mettre à jour la valeur s[i][j] :
        # On ajoute à la valeur courante s[i][j] le résultat du maximum parmi certains éléments de la ligne précédente
        # L’expression s[i-1][t*(j>0):t+2] fait ceci :
        # - Si j > 0, alors t*(j>0) est égal à t (puisque (j>0) est True donc 1)
        # - Sinon, t*(j>0) est 0, donc l’indice de début est 0
        # - L’indice de fin est toujours t+2
        # En résumé, on extraie les éléments entre certains indices de la ligne précédente.
        # max(...) donne la plus grande valeur de cette sous-liste.
        s[i][j] += max(s[i-1][t*(j > 0):t+2])

# À la fin de la boucle, la dernière ligne de s, c’est-à-dire s[-1], a été modifiée et contient les valeurs désirées.
# print(*s[-1]) affiche chaque élément de s[-1] mais les sépare avec des espaces (pas de crochets ni virgules)
# L’opérateur * « unpack » la liste pour passer chaque élément comme argument séparé à print().
print(*s[-1])