# Demande à l'utilisateur d'entrer deux valeurs entières séparées par un espace
# input() lit la ligne de texte entrée par l'utilisateur au clavier
# .split() découpe la chaîne de caractères entrée en une liste de sous-chaînes en utilisant l'espace comme séparateur
# map(int, ...) applique la fonction int (pour convertir en entier) à chaque élément de cette liste
# Les deux valeurs ainsi converties en entiers sont assignées respectivement aux variables A et B
A, B = map(int, input().split())

# Début de la structure conditionnelle 'if'
# On vérifie si la valeur de A est supérieure ou égale à 13
if A >= 13:
    # Si la condition précédente est vraie (A est au moins 13)
    # On affiche simplement la valeur de B en utilisant print()
    print(B)
# Si la première condition (A >= 13) n'est pas satisfaite, on vérifie la suivante avec 'elif'
# 'elif' signifie "sinon, si..."
# On vérifie si la valeur de A est inférieure ou égale à 12 ET supérieure ou égale à 6
# En Python, l'expression composée 12 >= A >= 6 est équivalente à (12 >= A) and (A >= 6)
elif 12 >= A >= 6:
    # Si cette condition est vraie (c'est-à-dire A est compris entre 6 et 12, bornes incluses)
    # On affiche la moitié de la valeur B, en utilisant la division entière (//)
    # La division entière retourne le quotient sans les décimales (partie entière seulement)
    print(B // 2)
# Si aucune des conditions précédentes n'est vraie (c'est-à-dire, si A est inférieur à 6)
# On utilise 'else' pour traiter tous les autres cas restants
else:
    # On affiche 0, ce qui signifie que pour les valeurs de A inférieures à 6, la sortie est toujours 0
    print(0)