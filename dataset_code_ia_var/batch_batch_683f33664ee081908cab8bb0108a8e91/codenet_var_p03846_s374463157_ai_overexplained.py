# Lecture d'un entier depuis l'entrée standard (console)
# La fonction input() lit la saisie utilisateur sous forme de chaîne de caractères
# La fonction int() convertit la chaîne de caractères en un entier
n = int(input())

# Lecture d'une liste d'entiers depuis l'entrée standard, séparés par des espaces
# input() lit la ligne en chaîne, split() découpe la chaîne en une liste de sous-chaînes
# map(int, ...) applique la fonction int à chaque sous-chaîne pour les convertir en entiers
# sorted(...) trie la liste d'entiers dans l'ordre croissant et retourne une nouvelle liste triée
A = sorted(map(int, input().split()))

# Vérification si n (la taille de la liste) est impair (n % 2 == 1)
if n % 2 == 1:
    # Si n est impair, initialiser la liste ex avec un seul élément 0
    ex = [0]
    # Boucle for : itère de i = 0 jusqu'à i < n//2 (division entière par 2)
    for i in range(n // 2):
        # Calcul d'une valeur paire a : a = 2 * (i+1)
        a = 2 * (i + 1)
        # Ajoute deux fois la valeur a à la liste ex (en concaténant [a, a])
        ex += [a, a]
# Si n est pair (le else s'exécute si n % 2 != 1, donc n pair)
else:
    # Si n est pair, on initialise la liste ex comme liste vide
    ex = []
    # a commence à 1
    a = 1
    # Boucle for : itère de i = 0 jusqu'à i < n//2
    for i in range(n // 2):
        # Ajoute deux fois la valeur a à la liste ex
        ex += [a, a]
        # Incrémente a de 2 à chaque tour de boucle (pour obtenir la séquence impaire suivante)
        a += 2

# Initialisation de la variable de réponse ans à 0 (ce sera la valeur imprimée à la fin)
ans = 0

# Test si la liste triée d'entrée A est exactement égale à la liste ex construite précédemment
if A == ex:
    # Si c'est le cas, on calcule 2 puissance (n//2)
    # L'opérateur ** signifie "puissance", donc 2 ** (n//2) calcule 2 à la puissance (n//2)
    # On prend ensuite le résultat modulo 10^9 + 7 (nombre très grand fréquemment utilisé pour éviter les débordements)
    ans = 2 ** (n // 2) % (10 ** 9 + 7)

# Affichage final de la réponse : imprime la valeur de ans à la sortie standard
print(ans)