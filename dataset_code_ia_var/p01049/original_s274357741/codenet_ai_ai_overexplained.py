# Demande à l'utilisateur d'entrer un nombre entier pour la variable n
n = int(input())

# Demande à l'utilisateur d'entrer deux entiers (séparés par un espace) assignés respectivement à 'a' et 'd'
a, d = map(int, input().split())

# Initialise un dictionnaire vide appelé 'mem'
# Ce dictionnaire servira à mémoriser ou remplacer certaines valeurs associées à une clé spécifique
mem = {}

# Définit une fonction appelée 'get_mem' qui prend un argument 'num'
def get_mem(num):
    # Vérifie si 'num' est présent dans le dictionnaire 'mem'
    if num in mem:
        # Si 'num' est une clé dans 'mem', on retourne la valeur associée à cette clé
        return mem[num]
    else:
        # Si 'num' n'est pas une clé dans 'mem', on retourne simplement 'num' lui-même
        return num

# Demande à l'utilisateur d'entrer un entier 'm'
# 'm' sera utilisé pour déterminer combien de fois la boucle 'for' s'exécutera
m = int(input())

# Démarre une boucle qui s'exécutera exactement 'm' fois
for _ in range(m):
    # À chaque itération, demande à l'utilisateur trois entiers (séparés par des espaces), les affectant à x, y, z respectivement
    x, y, z = map(int, input().split())
    # Vérifie si la variable x est égale à 0
    if x == 0:
        # Si oui, récupère la valeur en mémoire de 'y' (via la fonction get_mem) et l'assigne à 'ny'
        ny = get_mem(y)
        # Récupère la valeur en mémoire de 'z' (via la fonction get_mem) et l'assigne à 'nz'
        nz = get_mem(z)
        # Associe dans 'mem' la clé 'y' avec la valeur 'nz'
        mem[y] = nz
        # Associe dans 'mem' la clé 'z' avec la valeur 'ny'
        mem[z] = ny
    # Vérifie si la variable x est égale à 1
    if x == 1:
        # Si oui, récupère la valeur en mémoire de 'z' (via la fonction get_mem) et la stocke dans 'nz'
        nz = get_mem(z)
        # Associe dans 'mem' la clé 'y' avec la valeur 'nz'
        mem[y] = nz

# Demande à l'utilisateur d'entrer un entier, applique la fonction get_mem sur cette entrée, puis stocke le résultat dans 'k'
k = get_mem(int(input()))

# Calcule la valeur recherchée, c'est-à-dire : 'a' + 'd' * (k - 1)
# Ce calcul représente probablement le terme k-ième d'une progression arithmétique de premier terme 'a' et de raison 'd'
resultat = a + d * (k - 1)

# Affiche le résultat final sur la sortie standard
print(resultat)