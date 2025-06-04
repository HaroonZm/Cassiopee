# Demander à l'utilisateur d'entrer un nombre entier et l'affecter à la variable n.
# Cette variable 'n' représente le nombre de boucles à effectuer dans la suite du programme.
n = int(input())

# Demander à l'utilisateur d'entrer deux entiers séparés par un espace.
# split() divise la chaîne en liste, input() lit l'entrée au format string.
# map(int, ...) applique l'opération int() à chaque élément de la liste résultante du split().
# On utilise une affectation multiple pour stocker la première valeur dans 'd' et la deuxième dans 'x'.
d, x = map(int, input().split())

# Initialiser une variable nommée 'count' à la valeur 0.
# Cette variable va servir à stocker un total cumulatif au fil des itérations de la boucle.
count = 0

# Commencer une boucle for qui va s'exécuter 'n' fois.
# range(n) génère une séquence d'entiers allant de 0 à n-1.
# À chaque itération, la variable 'i' prend la valeur suivante dans la séquence.
for i in range(n):
    # Demander à l'utilisateur d'entrer un entier et l'affecter à la variable 'a'.
    a = int(input())
    
    # Vérifier si la division entière du nombre 'd' par la valeur 'a' n'a pas de reste.
    # Cela se fait à l'aide de l'opérateur modulo %, qui donne le reste de la division.
    if d % a == 0:
        # Si la division de d par a tombe juste (le reste est zéro), alors on peut faire d//a étapes.
        # L'opérateur // effectue une division entière (quotient sans le reste).
        count += d // a  # On ajoute ce nombre à la variable 'count'.
    else:
        # Si la division de d par a ne tombe pas juste (reste non nul), on ajoute un à la division entière.
        # Cela permet de s'assurer qu'on couvre toute la distance 'd', même s'il reste un petit morceau.
        count += d // a + 1  # On ajoute à 'count' le quotient + 1 pour le dernier morceau incomplet.

# Après la boucle, ajouter la valeur de la variable 'x' à 'count'.
# Cela permet d'ajouter un supplément, provenant généralement d'une valeur de départ ou d'une ressource additionnelle.
count += x

# Afficher la valeur finale de la variable 'count' à l'écran.
# La fonction print() convertit la variable en une chaîne de caractères, puis l'affiche à l'utilisateur.
print(count)