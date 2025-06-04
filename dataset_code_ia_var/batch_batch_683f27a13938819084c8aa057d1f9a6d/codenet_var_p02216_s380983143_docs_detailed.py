def first():
    """
    Affiche 'First' et termine immédiatement l'exécution du programme.
    Utilisé pour indiquer que le premier joueur va gagner dans le contexte
    de la logique du jeu implémentée.
    """
    print("First")
    exit()

def second():
    """
    Affiche 'Second' et termine immédiatement l'exécution du programme.
    Utilisé pour indiquer que le second joueur va gagner dans le contexte
    de la logique du jeu implémentée.
    """
    print("Second")
    exit()

# Lecture du nombre d'entiers dans la liste
n = int(input())

# Lecture de la liste d'entiers 'a'
# On suppose que l'utilisateur saisit les entiers séparés par des espaces
a = list(map(int, input().split()))

# Calcul de la valeur minimale dans la liste 'a'
min_a = min(a)

# Calcul de la somme des éléments de la liste 'a'
sum_a = sum(a)

# Calcul du reste, soit la somme des différences avec le minimum : sum(a_i - min_a)
rest = sum_a - n * min_a

# Premier cas : si 'n' (le nombre d'éléments du tableau) est impair
if n % 2 == 1:
    # Si la somme totale est paire, le second joueur gagne
    if sum_a % 2 == 0:
        second()
    # Si la somme totale est impaire, le premier joueur gagne
    if sum_a % 2 == 1:
        first()

# Si la valeur minimale de la liste est impaire, le premier joueur gagne
if min_a % 2 == 1:
    first()

# Si la somme des différences ('rest') est impaire, le premier joueur gagne
if rest % 2 == 1:
    first()

# Sinon (si 'rest' est paire), le second joueur gagne
if rest % 2 == 0:
    second()