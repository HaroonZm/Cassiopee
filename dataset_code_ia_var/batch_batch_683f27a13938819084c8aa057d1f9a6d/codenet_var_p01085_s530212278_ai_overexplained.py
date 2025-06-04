# Démarrez une boucle infinie qui va continuer jusqu'à ce qu'on la quitte explicitement avec 'break'
while True:
    # Attendez une ligne d'entrée utilisateur, séparez la chaîne saisie en éléments, transformez chacun en entier,
    # et affectez les trois premiers entiers à m, minn, maxn respectivement.
    m, minn, maxn = map(int, input().split())

    # Si tous les trois entiers lus (m, minn et maxn) sont égaux à 0, on interprète cela comme une condition d'arrêt,
    # donc on quitte la boucle grâce à 'break', ce qui arrêtera l'exécution du code à la boucle 'while'
    if m == minn == maxn == 0:
        break

    # Créez une liste nommée 'P', qui contiendra 'm' entiers.
    # Pour cela, effectuez une itération sur une séquence de longueur 'm', 
    # et pour chaque itération, lisez un entier depuis l'entrée utilisateur, 
    # convertissez chaque entrée en entier avec int(input()), et stockez-la dans la liste.
    P = [int(input()) for i in range(m)]

    # Initialisez la variable 'ansd' à 0.
    # Cette variable va stocker la différence maximale trouvée (parmi les critères du problème) au fur et à mesure de la boucle.
    ansd = 0

    # Initialisez la variable 'ansi' à 0.
    # Cette variable va retenir l'indice (conforme à certains critères) associé à la différence maximale sauvegardée dans 'ansd'.
    ansi = 0

    # Lancez une boucle sur la variable 'i', en commençant à la valeur 'minn-1' jusqu'à 'maxn-1' inclus,
    # c'est-à-dire de 'minn-1' à 'maxn-1', que l'on écrit 'for i in range(minn-1, maxn)' car 'range' est exclusif sur la borne supérieure.
    for i in range(minn-1, maxn):
        # Calculez la différence entre l'élément d'indice i de la liste 'P' et celui d'indice i+1,
        # soit 'P[i] - P[i+1]'.
        # Si cette différence est supérieure ou égale à la valeur courante de 'ansd', alors:
        if P[i] - P[i+1] >= ansd:
            # On met à jour la variable 'ansd' avec la nouvelle différence, car elle est plus grande
            # ou égale à celle précédemment stockée dans 'ansd'.
            ansd = P[i] - P[i+1]

            # On met à jour 'ansi' avec la valeur de 'i+1', car on souhaite retenir l'indice correspondant 
            # (probablement l'indice où la plus grande différence a eu lieu dans ce contexte).
            ansi = i+1

    # Après avoir terminé l'analyse des indices concernés et trouvé la position demandée,
    # affichez la valeur de 'ansi' sur la sortie standard, c'est-à-dire affichez l'entier à l'écran.
    print(ansi)