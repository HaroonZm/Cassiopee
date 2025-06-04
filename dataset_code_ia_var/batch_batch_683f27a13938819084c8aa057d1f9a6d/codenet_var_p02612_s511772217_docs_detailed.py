def calculate_subtraction_to_next_1000(n):
    """
    Calcule combien il faut soustraire à n pour atteindre le multiple de 1000 supérieur.

    Plus précisément, cette fonction retourne le résultat de l'expression :
    1000 - ((n - 1) % 1000 + 1)
    Ce calcul donne le complément à 1000 du reste obtenu par (n - 1) modulo 1000, ajusté de +1.
    
    Args:
        n (int): Un entier dont on veut calculer le complément à 1000 en suivant la formule donnée.
    
    Returns:
        int: La valeur à soustraire pour atteindre le prochain multiple de 1000, selon la formule.
    """
    # On décale n de -1 pour l'opération modulo
    shifted_n = n - 1
    # On calcule le reste de la division par 1000
    remainder = shifted_n % 1000
    # On ajoute 1 au reste
    adjusted_remainder = remainder + 1
    # On calcule le complément à 1000 de la valeur précédente
    result = 1000 - adjusted_remainder
    return result

def main():
    """
    Lit un entier depuis l'entrée standard, applique le calcul et affiche le résultat.
    """
    # Lecture de l'entier depuis l'entrée utilisateur
    n = int(input())
    # Calcul du résultat selon la fonction dédiée
    answer = calculate_subtraction_to_next_1000(n)
    # Affichage du résultat
    print(answer)

if __name__ == "__main__":
    main()