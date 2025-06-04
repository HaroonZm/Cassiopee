# Définition de la fonction principale "main" qui prend en entrée trois paramètres :
# - m : un entier représentant le nombre d'éléments à lire
# - nx : un entier utilisé comme borne supérieure d'une plage (probablement "nmax")
# - nn : un entier utilisé comme borne inférieure d'une plage (probablement "nmin")
def main(m, nx, nn):
    # Création d'une liste "b" qui va contenir des entiers fournis par l'utilisateur.
    # La compréhension de liste [int(input()) for i in range(m)] veut dire :
    # - Boucle "for i in range(m)" itère de 0 jusqu'à m-1 (m non inclus)
    # - À chaque itération, on demande à l'utilisateur une entrée avec input()
    #   qu'on convertit en entier avec int(), puis cet entier est ajouté à la liste.
    b = [int(input()) for i in range(m)]
    
    # Initialisation d'une variable "d" qui va servir à stocker la plus grande différence trouvée.
    # Elle est initialisée à -1, une valeur plus petite que toute différence positive entre deux entiers.
    d = -1
    
    # Boucle "for" parcourant i allant de nn jusqu'à nx (inclus, car range est de nn à nx+1).
    # Cela signifie que tous les entiers de nn à nx vont être utilisés comme index pour les calculs.
    for i in range(nn, nx + 1):
        # Calcul de la différence entre l'élément précédent dans la liste "b" (b[i-1])
        # et l'élément courant (b[i]). On soustrait b[i] de b[i-1].
        # Note : Les listes sont indexées à partir de 0 en Python.
        if d <= b[i - 1] - b[i]:
            # Si la différence calculée (b[i-1] - b[i]) est supérieure ou égale à "d",
            # alors on met à jour "d" avec cette nouvelle différence plus grande.
            d = b[i - 1] - b[i]
            # On mémorise aussi la valeur de "i" dans la variable "ans", indiquant 
            # l'indice où a eu lieu la meilleure différence.
            ans = i
    # Affichage de la valeur finale de "ans" indiquant où la différence maximale a été trouvée.
    print(ans)


# Le bloc suivant est la boucle principale du programme (parfois appelée "boucle infinie")
# tant que l'utilisateur ne souhaite pas arrêter le programme.
while 1:
    # On demande à l'utilisateur de saisir trois entiers sur la même ligne, séparés par des espaces :
    # - m      : le nombre d'éléments à traiter
    # - nmin   : une borne inférieure
    # - nmax   : une borne supérieure
    # map(int, input().split()) sert à :
    # - découper la chaîne entrée en liste avec split()
    # - convertir chaque sous-chaîne en entier via map(int, ...)
    # - "m, nmin, nmax =" permet d'assigner simultanément les trois valeurs à trois variables
    m, nmin, nmax = map(int, input().split())
    
    # Condition d'arrêt : si les trois valeurs saisies sont égales à 0,
    # alors tous les tests sont finis, on sort de la boucle avec break.
    if m == nmax == nmin == 0:
        break
    # Appel de la fonction "main" pour traiter le cas courant.
    # Ici, il y a une inversion des paramètres nmax et nmin dans l'appel à main().
    # - le second argument correspond à nmax (borne supérieure)
    # - le troisième argument est nmin (borne inférieure)
    # Ceci est conforme à la définition de main(m, nx, nn)
    main(m, nmax, nmin)