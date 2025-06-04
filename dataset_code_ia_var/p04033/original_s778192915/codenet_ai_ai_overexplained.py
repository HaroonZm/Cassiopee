# Demande à l'utilisateur de saisir deux nombres séparés par un espace
# La fonction input() lit une ligne de texte depuis l'entrée standard (clavier)
# La méthode split() coupe la chaîne en une liste à partir des espaces
# La fonction map(int, ...) applique la conversion en entier (int) à chaque élément de la liste générée par split()
# Enfin, l'affectation multiple 'a, b = ...' place le premier nombre dans 'a' et le second dans 'b'
a, b = map(int, input().split())

# On commence une structure conditionnelle pour tester les valeurs de 'a' et 'b'
if a <= 0 and b >= 0:
    # Cette condition vérifie si 'a' est inférieur ou égal à zéro ET 'b' est supérieur ou égal à zéro
    # Le symbole '<=' signifie 'inférieur ou égal à'
    # Le symbole '>=' signifie 'supérieur ou égal à'
    # Le mot 'and' signifie que les deux conditions doivent être vraies en même temps
    print("Zero")  # Si c'est vrai, on affiche la chaîne de caractères "Zero" à l'écran

elif b < 0:
    # Sinon, si la première condition n'est pas vérifiée,
    # on teste si 'b' est strictement inférieur à zéro (c'est-à-dire négatif)
    # Le symbole '<' signifie 'strictement inférieur à'
    if (b - a) % 2 == 0:
        # On calcule la différence entre 'b' et 'a' (c'est 'b - a')
        # On applique l'opérateur modulo '%' avec 2 pour obtenir le reste de la division entière par 2
        # Si le résultat est égal à zéro ('== 0'), alors la différence est un nombre pair
        print("Negative")  # Dans ce cas, on affiche "Negative"
    else:
        # Si le reste n'est pas zéro, alors la différence est un nombre impair
        print("Positive")  # On affiche alors "Positive"

else:
    # Si aucune des conditions précédentes n'est vérifiée, c'est le cas par défaut
    print("Positive")  # On affiche "Positive"