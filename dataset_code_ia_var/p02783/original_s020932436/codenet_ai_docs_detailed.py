def compute_min_attacks(h, a):
    """
    Calcule le nombre minimal d'attaques nécessaires pour réduire la santé 'h' à zéro ou moins,
    sachant que chaque attaque inflige 'a' points de dégâts.

    Paramètres:
    h (int): La santé totale de l'ennemi.
    a (int): Le nombre de dégâts par attaque.

    Retourne:
    int: Le nombre minimal d'attaques nécessaires.
    """
    # Si la santé est exactement divisible par les dégâts,
    # le nombre d'attaques est la division entière.
    if h % a == 0:
        return h // a
    else:
        # Sinon, il faut une attaque supplémentaire pour finir l'ennemi.
        return h // a + 1

def main():
    """
    Lit l'entrée standard pour obtenir la santé de l'ennemi et les dégâts par attaque,
    puis affiche le nombre minimal d'attaques nécessaires.
    """
    # Lire deux entiers depuis l'entrée séparés par un espace
    h, a = map(int, input().split())

    # Calculer et afficher le résultat
    print(compute_min_attacks(h, a))

if __name__ == '__main__':
    main()