# Lecture des deux entiers n et k depuis l'entrée standard (par défaut, open(0) se réfère à sys.stdin)
# open(0).read() lit tout l'entrée comme une chaîne de caractères
# .split() découpe la chaîne en une liste de sous-chaînes au niveau des espaces
# map(int, ...) convertit chaque sous-chaîne en entier
# L'affectation multiple permet de placer les deux entiers lus dans les variables n et k respectivement
n, k = map(int, open(0).read().split())

# Initialisation de la variable ans à 0.
# Cette variable stockera la réponse finale qui sera construite au fil de la boucle
ans = 0

# Nous allons maintenant itérer la variable b depuis k+1 jusqu'à n inclus.
# range(a, b) génère une séquence commençant à a jusqu'à b-1, donc range(k+1, n+1) inclut n
for b in range(k + 1, n + 1):
    
    # Calcul de la variable c : (n // b) donne combien de fois b tient exactement dans n (division entière)
    # On multiplie ce nombre par (b - k) : cela représente un certain décompte dépendant de b et k
    c = (n // b) * (b - k)

    # Si k n'est pas nul (c'est-à-dire si k a une valeur différente de 0), il faut calculer d différemment
    if k:
        # n % b donne le reste de la division de n par b -- c'est le reste non couvert par les blocs complets de taille b
        # (n % b) - k + 1 peut être négatif, donc on prend le maximum avec 0 : max(0, ...)
        # Cela garantit que d ne descend jamais en dessous de zéro
        d = max(0, n % b - k + 1)
    else:
        # Si k est égal à 0, d prend simplement la valeur n % b (le reste de la division entière)
        d = n % b

    # On ajoute le résultat c à la réponse accumulée ans
    ans += c

    # On ajoute également le résultat d
    ans += d

# Enfin, on affiche la réponse ans avec la fonction print (ceci écrit le résultat sur la sortie standard)
print(ans)