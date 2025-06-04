# Définition de la fonction nextX prenant en entrée quatre paramètres : x, a, b, c
def nextX(x, a, b, c):
    # Retourne la valeur du calcul : (a multiplié par x) plus b, puis modulo c
    # Le symbole % signifie le reste de la division entière. Cela permet d'obtenir un résultat compris entre 0 et c-1
    return (a * x + b) % c

# Boucle infinie avec "while 1" (équivalent à "while True")
while 1:
    # Lecture d'une ligne de l'entrée standard, puis découpage en entiers
    # La fonction input() lit une chaîne depuis l'utilisateur
    # split() découpe la chaîne selon les espaces
    # map(int, ...) convertit chaque morceau en entier
    # Cela donne cinq entiers stockés dans n, a, b, c, x
    n, a, b, c, x = map(int, input().split())
    
    # Si n vaut 0, on sort de la boucle principale
    if n == 0:
        break

    # Lecture d'une nouvelle ligne de l'entrée standard, contenant n entiers
    # Ces valeurs sont attendues dans le bon ordre
    data = list(map(int, input().split()))

    # Boucle de i allant de 0 à 10000 inclus (soit 10001 tours maximum)
    for i in range(0, 10001):
        # Si le premier élément de la liste data est égal à la valeur courante de x
        if data[0] == x:
            # Supprime le premier élément de data avec la fonction del
            del data[0]
        # Si la longueur de la liste data est de 0 (autrement dit, la liste est vide)
        if len(data) == 0:
            # Affiche la valeur de i, qui indique à quel tour la liste data a été entièrement traversée
            print(i)
            # Termine la boucle for prématurément car on a atteint le but
            break
        # On calcule la prochaine valeur de x en appelant nextX avec les paramètres a, b, c
        x = nextX(x, a, b, c)
    else:
        # Si la boucle for n'a pas été interrompue par un break (autrement dit, on a fait tous les tours sans vider la liste data)
        # On affiche -1 pour indiquer que la séquence n'a pas pu être rencontrée dans la limite autorisée
        print(-1)