# Définition de la fonction principale qui contiendra tout le code du programme
def main():
    # Lecture d'une valeur entière à partir de l'entrée standard (ex: clavier)
    # Cette valeur représente le nombre total d'éléments (souvent désigné comme "N" dans les problèmes de programmation)
    N = int(input())
    
    # Lecture d'une ligne de texte depuis l'entrée standard contenant plusieurs nombres séparés par des espaces
    # La méthode split() sépare la chaîne sur chaque espace et retourne une liste de chaînes individuelles
    # La boucle for convertit chaque chaîne (i) en entier grâce à int(i)
    # Cela construit une nouvelle liste d'entiers stockée dans la variable h
    h = [int(i) for i in input().split()]
    
    # Création d'une liste c initialisée avec des zéros, de longueur N
    # Le caractère '*' répète [0] N fois pour former une liste [0,0,...,0] de taille N
    c = [0]*N
    
    # Initialisation de la première case de la liste de coûts c
    # Le coût pour atteindre le premier élément (indice 0) est toujours 0 car aucun saut n'est nécessaire
    c[0] = 0

    # Initialisation de la seconde case de la liste de coûts c
    # Le coût pour atteindre le deuxième élément (indice 1) est la valeur absolue de la différence de hauteur entre le premier et le deuxième élément
    # On utilise abs() pour obtenir la différence sans tenir compte du signe
    c[1] = abs(h[1] - h[0])
    
    # Boucle for qui part de i = 2 jusqu'à i = N-1 inclus (donc pour tous les indices de 2 à N-1)
    for i in range(2, N):
        # Calcul de deux coûts possibles pour atteindre la position i :
        # Première option : venir à i depuis i-1, donc coût absolu de la différence de hauteur + coût pour atteindre i-1
        # Deuxième option : venir à i depuis i-2, donc coût absolu de la différence de hauteur + coût pour atteindre i-2
        # On utilise la fonction min() pour conserver le plus petit des deux coûts possibles
        c[i] = min(
            abs(h[i] - h[i-1]) + c[i-1],     # Option 1 : saut d'une position
            abs(h[i] - h[i-2]) + c[i-2]      # Option 2 : saut de deux positions
        )
    
    # Affichage du coût minimal pour atteindre la dernière position (indice N-1) depuis le début
    # print() écrit la valeur sur la sortie standard
    print(c[N-1])

# Appel de la fonction principale pour que le programme commence son exécution
main()