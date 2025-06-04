# Demander à l'utilisateur d'entrer deux entiers séparés par un espace
# input() lit la ligne saisie au clavier sous forme de chaîne de caractères
# split() découpe la chaîne en une liste de sous-chaînes, en les séparant là où il y a des espaces
# map(int, ...) applique la fonction int() à chaque sous-chaîne, les convertissant en entiers
n, m = map(int, input().split())

# Boucle pour itérer m fois, c'est-à-dire autant de fois que le second nombre entré par l'utilisateur
# range(m) produit une séquence de m nombres de 0 à m-1 (non inclus), mais on ne l'utilise pas, d'où le "_"
for _ in range(m):
    # lire un entier fourni par l'utilisateur
    a = int(input())

    # Calcule le PGCD de n et a en utilisant l'algorithme d'Euclide avec la boucle while
    # La condition "while a" signifie que la boucle continue tant que a n'est pas nul (si a==0 la boucle s'arrête)
    # À chaque itération, on affecte à n la valeur de a, et à a la valeur du reste de la division de n par a (n%a)
    # Cela calcule le plus grand commun diviseur de n et a puis stocke le résultat dans n à la sortie de la boucle
    while a:
        n, a = a, n % a

# À la fin de toutes les entrées, afficher "Yes" si n vaut 1, sinon afficher "No"
# [ 'No', 'Yes' ] est une liste à deux éléments, indexée par la valeur booléenne n==1 (qui est True ou False donc 1 ou 0)
# Donc si n==1, l'index est 1 et affiche 'Yes', sinon c'est 0 et affiche 'No'
print(['No', 'Yes'][n == 1])