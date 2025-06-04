def find_second_x(N, S):
    """
    Recherche la position du deuxième 'x' consécutif dans une chaîne de caractères.

    Args:
        N (int): La longueur de la chaîne S.
        S (str): La chaîne à analyser.

    Returns:
        int: L'indice où le deuxième 'x' consécutif apparaît pour la première fois,
             ou la longueur de la chaîne si aucune paire de 'x' consécutifs n'est trouvée.
    """
    # Nombre de 'x' consécutifs rencontrés
    kizetu = 0
    # Compteur de position dans la chaîne
    cnt = 0

    # Parcourt chaque caractère dans la chaîne S
    for s in S:
        # Si le caractère est 'x', on incrémente le compteur de 'x' consécutifs
        if s == "x":
            kizetu += 1
        else:
            # On réinitialise si un caractère différent est rencontré
            kizetu = 0

        # Si deux 'x' consécutifs sont trouvés, on retourne la position actuelle
        if kizetu == 2:
            return cnt

        # On avance à la position suivante
        cnt += 1
    # Aucun 'xx' n'a été trouvé, on retourne la longueur de la chaîne
    return len(S)

def main():
    """
    Lit l'entrée standard, appelle find_second_x, et affiche le résultat.
    """
    # Lecture du nombre entier N correspondant à la longueur de la chaîne (non utilisé dans la logique)
    N = int(input())
    # Lecture de la chaîne de caractères S
    S = input()
    # Appel de la fonction principale et affichage du résultat
    result = find_second_x(N, S)
    print(result)

if __name__ == "__main__":
    main()