#!/usr/bin/env python3

def solve(n, m, a, b, ds):
    """
    Détermine le nombre maximal d'éléments à considérer comme 'gaspillage' dans une séquence soumise à des seuils.

    Un élément est initialement marqué comme 'gaspillage' si sa valeur est supérieure ou égale à 'a'.
    Si le nombre d'éléments marqués dépasse la limite autorisée (n - m), certains sont potentiellement désélectionnés,
    en considérant ceux qui sont parmi les derniers et qui respectent un autre seuil 'b'.

    Args:
        n (int): Nombre total d'éléments dans la séquence.
        m (int): Nombre d'éléments qui ne peuvent pas être considérés comme 'gaspillage'.
        a (int): Seuil initial pour marquer un élément comme 'gaspillage'.
        b (int): Seuil secondaire pour réévaluer certains éléments comme non 'gaspillage'.
        ds (List[int]): La séquence des valeurs des éléments.

    Returns:
        int: Le nombre total d'éléments considérés comme 'gaspillage' après application des règles.
    """
    # Initialisation de la liste des éléments 'gaspillage' (False = non gaspillé, True = gaspillé)
    is_waste = [False for _ in range(n)]
    # Marquer les premiers éléments supérieurement ou également à 'a' comme 'gaspillage'
    for i in range(n):
        if ds[i] >= a:
            is_waste[i] = True
        else:
            # Arrêter dès qu'un élément ne satisfait plus la condition
            break
    # Si le nombre d'éléments 'gaspillage' dépasse le seuil (n - m)
    if sum(is_waste) > n - m:
        # Parcourir la séquence à l'envers
        for i in range(n - 1, -1, -1):
            if is_waste[i]:
                # Si la valeur est inférieure ou égale à 'b', révoquer le statut de 'gaspillage'
                if ds[i] <= b:
                    is_waste[i] = False
                else:
                    # Dès que la condition n'est plus vérifiée, arrêter
                    break
    # Retourner le total des éléments considérés comme 'gaspillage'
    return sum(is_waste)

def main():
    """
    Fonction principale pour l'exécution du programme en ligne de commande.

    Lit les valeurs depuis l'entrée standard (quatre entiers puis une liste d'entiers),
    résout le problème et affiche le résultat.
    """
    # Lecture des paramètres de la première ligne : n, m, a, b
    n, m, a, b = map(int, input().split())
    # Lecture des valeurs de la liste ds
    ds = list(map(int, input().split()))
    # Appel de la fonction solve et affichage du résultat
    print(solve(n, m, a, b, ds))

if __name__ == '__main__':
    main()