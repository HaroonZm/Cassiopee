def split(x):
    """
    Prend un entier x et tente de le diviser en deux parties à chaque position possible,
    multiplie les deux parties (interprétées comme des entiers) et conserve les résultats possibles.
    Retourne la plus grande valeur obtenue par cette opération. 
    Si x est un nombre à un chiffre, retourne None.

    Args:
        x (int): Entier positif à diviser et multiplier.

    Returns:
        int or None: Le maximum des produits possibles, ou None s'il n'y en a pas.
    """
    assert isinstance(x, int), "L'argument doit être un entier."
    sx = str(x)  # Convertit l'entier en chaîne pour manipulation par indice
    l = len(sx)  # Longueur de la chaîne de chiffres
    candidates = []  # Liste pour stocker tous les produits possibles

    # Parcourt chaque position de découpe possible sauf à l'extrémité
    for idx in range(1, l):
        # Partitionne sx en deux sous-chaines
        # Partie gauche : sx[:idx], partie droite : sx[idx:]
        first = sx[idx:]  # Cette variable n'est pas utilisée, peut être supprimée
        left = int(sx[:idx])
        right = int(sx[idx:])
        product = left * right
        candidates.append(product)  # Ajoute le produit à la liste

    # Si aucune découpe valide (nombre à un chiffre), retourne None
    if len(candidates) == 0:
        return None
    else:
        # Retourne le plus grand produit trouvé
        return max(candidates)

def problem1():
    """
    Fonction principale qui gère plusieurs cas de test.

    Pour chaque entier N fourni, applique la fonction split de façon répétée :
      - À chaque itération, N est remplacé par le plus grand produit de la découpe (par split).
      - Le processus s'arrête si split retourne None (nombre à un chiffre) ou si le résultat ne change plus (boucle infinie).
      - Compte le nombre d'étapes jusqu'à ce que le processus prenne fin ; s'il y a une boucle infinie, retourne -1.

    Les réponses pour tous les cas de test sont affichées, une par ligne.
    """
    Q = input()  # Lit le nombre de cas de test
    answers = []  # Liste pour stocker les résultats pour chaque cas de test

    # Itère sur chaque cas de test
    for _ in range(int(Q)):
        N = int(input())  # Lit la valeur d'entrée pour ce cas de test
        x = N
        cnt = 0  # Compte le nombre d'itérations nécessaires

        # Applique split tant que possible, s'arrête si None ou boucle infinie détectée
        while True:
            next_x = split(x)
            if next_x is None:
                # Si on ne peut plus diviser, on arrête
                break
            elif x == next_x:
                # Si on tombe dans une boucle sans changement, -1
                cnt = -1
                break
            else:
                cnt += 1  # On compte cette opération
            x = next_x  # Prend la nouvelle valeur obtenue

        answers.append(str(cnt))  # Stocke le résultat de ce cas de test

    # Affiche toutes les réponses, une par ligne
    print('\n'.join(answers))

if __name__ == '__main__':
    # Exécute la fonction principale quand le script est lancé directement
    problem1()