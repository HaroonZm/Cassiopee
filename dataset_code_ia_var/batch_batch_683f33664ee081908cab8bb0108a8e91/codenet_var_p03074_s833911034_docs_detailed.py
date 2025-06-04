def max_consecutive_ones_after_flips():
    """
    Lit une chaîne binaire et un nombre d'opérations de flip autorisées (k),
    puis détermine la longueur maximale d'une sous-séquence contiguë d'au plus
    k sous-séquences de '0' qui peuvent être retournées en '1', de manière à obtenir
    la plus longue sous-séquence contiguë possible de '1'.

    Entrée:
        Première ligne : deux entiers n (taille de la chaîne) et k (nombre de sous-séquences '0' que l'on peut retourner)
        Deuxième ligne : chaîne s composée de '0' et '1'

    Sortie:
        Imprime un entier représentant la longueur maximale atteignable sous les contraintes.
    """

    # Lecture des entrées
    n, k = map(int, input().split())  # n: longueur de la chaîne, k: nombre de flips autorisés
    s = input()  # La chaîne binaire
    rest = k     # Nombre de flips restants
    i = 0        # Pointeur sur la position actuelle dans la chaîne

    # Première phase : trouver la plus longue sous-chaîne possible en partant du début
    # en transformant au plus k plages de '0' en '1'
    while i < n:
        if s[i] == '1':
            # Avancer sur les '1'
            i += 1
        else:
            # Dès qu'on rencontre un '0'
            if rest == 0:
                # Plus de flips disponibles, on arrête
                break
            rest -= 1  # Utilisation d'un flip
            # Avancer sur tous les '0' consécutifs (une plage)
            while i < n and s[i] == '0':
                i += 1

    ans = i  # Longueur de la fenêtre maximale atteinte en partant du début

    # Deuxième phase : faire glisser la fenêtre pour explorer d'autres positions possibles
    j = 0  # Deuxième pointeur pour marquer le début de la fenêtre
    while i < n:
        # Avancer i sur les '0' consécutifs (sortie d'une plage de '0' ajoutée à la fenêtre)
        while i < n and s[i] == '0':
            i += 1
        # Avancer i sur les '1' atteints juste après cette plage de '0'
        while i < n and s[i] == '1':
            i += 1
        # Avancer j pour sauter la première plage de '1' devenue extérieure à la fenêtre
        while j < n and s[j] == '1':
            j += 1
        # Avancer j pour sortir de la première plage de '0' traitée en début de fenêtre
        while j < n and s[j] == '0':
            j += 1
        # Mettre à jour la réponse maximale trouvée
        ans = max(ans, i - j)

    # Affichage du résultat
    print(ans)


# Appel de la fonction principale qui gère toute la logique
max_consecutive_ones_after_flips()