# Boucle infinie : cette boucle continuera à s'exécuter tant qu'aucune instruction break n'est rencontrée.
while True:
    # Lecture d'une ligne entrée par l'utilisateur au clavier (via la fonction input).
    # input() renvoie une chaîne de caractères, donc on utilise int() pour convertir cette chaîne en un entier.
    n = int(input())
    
    # On vérifie si la valeur saisie est égale à 0.
    # Si c'est le cas, on sort de la boucle avec la commande break.
    if n == 0:
        break  # Arrête la boucle la plus proche (while True dans ce cas).
    
    # Initialisation d'une variable compteur à 0.
    # Cette variable servira à compter combien d'étapes sont nécessaires pour que n devienne 1 selon les règles suivantes.
    cnt = 0
    
    # Cette boucle s'exécutera tant que n n'est pas égal à 1.
    while n != 1:
        # Ici, on vérifie si n est impair ou pair.
        # L'opérateur % calcule le reste de la division de n par 2.
        # Si le reste est 1, n est impair, sinon il est pair.
        # Si n est impair, on calcule 3*n + 1.
        # Si n est pair, on calcule n // 2 (division entière par 2).
        # L'expression conditionnelle (aussi appelée "ternaire") a la forme suivante :
        # x if condition else y signifie : si condition est vraie, utiliser x, sinon utiliser y.
        n = 3*n + 1 if n % 2 else n // 2

        # On incrémente le compteur de 1 à chaque itération pour compter le nombre de transformations appliquées à n.
        cnt += 1
    
    # Lorsque n devient égal à 1, la boucle interne se termine et on affiche la valeur du compteur cnt,
    # qui indique combien d'opérations ont été nécessaires.
    print(cnt)  # Affiche le nombre d'étapes pour chaque nombre saisi (sauf zéro).