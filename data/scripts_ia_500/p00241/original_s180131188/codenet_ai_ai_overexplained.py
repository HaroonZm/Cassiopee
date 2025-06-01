# Démarrer une boucle infinie qui va continuer à s'exécuter jusqu'à ce qu'on lui demande explicitement de s'arrêter
while 1:
    # Demander à l'utilisateur de saisir une entrée via le clavier, qui sera reçue sous forme de chaîne de caractères
    # Ensuite, convertir cette chaîne de caractères en un entier (int), car input() renvoie toujours une chaîne
    n = int(input())
    
    # Vérifier si la valeur entrée par l'utilisateur est égale à 0
    # Si c'est le cas, exécuter l'instruction 'break' qui interrompt immédiatement la boucle while
    if n == 0:
        break

    # Exécuter une boucle for un nombre de fois égal à la valeur entière n
    # Le caractère '_' est une variable "jetable" utilisée quand on ne se sert pas de la variable de boucle
    for _ in range(n):
        # Lire une nouvelle ligne de saisie utilisateur, qui contiendra plusieurs nombres séparés par des espaces
        # Diviser cette chaîne en morceaux individuels par la méthode split(), ce qui produit une liste de chaînes
        # Utiliser map() pour appliquer int() sur chacune de ces chaînes pour transformer chaque élément en entier
        # Envelopper le résultat de map() dans list() pour obtenir une liste contenant tous ces entiers
        data = list(map(int, input().split()))
        
        # Calculer la variable 'c' selon une expression qui effectue des opérations arithmétiques
        # Cette formule semble calculer la partie réelle d'un produit de quaternions, dont les composantes sont contenues dans data
        # Multiplication et soustraction sont effectuées entre les indices spécifiques des éléments de la liste 'data'
        c = data[0]*data[4] - data[1]*data[5] - data[2]*data[6] - data[3]*data[7]
        
        # Calculer la variable 'i' correspondant à la première composante imaginaire d'un quaternion calculé
        i = data[0]*data[5] + data[1]*data[4] + data[2]*data[7] - data[3]*data[6]
        
        # Calculer la variable 'j' correspondant à la deuxième composante imaginaire du quaternion
        j = data[0]*data[6] - data[1]*data[7] + data[2]*data[4] + data[3]*data[5]
        
        # Calculer la variable 'k' correspondant à la troisième composante imaginaire du quaternion
        k = data[0]*data[7] + data[1]*data[6] - data[2]*data[5] + data[3]*data[4]
        
        # Afficher le résultat des 4 valeurs calculées sous forme de chaîne de caractères séparées par des espaces
        # print() ajoute automatiquement un saut de ligne à la fin de l'affichage
        print(c, i, j, k)