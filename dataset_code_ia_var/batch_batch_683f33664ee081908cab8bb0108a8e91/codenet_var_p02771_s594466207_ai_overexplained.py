import sys  # On importe le module sys qui permet d'interagir avec l'interpréteur Python, notamment pour la lecture et l'écriture standard

input = sys.stdin.readline  # On assigne la fonction readline de sys.stdin à la variable input pour permettre une lecture efficace d'une ligne depuis l'entrée standard

# On lit une ligne depuis l'entrée standard, puis on supprime les espaces de début et de fin et on découpe cette ligne en une liste de chaînes sur chaque espace rencontré.
# Ensuite, on applique la fonction int à chaque chaîne pour la transformer en entier grâce à la fonction map. On transforme le résultat de map en une liste d'entiers.
abc = list(map(int, input().split()))

# On transforme la liste abc en un ensemble (set) pour éliminer tous les doublons, car un ensemble ne peut contenir des éléments identiques.
# Ensuite, on calcule le nombre d'éléments distincts présents dans abc à l'aide de la fonction len, qui retourne la taille de l'ensemble.
res = len(set(abc))

# On effectue un test conditionnel :
# Si le nombre d'éléments distincts est égal à 1 (donc tous les éléments sont identiques)
# OU
# Si le nombre d'éléments distincts est égal à 3 (donc chaque élément est différent des deux autres)
if res == 1 or res == 3:
    print("No")  # Si au moins une des deux conditions est vraie, on affiche le texte "No" à l'écran
else:
    print("Yes")  # Sinon, on affiche "Yes" à l'écran (dans ce cas, il doit y avoir exactement deux valeurs identiques et une différente)