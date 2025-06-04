# Demande à l'utilisateur d'entrer une valeur, puis convertit cette valeur (qui est sous forme de chaîne de caractères) en un entier.
N = int(input())

# Initialise un compteur pour le nombre de fois où la chaîne "A" va apparaître. Il est initialisé à zéro car aucune entrée n'a encore été lue.
a = 0

# Initialise un compteur pour toutes les autres entrées différentes de "A". Il est également initialisé à zéro.
un = 0

# Initialise une variable indicatrice ("flag") nommée 'no' à zéro. Cette variable sera utilisée pour vérifier si une condition spécifique a été rencontrée.
no = 0

# Lance une boucle for qui va s'exécuter exactement N fois. 'range(N)' produit les entiers de 0 à N-1 inclus.
for i in range(N):
    # À chaque itération, lit une nouvelle chaîne de caractères entrée par l'utilisateur.
    s = input()
    
    # Vérifie si la valeur de la chaîne lue ('s') est exactement égale à la lettre "A".
    if s == "A":
        # Si c'est le cas, incrémente la variable 'a' de un.
        a += 1
    else:
        # Si ce n'est pas "A", incrémente le compteur 'un' de un.
        un += 1
    
    # Vérifie si le nombre d'éléments non-"A" ('un') est supérieur au nombre d'éléments "A" ('a').
    if un > a:
        # Si cette condition est vraie, affiche immédiatement "NO" à l'écran.
        print("NO")
        # Modifie la variable indicatrice 'no' pour indiquer qu'une condition d'arrêt s'est produite.
        no = 1
        # Interrompt la boucle en utilisant 'break' car la condition souhaitée n'est plus respectée.
        break

# Après la boucle, vérifie si le nombre de "A" ('a') est différent du nombre d'autres éléments ('un')
# et également que la variable indicatrice 'no' est restée à 0, ce qui signifie qu'aucune rupture n'a eu lieu plus tôt.
if a != un and not no:
    # Si c'est le cas, imprime "NO" à l'écran car les deux valeurs ne sont pas égales.
    print("NO")
# Si la variable 'no' est encore à zéro, ce qui veut dire qu'aucune condition d'erreur n'a été rencontrée
elif not no:
    # Dans ce cas, imprime "YES" à l'écran pour signaler que toutes les conditions sont remplies.
    print("YES")