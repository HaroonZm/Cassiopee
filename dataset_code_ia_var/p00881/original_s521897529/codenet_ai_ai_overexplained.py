from collections import Counter  # Importe l'objet Counter pour compter les éléments de façon efficace

while True:  # Boucle infinie, s'exécutera jusqu'à un break explicite
    # Demande à l'utilisateur 2 entiers séparés par des espaces
    # map(int, ...) applique int à chaque sous-élément de l'input().split()
    # On utilise l'affectation multiple et une expression génératrice pour obtenir m et n
    m, n = (int(s) for s in input().split())
    # Si m est nul (0), alors on sort de la boucle (terminaison du programme)
    if not m:
        break

    # Crée une liste 'objects' contenant n éléments ;
    # pour chaque élément, lit un input binaire (ex: '0101'), le convertit en entier de base 2
    objects = [int(input(), 2) for i in range(n)]
    # Crée une liste dp de taille (2 puissance m).
    # Pour chaque valeur possible de mask (masque binaire sur m bits), dp[mask] est un tableau d'octets de taille (2 puissance m).
    # Le but est d'utiliser dp[mask][masked] pour stocker des résultats intermédiaires liés à la dynamique du problème.
    dp = [bytearray(1 << m) for i in range(1 << m)]
    # Crée une liste 'bits', contenant les valeurs correspondant à chaque bit individuel dans m positions.
    # Par exemple, si m = 3, bits = [1, 2, 4] (c'est-à-dire 001b, 010b, 100b)
    bits = [1 << i for i in range(m)]

    # Itération sur tous les masques binaires possibles à m bits,
    # sauf le masque complet (on part du plus grand incomplet vers le plus petit)
    # reversed(range((1 << m) - 1)) génère la séquence de tous les entiers de 0 à 2^m-2 en ordre décroissant
    for mask in reversed(range((1 << m) - 1)):
        # Compte pour chaque objet, sa valeur masquée par 'mask' (bitwise AND),
        # puis stocke le compte de chaque valeur possible dans Counter
        for masked, count in Counter(obj & mask for obj in objects).items():
            # Si au moins deux objets ont la même valeur masquée sous le même 'mask'
            # (donc, il y a au moins une collision ou duplicata pour ce masque-là)
            if count > 1:
                # On va mettre à jour dp[mask][masked] pour ce couple (mask, masked)
                # L'idée est de tester, pour chaque bit non encore activé dans le masque (i.e. chaque b tel que b & mask == 0)
                # la valeur suivante est min() sur ces bits de :
                #   max(dp[mask + b][masked],         <- on ne modifie pas le sous-masque (pas de nouvelle distinction)
                #       dp[mask + b][masked + b])     <- on sépare les groupes qui diffèrent sur le bit b
                # +1 car on ajoute une opération (une "question")
                dp[mask][masked] = min(
                    max(
                        dp[mask + b][masked],        # cas où le bit b ne change pas la distinction
                        dp[mask + b][masked + b]     # cas où le bit b permet de distinguer différemment
                    ) + 1                           # passage à l'étape suivante ou à la profondeur suivante
                    for b in bits if not b & mask   # ne prendre que les bits b qui ne sont pas déjà présents dans le masque
                )
    # Après avoir construit dp, on affiche la réponse finale correspondant au masque vide et au sous-masque vide
    print(dp[0][0])  # Affiche le résultat demandé pour le problème posé