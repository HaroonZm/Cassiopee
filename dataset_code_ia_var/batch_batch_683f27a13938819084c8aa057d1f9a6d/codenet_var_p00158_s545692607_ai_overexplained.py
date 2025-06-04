# Commence une boucle infinie qui continue indéfiniment car la condition de boucle est toujours vraie (1 est évalué à True)
while 1:
    # Demande à l'utilisateur de saisir une entrée au clavier avec raw_input()
    # raw_input() retourne une chaîne de caractères, donc on utilise int() pour convertir cette chaîne en entier
    n = int(raw_input())
    
    # Vérifie si l'entier saisi par l'utilisateur est égal à 0
    # Si la condition est vraie (n == 0), alors le mot clé break est utilisé pour sortir immédiatement de la boucle while la plus proche
    if n == 0:
        break
    
    # Initialise une variable c à 0 ; elle servira de compteur pour suivre le nombre d'itérations dans la prochaine boucle
    c = 0

    # Commence une seconde boucle qui se poursuit tant que la valeur de n n'est pas égale à 1
    while n != 1:
        # À chaque itération, on veut appliquer une transformation à n selon la parité de la valeur
        # n % 2 calcule le reste de la division de n par 2
        # Si n est pair (n % 2 == 0), alors l'index est 0, donc n devient n / 2
        # Si n est impair (n % 2 == 1), alors l'index est 1, donc n devient n * 3 + 1
        # [n/2, n*3+1] crée une liste de deux éléments : premier élément pour n pair, deuxième pour n impair
        # L'indexation avec [n % 2] sélectionne l'une des deux transformations selon la parité de n
        # Note : n/2 effectue une division entière en Python 2 si n est un entier
        n = [n / 2, n * 3 + 1][n % 2]
        
        # Augmente la valeur de c de 1 pour compter cette transformation de n
        c += 1

    # Une fois que n atteint la valeur 1, la boucle interne se termine
    # On affiche (print) la valeur du compteur c, qui indique le nombre d'étapes nécessaires pour atteindre 1
    print c