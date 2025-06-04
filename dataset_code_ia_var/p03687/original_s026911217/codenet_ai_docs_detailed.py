def min_operations_to_single_char():
    """
    Demande à l'utilisateur une chaîne de caractères, et pour chaque caractère distinct de la chaîne, calcule 
    le nombre minimal d'opérations nécessaires pour transformer la chaîne en une chaîne composée uniquement 
    de ce caractère. À chaque opération, pour chaque paire consécutive où l'un des caractères correspond au 
    caractère cible, on attribue la valeur cible à la position du nouveau tableau. 
    Affiche le nombre minimal d'opérations sur tous les caractères possibles.
    """
    from copy import deepcopy  # Importation pour créer une copie profonde des listes

    # Alphabet minuscule anglais; inutilisé dans la logique principale, mais éventuellement prévu pour référence
    alpha = "abcdefghijklmnopqrstuvwxyz"
    # Convertit l'entrée standard de l'utilisateur en liste de caractères
    s = list(input())

    ans = 10**9  # Initialise la valeur minimale d'opérations à une valeur très haute

    # Boucle sur chaque caractère de la chaîne d'entrée
    for c in s:
        # Crée une copie de la chaîne d'origine à transformer
        s_c = deepcopy(s)
        counter = 0  # Initialise le compteur d'opérations

        # Continue jusqu'à ce que la chaîne courante soit composée uniquement du caractère cible
        while set(s_c) != {c}:
            counter += 1  # Incrémente le compteur à chaque opération
            new = []  # Nouvelle version de la chaîne après modification

            # Parcourt la chaîne actuelle et construit la nouvelle chaîne selon la règle :
            # Si au moins un des deux caractères consécutifs vaut le caractère cible, on place le caractère cible dans la nouvelle chaîne
            for i in range(len(s_c)-1):
                if s_c[i] == c or s_c[i+1] == c:
                    new.append(c)
                else:
                    new.append(0)  # 0 utilisé comme valeur fictive pour indiquer l'absence du caractère cible

            s_c = new  # Met à jour la chaîne courante

        # Met à jour la réponse avec le nombre d'opérations minimal trouvé jusqu'ici
        ans = min(ans, counter)

    # Affiche la valeur minimale obtenue
    print(ans)