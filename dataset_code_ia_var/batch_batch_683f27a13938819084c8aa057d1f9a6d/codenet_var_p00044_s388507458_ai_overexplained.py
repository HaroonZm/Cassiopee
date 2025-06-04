# Définition de la fonction « sieve » prenant un entier n en argument
def sieve(n):
    # Création d'une liste p de booléens, tous initialisés à True
    # Cette liste va de l'indice 0 jusqu'à l'indice n inclus ; elle va servir à indiquer si l'indice représente un nombre premier ou non
    p = [True] * (n + 1)
    # 0 et 1 ne sont pas des nombres premiers, on affecte donc False à ces indices
    p[0] = False
    p[1] = False
    # Parcours de tous les entiers i de 2 jusqu’à la racine carrée (approximative) de n ; +1 car range est non inclusif
    for i in range(2, int((n + 1) * 0.5) + 1):
        # Si p[i] est True, cela signifie que i est considéré comme premier pour l'instant
        if p[i] == True:
            # Parcours de tous les multiples de i à partir de i*i jusqu'à n inclus, en incrémentant de i à chaque étape (c-à-d, i*i, i*i+i, i*i+2i, ...)
            for j in range(i * i, n + 1, i):
                # On marque ces multiples comme non premiers, car ils sont divisibles par i
                p[j] = False
    # Création d'une liste vide pour stocker les nombres premiers identifiés
    prime = []
    # Parcours de tous les indices de 0 jusqu'à n inclus
    for i in range(n + 1):
        # Si p[i] est True, c'est que l'indice i est un nombre premier
        if p[i] == True:
            # On ajoute i à la liste des nombres premiers
            prime.append(i)
    # On retourne finalement la liste complète des nombres premiers trouvés jusqu’à n inclus
    return prime

# Définition de la fonction « solve » prenant un entier n en argument
def solve(n):
    # On initialise une variable i à 0 ; elle servira d’indice pour parcourir la liste prime
    i = 0
    # Boucle infinie : elle va tourner jusqu'à ce qu'on utilise « break »
    while True:
        # Si n est strictement supérieur à prime[i]
        if n > prime[i]:
            # On affecte à « a » la valeur de prime[i] ; « a » va donc mémoriser le plus grand nombre premier inférieur à n pour l’instant
            a = prime[i]
        # Sinon, si n est exactement égal à prime[i]
        elif n == prime[i]:
            # Cela signifie que n est lui-même un nombre premier ; dans ce cas, on affecte à « a » le précédent nombre premier dans la liste
            a = prime[i - 1]
        else:
            # Sinon (le cas où n < prime[i]), on affecte à « b » la valeur de prime[i] : c’est le plus petit nombre premier immédiatement supérieur ou égal à n
            b = prime[i]
            # On sort de la boucle, car on a trouvé les bornes désirées
            break
        # On incrémente l’indice i de 1, afin de tester le nombre premier suivant à l’itération suivante
        i += 1
    # Affichage sur la même ligne des deux valeurs a et b séparées par un espace
    print(a, b)

# Génération de la liste des nombres premiers jusqu’à 50021 inclus, en appelant la fonction sieve
prime = sieve(50021)

# Boucle infinie pour traiter les entrées utilisateur jusqu’à interruption
while True:
    try:
        # Lecture d’une entrée utilisateur, transformée en entier avec int ; input() attend une ligne au clavier
        n = int(input())
        # Appel de la fonction solve pour ce n, qui affiche le résultat
        solve(n)
    except EOFError:
        # Si l'entrée lève EOFError (fin de fichier, ex: Ctrl+D), on sort de la boucle en utilisant break
        break