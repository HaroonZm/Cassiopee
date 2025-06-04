def get_divisors(n):
    """
    Calcule et renvoie la liste des diviseurs propres de n (excluant n lui-même).

    Args:
        n (int): Le nombre entier pour lequel on souhaite trouver les diviseurs.

    Returns:
        list: Une liste contenant tous les diviseurs propres de n.
    """
    divisors = set()  # Utilisation d'un ensemble pour éviter les doublons
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            if i != n // i and n // i != n:
                # Ajouter aussi le diviseur complémentaire (sauf n lui-même)
                divisors.add(n // i)
    if n in divisors:
        divisors.remove(n)  # Exclure n lui-même
    return list(divisors)


def classify_number(n):
    """
    Détermine si un nombre est parfait, déficient ou abondant.

    Args:
        n (int): Le nombre entier à classifier.

    Returns:
        str: Une chaîne décrivant le type du nombre :
            - "perfect number" si le nombre est parfait,
            - "deficient number" si le nombre est déficient,
            - "abundant number" si le nombre est abondant.
    """
    divisors = get_divisors(n)
    divisors_sum = sum(divisors)
    if divisors_sum == n:
        return "perfect number"
    elif divisors_sum < n:
        return "deficient number"
    else:
        return "abundant number"


def main():
    """
    Fonction principale qui exécute une boucle pour lire des entiers et
    affiche pour chacun s'il est parfait, déficient ou abondant.
    La boucle s'arrête lorsque l'utilisateur saisit 0.
    """
    while True:
        n = int(input("Entrez un nombre entier (0 pour arrêter) : "))
        if n == 0:
            break  # Arrêter la boucle si l'utilisateur saisit 0
        result = classify_number(n)
        print(result)


if __name__ == '__main__':
    main()