import sys  # On importe le module sys pour accéder à sys.stdin (entrée standard)

# On lit toutes les lignes disponibles dans l'entrée standard et on les sauvegarde dans la variable input_lines
# sys.stdin.readlines() retourne une liste de chaînes, où chaque chaîne correspond à une ligne, incluant le caractère de fin de ligne '\n'
input_lines = sys.stdin.readlines()

# On enlève le caractère de fin de ligne '\n' à la fin de chaque ligne provenant de l'entrée standard.
# Pour cela, on utilise une expression lambda qui supprime le dernier caractère de chaque chaîne (supposé être '\n')
# La fonction map applique cette lambda à chaque élément (chaque ligne) de input_lines.
lines = map(lambda x: x[:-1], input_lines)

# Chaque ligne étant maintenant une simple chaîne sans '\n', il faut la découper en morceaux (champs) séparés par des espaces
# On utilise donc une autre expression lambda avec la méthode split(" ") pour chaque élément (ligne) de lines
# Cela permet d'obtenir, pour chaque ligne, une liste de chaînes représentant les différentes valeurs numériques présentes sur la ligne
lines = map(lambda x: x.split(" "), lines)

# Cependant, map en Python 3 retourne un itérable (et non pas une liste comme en Python 2), il faut donc le convertir explicitement en liste
lines = list(lines)

# La première ligne (lines[0]) est censée contenir un entier n (le nombre de cas ou lignes de données à traiter ensuite)
# lines[0][0] permet d'accéder à cette valeur, mais elle est actuellement sous forme de chaîne, donc il faut la convertir en int
n = int(lines[0][0])

# On enlève maintenant la première ligne de la liste lines puisqu'elle a déjà été utilisée pour obtenir 'n'
# La méthode pop(0) retire et retourne le premier élément de la liste lines (ici, la ligne contenant 'n')
lines.pop(0)

# On parcourt ensuite chaque ligne restante dans lines (qui est une liste de listes de chaînes),
# Chaque ligne représente un test et contient à chaque fois 8 valeurs : x1, y1, x2, y2, x3, y3, x4, y4
for l in lines:
    # On utilise la fonction map pour convertir chaque chaîne de la ligne l en float (nombre à virgule flottante)
    # Puis, on assigne, via déballage (unpacking), chaque valeur convertie à la variable correspondante : x1, y1, etc.
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, l)
    
    # On calcule maintenant les composantes horizontale et verticale du premier vecteur (allant de (x1, y1) à (x2, y2))
    X1 = x2 - x1  # Différence des abscisses pour le premier vecteur
    Y1 = y2 - y1  # Différence des ordonnées pour le premier vecteur

    # On calcule de même les composantes horizontale et verticale du second vecteur (allant de (x3, y3) à (x4, y4))
    X2 = x4 - x3  # Différence des abscisses pour le second vecteur
    Y2 = y4 - y3  # Différence des ordonnées pour le second vecteur

    # Le but est maintenant de déterminer si ces deux vecteurs sont colinéaires (i.e. parallèles)
    # Deux vecteurs (X1, Y1) et (X2, Y2) sont colinéaires lorsque le déterminant suivant est nul :
    # |X1 Y1|
    # |X2 Y2|  <=> X1*Y2 - X2*Y1 == 0
    # Cependant, pour tenir compte de la précision limitée des nombres flottants, on vérifie si la valeur absolue
    # de cette expression est inférieure à un seuil très petit (1e-10)
    if abs(X1*Y2 - X2*Y1) < 1e-10:
        # Si les vecteurs sont colinéaires (presque nuls à 1e-10 près), on affiche "YES"
        print("YES")
    else:
        # Sinon, on affiche "NO"
        print("NO")