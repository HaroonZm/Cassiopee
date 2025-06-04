# Lire une valeur entrée par l'utilisateur, l'utilisateur doit saisir un nombre entier
# La fonction input() lit la saisie et int() convertit la saisie (qui est une chaîne) en entier
n = int(input())

# Lire une ligne saisie par l'utilisateur, qui contient des nombres séparés par des espaces
# La fonction input() lit toute la ligne comme une chaîne de caractères
# La méthode split() découpe cette chaîne en une liste de sous-chaînes selon les espaces
# On utilise une compréhension de liste pour appliquer int() à chaque élément et obtenir une liste d'entiers
response_list = [ int(v) for v in input().split() ]

# Initialiser la variable ans à 0, elle servira à stocker la réponse finale
ans = 0

# Définir une constante mod qui est utilisée pour calculer les résultats modulo 1000000007
# Cela permet d'éviter des dépassements d'entiers, c'est une pratique courante dans les problèmes de programmation compétitive
mod = 10**9 + 7

# Vérifier si n est pair (divisible par 2)
if n % 2 == 0:
    # Si n est pair, générer une liste right_list contenant n éléments
    # Pour chaque indice i allant de 0 à n-1, on calcule 2*(i//2+1)-1
    # i//2 effectue une division entière pour grouper les indices deux à deux
    # On ajoute 1, multiplie par 2, puis soustrait 1 pour obtenir la séquence des entiers impairs (1, 1, 3, 3, 5, 5, ...)
    right_list = [ 2*(i//2+1)-1 for i in range(n) ]
else:
    # Si n est impair, générer une liste right_list différente
    # Pour chaque indice i allant de 0 à n-1, on calcule 2*((i+1)//2)
    # (i+1)//2 regroupe les indices deux à deux différemment puis multiplie par 2 pour obtenir la séquence des entiers pairs (0, 2, 2, 4, 4, 6, 6, ...)
    right_list = [ 2*((i+1)//2) for i in range(n) ]

# Trier la liste de réponse fournie par l'utilisateur
# La fonction sorted() ne modifie PAS la liste originale, mais retourne une nouvelle liste triée
# Cette ligne vérifie si la liste triée par l'utilisateur correspond exactement à la liste right_list construite précédemment
if sorted(response_list) == right_list:

    # Si n est pair :
    if n % 2 == 0:
        # Calculer la puissance de 2 à la puissance (n // 2), c'est-à-dire faire 2^(n//2)
        # pow() prend trois arguments, le troisième est modulo mod pour éviter les très grands nombres
        # Nous faisons ans = 2^(n//2) % mod
        ans = pow(2, n//2, mod)
    else:
        # Si n est impair, on fait le même calcul mais avec (n-1)//2 au lieu de n//2
        # Cela calcule 2^((n-1)//2) % mod
        ans = pow(2, (n-1)//2, mod)

# Afficher la valeur finale de ans calculée ci-dessus
print(ans)