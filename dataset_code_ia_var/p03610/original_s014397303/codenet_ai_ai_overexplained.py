# Demande à l'utilisateur de saisir une chaîne de caractères
# La fonction input() attend une saisie utilisateur au clavier, qui sera stockée dans la variable 's'
s = input()

# Vérifie si la longueur de la chaîne 's' est inférieure ou égale à 2
# len(s) calcule le nombre de caractères dans la variable 's'
if len(s) <= 2:
    # Si la condition précédente est vraie, c'est-à-dire si 's' contient 2 caractères ou moins
    # Affiche le premier caractère de la chaîne 's'
    # L'indexation commence à 0, donc s[0] représente le premier caractère de la chaîne
    print(s[0])

else:
    # Si la longueur de 's' est supérieure à 2, c'est-à-dire que la chaîne contient au moins 3 caractères
    # Calculer la moitié entière de la longueur de la chaîne 's'
    # L'opérateur // réalise une division entière (quotient sans la partie décimale/un reste n'est pas pris en compte)
    N = len(s) // 2

    # Initialiser la variable 'q' à zéro
    # Elle sera potentiellement utilisée pour ajuster la taille de la liste à créer selon que N est pair ou impair
    q = 0

    # Vérifie si N est impair
    # L'opérateur % calcule le reste de la division. Si N%2 == 1, alors N est un nombre impair
    if N % 2 == 1:
        # Si N est impair, on met q à 1 (cela permet d'ajouter un élément supplémentaire à la liste plus tard)
        q = 1

    # Crée une liste vide nommée 'Odd'
    # Cette liste servira à stocker les caractères de 's' d'indices pairs 
    # (c'est-à-dire les caractères aux positions 0, 2, 4, etc.)
    Odd = []

    # On va parcourir les entiers de 0 jusqu'à N + q (exclus, car le paramètre de fin de range n'est pas inclus)
    # range(N+q) génère une séquence de nombres de 0 à N+q-1
    for i in range(N + q):
        # s[2*i] accède au caractère de s à la position '2*i'
        # Cela permet de sélectionner uniquement les caractères à des positions d'indices pairs (0, 2, 4, ... )
        # On ajoute (append) ce caractère à la liste Odd
        Odd.append(s[2 * i])

    # Après la boucle, la liste Odd contient certains caractères de la chaîne 's'
    # "".join(Odd) permet de transformer la liste Odd en une chaîne de caractères
    # La méthode join() insère la chaîne "" (c'est-à-dire rien) entre chaque élément de la liste pour tout concaténer
    Odd = "".join(Odd)

    # Affiche la chaîne résultante qui est maintenant stockée dans Odd
    print(Odd)