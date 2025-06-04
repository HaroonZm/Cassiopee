# Définition de la variable 'm' qu'on utilisera comme module pour toutes les opérations modulos.
# 'm' est une très grande valeur, probablement un nombre premier utilisé pour éviter les débordements d'entiers.
m = 10000000019

# Initialisation de la variable 'x' à 0.
# 'x' servira à stocker le résultat intermédiaire lors des traitements.
x = 0

# Définition d'une fonction qui applique un modulo sûr à une valeur donnée.
# Cette fonction prend un entier 'x' en argument.
def mod(x):
    # L'expression (x % m) effectue l'opération "modulo m" sur x,
    # de sorte que le résultat est compris entre 0 et m - 1 si x >= 0.
    # Cependant, si x est négatif, le résultat risque d'être négatif.
    # Donc, on ajoute 'm' pour s'assurer que la valeur est positive, puis on refait un modulo,
    # garantissant que le résultat final est toujours dans l'intervalle [0, m-1].
    return (x % m + m) % m

# Définition d'une fonction pour calculer la puissance rapide modulo m.
# 'x' est la base et 'a' est l'exposant.
def pow(x, a):
    # On initialise la variable 'ret' à 1, qui stockera le résultat de x^a.
    ret = 1
    # La boucle tourne tant que 'a' n'est pas égal à 0.
    while a:
        # L'opérateur '&' est un "ET" au niveau des bits. (a & 1) vérifie si le bit de poids faible est à 1,
        # c'est-à-dire si 'a' est impair.
        if (a & 1):
            # Si 'a' est impair, on multiplie le résultat actuel par 'x' et on prend le modulo.
            ret = mod(x * ret)
        # On élève toujours x au carré à chaque tour de boucle (x = x^2), puis on prend le modulo.
        x = mod(x * x)
        # On effectue un décalage à droite sur 'a' de 1 bit (a >>= 1), soit une division entière par 2.
        # Cela sert à parcourir tous les bits de l'exposant 'a', ce qui rend l'algorithme rapide (log_2(a) étapes).
        a >>= 1
    # On retourne le résultat de x^a modulo m.
    return ret

# La boucle suivante exécutera un nombre de fois donné par l'utilisateur.
# input() lit une ligne saisie par l'utilisateur, int() la convertit en entier.
for _ in range(int(input())):
    # On lit une ligne saisie par l'utilisateur et on l'utilise comme deux entiers séparés par un espace.
    o, y = map(int, input().split())
    # Si le premier entier 'o' est égal à 1, on ajoute 'y' à 'x' avec un modulo m.
    if o == 1:
        x = (x + y) % m
    # Si 'o' vaut 2, on soustrait 'y' de 'x', puis on fait un modulo m.
    elif o == 2:
        x = (x - y) % m
    # Si 'o' vaut 3, on multiplie 'x' par 'y' puis on applique le modulo via la fonction mod().
    elif o == 3:
        x = mod(x * y)
    # Si aucune des conditions précédentes n'est vraie (pour tous les autres cas de 'o'), on interprète ça comme une division.
    else:
        # On veut calculer (x / y) modulo m.
        # Dans l'arithmétique modulaire, diviser par y revient à multiplier par son inverse modulo m.
        # L'inverse de y modulo m est égal à y^(m-2) modulo m lorsque m est premier (grâce au petit théorème de Fermat).
        # Donc, on utilise la fonction pow pour calculer y^(m-2) modulo m, puis on multiplie 'x' par cet inverse et on applique mod().
        x = mod(x * pow(y, m - 2))
# À la fin du traitement de toutes les opérations, on affiche le résultat final.
# On vérifie si la valeur de 'x' est inférieure à 2^31 en utilisant le décalage de bits 1 << 31.
if x < (1 << 31):
    # Si c'est le cas, on affiche 'x' directement.
    print(x)
else:
    # Sinon, on soustrait 'm' de 'x' puis on affiche le résultat. Cela sert à normaliser les résultats,
    # notamment pour éviter d'avoir des valeurs négatives ou trop grandes selon les contextes applicatifs.
    print(x - m)