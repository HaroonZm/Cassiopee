# Définition de la fonction Collatz qui prend un argument entier n
def Collatz(n):
    # Vérification si le nombre n est pair
    # L'opérateur % (modulo) donne le reste de la division de n par 2
    # Si le reste est 0, cela signifie que n est divisible par 2 (c'est un nombre pair)
    if n % 2 == 0:
        # Si n est pair, diviser n par 2 en utilisant // (division entière)
        # Cela signifie que le résultat sera aussi un entier, aucune partie décimale
        return n // 2
    else:
        # Si n n'est pas pair (donc impair), multiplier n par 3 puis ajouter 1
        # Cela suit la célèbre conjecture de Collatz (aussi appelée problème 3n+1)
        return n * 3 + 1

# Boucle infinie while True, car True est toujours vrai
# Cela permet de répéter le bloc de code à l'intérieur indéfiniment
while True:
    # Demander à l'utilisateur d'entrer un nombre avec input()
    # input() retourne une chaîne de caractères, il faut donc la convertir en entier avec int()
    n = int(input())
    # Vérifier si l'utilisateur a entré 0
    # Cela est le cas de sortie de la boucle (condition d'arrêt)
    if n == 0:
        # Sortir de la boucle while en utilisant break
        break

    # Initialiser un compteur à zéro pour stocker le nombre d'étapes nécessaires
    count = 0
    # Démarrer une boucle qui continue tant que n n'est pas égal à 1
    while n != 1:
        # Appeler la fonction Collatz sur n et mettre à jour la valeur de n
        n = Collatz(n)
        # Incrémenter le compteur de 1 pour chaque itération
        count += 1
    # Afficher le nombre d'étapes effectuées lorsque n est devenu 1
    print(count)