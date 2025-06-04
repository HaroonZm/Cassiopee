# Demande à l'utilisateur de saisir une valeur entière, l'affecte à la variable N
# Cette valeur représente généralement le nombre d'éléments qui seront traités par la suite
N = int(input())  # Exemple : si l'utilisateur tape 3, alors N = 3

# Demande à l'utilisateur d'entrer deux entiers séparés par un espace
# Ces deux entiers sont placés dans une map, convertis en int, puis décompressés dans les variables A et B
A, B = map(int, input().split())  # Exemple : si l'utilisateur tape "2 5", alors A = 2 et B = 5

# Demande à l'utilisateur d'entrer un autre nombre entier
# Ce nombre est assigné à la variable C
C = int(input())  # Exemple : si l'utilisateur tape 10, alors C = 10

# Création d'une liste D comme suit :
# - Pour chaque valeur dans l'itérable généré par [0]*N (c'est-à-dire une liste contenant N zéros, utilisée comme compteur)
# - On lit un entier grâce à input()
# - On convertit l'entrée utilisateur en int
# - On construit une liste de ces entiers
# Ensuite :
# - On trie cette liste avec sorted() pour classer les éléments du plus petit au plus grand
# - On prend la liste triée et on la renverse avec [::-1], ce qui a pour effet d'obtenir les éléments du plus grand au plus petit
D = sorted(
    int(input()) for _ in [0]*N  # Boucle pour N répétitions afin de créer la liste des N entiers saisis
)[::-1]  # L'opérateur [::-1] inverse la séquence de la liste (donc du plus grand au plus petit)

# Maintenant, on veut calculer une valeur maximale comme suit :
# Pour chaque i allant de 1 à N-1 (car range(1, N) commence à 1 inclus et va jusqu'à N exclus)
# - On sélectionne les i premiers éléments de la liste D via D[:i]
# - On calcule la somme de ces i éléments avec sum(D[:i])
# - On ajoute cette somme à la valeur de C, formant ainsi le numérateur de notre division entière
# - Le dénominateur est A + i*B (A augmenté de i fois B)
# - On effectue ensuite une division entière (//), qui retourne le quotient de la division sans partie décimale
# On utilise un générateur pour calculer tous ces résultats pour chaque valeur de i (allant de 1 à N-1)
# On utilise enfin la fonction max pour trouver la valeur maximale obtenue parmi tous ces calculs
# Le résultat final est affiché à l'écran avec print
print(
    max(  # Cherche la valeur maximale parmi toutes les valeurs générées dans la boucle
        (
            C + sum(D[:i])  # Somme de C avec les i premiers éléments de D
        ) // (
            A + i*B  # Calcul de A augmenté de i fois B, pour le dénominateur de la division entière
        )
        for i in range(1, N)  # Boucle sur i allant de 1 à N-1 inclus
    )
)