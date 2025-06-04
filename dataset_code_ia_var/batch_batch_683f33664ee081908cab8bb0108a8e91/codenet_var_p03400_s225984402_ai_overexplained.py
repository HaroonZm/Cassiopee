# Demande à l'utilisateur de saisir un nombre entier par l'entrée standard (clavier)
# Ce nombre sera converti en entier grâce à la fonction int() et stocké dans la variable N
N = int(input())

# Demande à l'utilisateur de saisir deux entiers séparés par un espace
# La méthode input() lit la chaîne, split() la découpe en sous-chaînes
# Le générateur (int(i) for i in ...) transforme chaque sous-chaîne en entier
# Les deux entiers sont "déballés" dans les variables D et X respectivement
D, X = (int(i) for i in input().split())

# Création d'une liste nommée A
# Cette liste va contenir N entiers, chacun étant saisi via input()
# La compréhension de liste effectue une itération sur la plage de 0 à N-1 (range(N))
# Pour chaque itération, input() lit une entrée utilisateur, int() la convertit en entier, et le résultat est ajouté à la liste A
A = [int(input()) for i in range(N)]


# Définition d'une fonction nommée count qui prend en argument un entier a
def count(a):
    # tmp est une variable qui servira de compteur incrémental pour la progression de la boucle
    # On l'initialise à 1 (entier)
    tmp = 1
    # cnt compte le nombre total d'itérations qui respectent la condition tmp <= D
    # On l'initialise à 0 (aucun comptage au début)
    cnt = 0
    # i sert de multiplicateur pour a
    # On l'initialise à 1
    i = 1

    # Cette boucle while continue tant que tmp est inférieur ou égal à D
    # Cela signifie que l'on va exécuter son corps jusqu'à ce que tmp dépasse la valeur D
    while tmp <= D:
        # À chaque passage dans la boucle, on augmente cnt de 1
        cnt += 1
        # On calcule la nouvelle valeur de tmp
        # a*i donne le multiple courant de a (où i commence à 1)
        # On ajoute 1 à ce produit puis on affecte cette valeur à tmp
        tmp = a * i + 1
        # On incrémente i de 1 pour le prochain tour de boucle
        i += 1
    # Quand la condition de la boucle n'est plus respectée, on sort de la boucle et retourne cnt
    return cnt


# Initialisation d'une variable compteur à 0
cnt = 0

# On parcours chaque élément (valeur) de la liste A à l'aide d'une boucle for
for a in A:
    # Pour chaque valeur a, on calcule le résultat de count(a) (nombre d'occurrences)
    # On ajoute ce résultat à la variable cnt
    cnt += count(a)

# On affiche avec print le résultat final qui est la somme de cnt et de X
# La fonction print écrit ce résultat sur la sortie standard (généralement l'écran)
print(cnt + X)