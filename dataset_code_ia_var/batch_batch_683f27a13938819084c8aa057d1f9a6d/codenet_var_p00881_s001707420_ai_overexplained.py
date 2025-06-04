from collections import Counter  # Importe la classe Counter du module collections, utilisée pour compter les objets immuables comme des entiers dans ce cas.

# Boucle infinie qui permet de traiter plusieurs cas de test jusqu'à une condition d'arrêt explicite.
while True:
    # Lit une ligne sur l'entrée standard, sépare la chaîne sur chaque espace, convertit chaque morceau en entier et affecte aux variables m et n.
    # Cette opération de décomposition correspond respectivement au nombre m de bits et à n le nombre d'objets.
    m, n = (int(s) for s in input().split())
    
    # Teste si m vaut 0 ; si c'est le cas, on considère que la séquence des cas de test est terminée, donc on quitte la boucle.
    if not m:
        break

    # Construit une liste 'objects' de taille n où chaque élément est la conversion d'une chaîne binaire entrée par l'utilisateur (ex: "1011") en entier décimal.
    objects = [int(input(), 2) for i in range(n)]

    # Prépare une structure de données dynamique pour la programmation dynamique.
    # Crée une liste 'dp' avec 2**m (autrement dit, 1 << m) éléments ;
    # chaque élément est un bytearray de taille 2**m, initialisé à zéro.
    # 'dp[asked][masked]' stockera le résultat calculé pour un état donné (asked, masked).
    dp = [bytearray(1 << m) for i in range(1 << m)]

    # Crée une liste 'bits' contenant 2**i pour chaque valeur i de 0 à m-1.
    # Ceci sert à représenter chaque position de bit individuellement dans un entier de m bits.
    bits = [1 << i for i in range(m)]

    # On parcourt 'asked' à l'envers (de 2**m - 2 à 0 inclus).
    # 'asked' représente l'ensemble des bits déjà "demandés" ou "utilisés".
    for asked in reversed(range((1 << m) - 1)):
        # Pour chaque valeur unique 'masked' obtenue en effectuant un ET binaire ('&') entre chaque objet et 'asked',
        # on compte combien de fois chaque résultat ('masked') survient grâce à Counter.
        # Ex: si asked=0011, obj=1011, alors obj & asked = 0011.
        for masked, count in Counter(obj & asked for obj in objects).items():
            # Si plus d'un objet partage le même masque (après masquage), il faudra subdiviser ce groupe plus loin.
            if count > 1:
                # Pour toutes les positions de bit b qui ne sont pas encore "demandées" (pas présentes dans asked),
                # on regarde deux cas pour chaque sous-groupe possible :
                #   1) On ajoute le bit b à asked, mais masked reste le même (on ne sait toujours pas la valeur de ce bit pour ce groupe).
                #   2) On ajoute le bit b à asked ET à masked (on suppose alors que le bit b vaut 1 pour ce sous-groupe).
                # Pour chacune de ces possibilités, on prend le maximum des cas (le pire cas), sur tous les bits b non demandés.
                # Enfin, parmi tous ces maximums pour chaque bit possible, on prend le minimum (stratégie optimale).
                # On ajoute 1 pour tenir compte de la requête actuelle.
                dp[asked][masked] = min(
                    max(
                        dp[asked + b][masked],  # Cas où le bit b est ajouté à 'asked', mais pas à 'masked'.
                        dp[asked + b][masked + b]  # Cas où le bit b est ajouté à la fois à 'asked' et à 'masked'.
                    )
                    for b in bits if not b & asked  # On considère les bits qui n'ont pas déjà été ajoutés à 'asked'.
                ) + 1  # On ajoute 1, car on fait une requête supplémentaire dans cet état.

    # Affiche le résultat : le nombre minimal d'opérations nécessaires pour distinguer tous les objets,
    # c'est-à-dire avec 0 bit demandé et 0 masque initial.
    print(dp[0][0])