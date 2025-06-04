# Demande à l'utilisateur de saisir une valeur pour n (le nombre total d'éléments ou de jours, par exemple)
# input() lit une entrée utilisateur sous forme de chaîne de caractères
# int() convertit la chaîne en nombre entier
n = int(input())

# Demande à l'utilisateur de saisir une valeur pour k (un seuil ou un nombre de premières itérations utilisant un tarif spécial)
k = int(input())

# Demande à l'utilisateur de saisir une valeur pour x (valeur associée aux premières k itérations)
x = int(input())

# Demande à l'utilisateur de saisir une valeur pour y (valeur associée aux itérations après k)
y = int(input())

# Initialise une variable ans à zéro
# Cette variable va servir à accumuler le résultat final au cours de la boucle
ans = 0

# Utilisation d'une boucle for pour parcourir les entiers de 0 jusqu'à n-1 inclus
# range(n) génère une séquence de n valeurs, démarrant à 0 et s'arrêtant avant d'atteindre n
for i in range(n):
    # i commence à 0, donc i+1 commence à 1
    # Teste si on se trouve dans une position inférieure ou égale à k (les k premiers éléments)
    if (i + 1 <= k):
        # Si c'est le cas, ajoute la valeur x à ans
        ans += x
    # Teste si on a dépassé le seuil k
    if (i + 1 > k):
        # Si c'est le cas, ajoute la valeur y à ans
        ans += y

# Après avoir parcouru tous les éléments de la boucle, imprime le résultat final stocké dans ans
print(ans)