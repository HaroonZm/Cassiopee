# Demander à l'utilisateur de fournir une entrée, qui sera traitée comme une chaîne de caractères par défaut.
# La fonction int() convertit cette chaîne de caractères en un entier, que nous stockons dans la variable n.
n = int(input())

# Si n est inférieur ou égal à 2, ou égal à 4, nous entrons dans ce bloc conditionnel.
if n <= 2 or n == 4:
    # Afficher "No" pour indiquer que la condition du problème n'est pas satisfaite pour ces valeurs
    print("No")

# Si n est exactement égal à 3, nous voulons traiter ce cas particulier séparément.
elif n == 3:
    # Afficher "Yes" pour indiquer que la condition est satisfaite pour n == 3
    print("Yes")
    # Boucle for avec la variable i prenant les valeurs de 0 à 4 (c'est-à-dire 5 itérations)
    for i in range(5):
        # Affiche deux nombres: i+1 et i+2
        # Ceci génère les paires (1,2), (2,3), (3,4), (4,5), (5,6)
        print(i + 1, i + 2)

# Si n est pair (multiple de 2), nous entrons dans ce cas
elif n % 2 == 0:
    # nn reçoit le nombre de bits nécessaires pour représenter n en binaire
    # Par exemple, si n=8, n.bit_length() retourne 4, car 8 en binaire est 1000 (4 chiffres)
    nn = n.bit_length()
    # Si n est une puissance de 2 (exactement 2^(nn-1)), on traite un cas particulier
    if n == 2 ** (nn - 1):
        # Afficher "No" car on ne satisfait pas la condition pour ce cas
        print("No")
    else:
        # Sinon (n > 4, n pair, mais pas une puissance de 2), on continue
        print("Yes")
        # Imprimer successivement des paires de nombres qui peuvent représenter des arêtes ou relations
        # Exemple : pour n=6, on aurait (1,2), (2,3), etc.
        print(1, 2)
        print(2, 3)
        print(3, n + 1)
        print(n + 1, n + 2)
        print(n + 2, n + 3)
        # Boucle pour i allant de 4 à n-1 inclus (n étant exclu par range), donc (4, ..., n-1)
        for i in range(4, n):
            # Imprime une paire où le premier élément est n+1 et le second est i
            print(n + 1, i)
            # Vérifie la parité de i : si i est pair (reste de la division de i par 2 est 0)
            if i % 2 == 0:
                # Si i est pair, imprime la paire (i, i + n + 1)
                print(i, i + n + 1)
            else:
                # Si i est impair, imprime la paire (i, i + n - 1)
                print(i, i + n - 1)
        # Après la boucle, nous définissons deux variables, n1 et n2
        # n1 est la plus grande puissance de 2 qui est inférieure ou égale à n
        n1 = 2 ** (nn - 1)
        # n2 est la différence entre (n + 1) et cette même puissance de 2
        n2 = (n + 1) - 2 ** (nn - 1)
        # On imprime les paires finales
        print(n1, n)
        print(n2, 2 * n)

# Enfin, pour tous les autres cas (n est impair, n > 3), on utilise le else
else:
    # Affiche "Yes" pour indiquer que la solution est possible
    print("Yes")
    # Imprimer les mêmes premiers liens fixes que dans le cas pair
    print(1, 2)
    print(2, 3)
    print(3, n + 1)
    print(n + 1, n + 2)
    print(n + 2, n + 3)
    # Boucle de i de 4 à n inclus, donc (4, ..., n)
    for i in range(4, n + 1):
        # Imprime la paire (1, i)
        print(1, i)
        # Vérifie si i est pair
        if i % 2 == 0:
            # Si pair, imprime (i, i + n + 1)
            print(i, i + n + 1)
        else:
            # Si impair, imprime (i, i + n - 1)
            print(i, i + n - 1)