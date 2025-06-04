"""
AOJ 1011: Finding the Largest Carbon Compound

Ce script calcule et affiche la valeur correspondant à un indice donné dans une
séquence particulière, utilisée dans le problème AOJ 1011.

La séquence est générée récursivement :
    a[1] = 1
    a[2] = 2
    Pour i >= 3: a[i] = 3*a[i-2] + 2

À chaque entrée utilisateur (un entier i), la valeur a[i] est affichée.

Auteur d'origine : bal4u, 2018-07-04. Réécrit avec des commentaires et docstrings.
"""

def precompute_sequence(max_index):
    """
    Précalcule la séquence jusqu'à un indice maximal donné.

    Args:
        max_index (int): L'indice maximal à calculer (inclusif).

    Returns:
        list: Une liste contenant les valeurs de la séquence telles que définies.
    """
    a = [0] * (max_index + 1)
    # Initialisation des deux premières valeurs selon l'énoncé
    a[1] = 1
    a[2] = 2
    # Calcul des valeurs de la séquence à partir du 3ème élément
    for i in range(3, max_index + 1):
        a[i] = 3 * a[i - 2] + 2
    return a

def main():
    """
    Fonction principale du script.
    - Précalcule la séquence pour les indices 1 à 30.
    - Lit les indices depuis l'entrée standard.
    - Pour chaque indice, affiche la valeur correspondante de la séquence.
    - Arrête l'exécution en cas de fin d'entrée ou d'erreur d'entrée.
    """
    # Précalcule la séquence jusqu'à l'indice 30 (inclus)
    a = precompute_sequence(31)
    while True:
        try:
            # Lit un indice depuis l'entrée utilisateur
            i = int(input())
        except Exception:
            # Si une erreur survient (fin d'entrée typiquement), arrêter la boucle
            break
        # Affiche la valeur de la séquence à l'indice i
        print(a[i])

if __name__ == "__main__":
    # Appel de la fonction principale si ce script est exécuté directement
    main()