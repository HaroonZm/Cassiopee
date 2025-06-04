# Définition d'une fonction nommée floor_sum qui prend quatre arguments entiers : n, m, a, et b
def floor_sum(n, m, a, b):
    # Initialisation d'une variable 'res' (pour 'result') à 0 : 
    # elle va accumuler la somme demandée au fur et à mesure du traitement
    res = 0
    # Début d'une boucle infinie : quittera la boucle en utilisant 'return' lorsque la condition sera remplie
    while True:
        # Première vérification : est-ce que 'a' (le coefficient multiplicateur de l'indice k) est supérieur ou égal à 'm' (le diviseur de la partie entière) ?
        if a >= m:
            # Calcul : combien de fois 'a' contient 'm' (quotient entier de la division de 'a' par 'm') 
            # Multiplication du résultat par 'n * (n-1) // 2' qui est la somme des entiers de 0 à n-1, cela donne le nombre total de fois où les multiples interviennent dans la somme des planchers
            res += a // m * n * (n - 1) // 2
            # Mise à jour de 'a' pour qu'il soit dans l'intervalle [0, m-1] en utilisant le reste (modulo) de la division de 'a' par 'm'
            a %= m
        # Seconde vérification indépendante : est-ce que 'b' (le terme constant dans l'argument du plancher) est supérieur ou égal à 'm' ?
        if b >= m:
            # Calcul : combien de fois 'b' contient 'm' (quotient entier)
            # Multiplication du résultat par 'n' (nombre total de termes) car chaque terme du plancher est affecté par cette translation
            res += b // m * n
            # Mise à jour de 'b' pour qu'il soit dans l'intervalle [0, m-1] en utilisant le reste de 'b' divisé par 'm'
            b %= m
        # Calcul de Y : (a * n + b) // m, c'est-à-dire combien d'entiers k de [0, n-1] on a tels que (a*k + b) // m vaut une certaine valeur
        Y = (a * n + b) // m
        # Calcul de X : Y * m - b, c'est une transformation intermédiaire servant à calculer où commence le dernier bloc pour le plancher
        X = Y * m - b
        # Condition d'arrêt : si 'Y' est nul (donc si le plancher est toujours zéro), la boucle doit se terminer
        if Y == 0:
            # On retourne la valeur de 'res' qui contient la somme finale demandée
            return res
        # Sinon : mise à jour de 'res' en ajoutant la contribution des nouveaux 'Y'
        # (n - (X + a - 1) // a) calcule combien de valeurs k contribuent à cette valeur de plancher
        # Ce terme est multiplié par Y, qui est la valeur du plancher sur ce bloc
        res += (n - (X + a - 1) // a) * Y
        # Mise à jour multiple pour réduire le problème à un problème plus petit (transformation récursive) :
        # On assigne à 'n' la valeur de Y, à 'm' la valeur de a, à 'a' la valeur de m et à 'b' la valeur de (-X) modulo a
        # Ce changement de variables réduit le domaine de la somme et permet de traiter le problème par étapes
        n, m, a, b = Y, a, m, -X % a

# Importation du module 'sys' qui permet de manipuler les flux d'entrée/sortie standards, notamment pour lire efficacement de grandes quantités de données
import sys
# Redéfinition de la fonction 'input' pour utiliser sys.stdin.buffer.readline :
# Cette version lit chaque ligne directement en binaire et est plus rapide que la fonction input() standard pour une grande quantité de données, notamment en compétition
input = sys.stdin.buffer.readline
# Lecture du premier entier de l'entrée standard qui représente le nombre de cas de tests à traiter
t = int(input())
# Boucle répétée 't' fois (une fois par cas de test)
for _ in range(t):
    # Lecture d'une ligne de l'entrée standard, division de la ligne en entiers,
    # et attribution des quatre valeurs lues à n, m, a, b respectivement
    n, m, a, b = map(int, input().split())
    # Appel de la fonction floor_sum avec les paramètres extraits du cas de test courant et affichage du résultat à la sortie standard
    print(floor_sum(n, m, a, b))