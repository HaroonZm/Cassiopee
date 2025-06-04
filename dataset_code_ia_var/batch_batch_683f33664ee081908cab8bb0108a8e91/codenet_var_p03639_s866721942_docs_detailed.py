def count_even_odd_classes(numbers):
    """
    Calcule le nombre d'entiers d'une liste qui sont divisibles par 4 (mod_4),
    divisibles par 2 mais pas par 4 (mod_2), et retourne ces deux comptages.

    Args:
        numbers (list of int): Liste d'entiers à analyser.

    Returns:
        tuple: (mod_4, mod_2)
            mod_4 (int): Nombre d'entiers divisibles par 4.
            mod_2 (int): Nombre d'entiers divisibles par 2 mais pas par 4.
    """
    mod_4 = 0  # Compteur pour les nombres divisibles par 4
    mod_2 = 0  # Compteur pour les nombres divisibles par 2 mais pas par 4
    for a_i in numbers:
        if a_i % 4 == 0:
            mod_4 += 1
        elif a_i % 2 == 0:
            mod_2 += 1
    return mod_4, mod_2

def compute_threshold(mod_4, mod_2):
    """
    Calcule le seuil 'm' utilisé pour déterminer la validité de la configuration,
    basé sur les règles du problème.

    Args:
        mod_4 (int): Nombre d'entiers divisibles par 4.
        mod_2 (int): Nombre d'entiers divisibles par 2 mais pas par 4.

    Returns:
        int: La valeur limite 'm' à comparer avec N.
    """
    if mod_2 == 0:
        m = 2 * mod_4 + 1
    else:
        m = 2 * mod_4 + mod_2
    return m

def main():
    """
    Fonction principale qui lit les entrées standard, calcule les différentes
    classes modulo, puis évalue la condition finale pour afficher 'Yes' ou 'No'.
    """
    # Lecture du nombre d'entiers à traiter
    N = int(input())
    # Lecture de la liste d'entiers
    a = list(map(int, input().split()))

    # Analyse des classes modulo pour la liste d'entiers
    mod_4, mod_2 = count_even_odd_classes(a)
    # Calcul du seuil m à utiliser pour la condition
    m = compute_threshold(mod_4, mod_2)

    # Comparaison finale et affichage du résultat selon la condition du problème
    if m >= N:
        print('Yes')
    else:
        print('No')

# Exécution du programme principal
if __name__ == "__main__":
    main()