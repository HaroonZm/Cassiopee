# Demande à l'utilisateur de saisir une chaîne de caractères via le clavier
s = input()  # Par défaut, input() lit l'entrée de l'utilisateur et la stocke sous forme de chaîne de caractères

# Calcule la longueur de la chaîne saisie et la stocke dans la variable n
n = len(s)  # La fonction len() retourne le nombre de caractères présents dans la chaîne

# Initialise une variable minnum à une valeur très grande qui sera utilisée pour stocker le minimum rencontré
minnum = 100000  # On part d'une valeur élevée pour s'assurer que toute différence trouvée sera plus petite

# Commence une boucle pour examiner toutes les sous-chaînes de longueur 3 qui peuvent être extraites de s
for i in range(n - 2):  # On s'arrête à n-2 car il faut assez de caractères restants pour prendre un groupe de 3

    # Extrait une sous-chaîne de longueur 3 caractères en commençant à la position i
    check = s[i:i+3]  # L'opération s[x:y] retourne une sous-chaîne de s de l'indice x à l'indice y-1 inclus

    # Convertit la sous-chaîne extraite en entier avec int(), la soustrait à 753
    # Calcule la valeur absolue de cette différence (pour ignorer le signe négatif)
    check = abs(753 - int(check))  # abs(x) donne la valeur positive de x, quelle que soit la valeur de x

    # Met à jour minnum si la valeur absolue courante est plus petite que celle stockée précédemment
    # min() prend deux valeurs et retourne la plus petite
    minnum = min(minnum, check)

# Affiche la plus petite différence obtenue à la fin de la boucle
print(minnum)  # print() affiche la valeur entre parenthèses à l'écran