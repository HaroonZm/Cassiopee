# Boucle infinie qui continuera à s'exécuter jusqu'à ce qu'une condition de sortie soit rencontrée
while True:
    # Demande à l'utilisateur d'entrer une valeur, lit la saisie au clavier (sous forme de chaîne de caractères)
    # Ensuite, la convertit en entier avec la fonction int()
    n = int(input())
    
    # Vérifie si l'entier saisi par l'utilisateur est égal à zéro
    if n == 0:
        # Si l'utilisateur a entré zéro, on sort de la boucle en utilisant 'break'
        break
    
    # Initialise un compteur à zéro, ce compteur va compter le nombre d'itérations de la boucle suivante
    i = 0
    
    # Démarre une boucle qui continue tant que n n'est pas égal à 1
    while n != 1:
        # Incrémente le compteur i de 1 à chaque itération pour compter le nombre d'étapes
        i += 1
        
        # Vérifie si n est pair en utilisant l'opérateur modulo (%)
        # Si la division par 2 donne un reste de 0, alors n est pair
        if n % 2 == 0:
            # Si n est pair, divise n par 2 et assigne la valeur obtenue à n
            n = n / 2
        else:
            # Si n est impair, effectue l'opération 3*n + 1 et assigne le résultat à n
            n = n * 3 + 1
    
    # À la fin de la boucle interne, lorsque n vaut 1, affiche le compteur i, 
    # c'est-à-dire le nombre d'étapes effectuées pour atteindre 1 selon la conjecture de Syracuse
    print(i)