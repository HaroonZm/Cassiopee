def calculate_special_sum(a):
    """
    Calcule et retourne la valeur maximale possible obtenue en partitionnant le tableau selon des règles basées sur l'opération XOR et la base de Gauss.
    
    Cette fonction sélectionne un sous-ensemble d'éléments de `a` (appelé 'blu') pour construire une base linéaire maximale en utilisant la méthode de réduction de Gauss sur le XOR binaire puis forme deux groupes dont la somme des XOR est la plus grande possible.
    
    Args:
        a (list of int): Liste des entiers sur lesquels appliquer l'algorithme.
    Returns:
        int: Le maximum de (XOR(blu) + XOR(rest)), où 'rest' sont les éléments restants et 'blu' la base construite.
    """

    n = len(a)  # Nombre d'éléments dans la liste
    sums = 0    # Sera le XOR total de tous les éléments de la liste

    # Calcul du XOR total
    for x in a:
        sums ^= x

    # blu : indices des éléments sélectionnés pour construire la "base"
    blu = set()

    # remain : indices encore disponibles pour être sélectionnés dans la base
    remain = set(range(n))

    # Parcours des 61 bits possibles du plus grand au plus petit (64 bits - quelques bits réservés à la précision)
    for i in range(60, -1, -1):
        # Vérifie si le bit i du XOR global est à 0, sinon pas la peine d'essayer de construire une base sur ce bit
        if (sums >> i) & 1 == 0:
            di = -1  # Indice d'un élément qui a le bit i à 1

            # Recherche d'un élément parmi les restants qui a le bit i à 1
            for j in remain:
                if (a[j] >> i) & 1 == 1:
                    di = j
                    break

            if di != -1:
                # On ajoute cet élément à la "base" blu
                blu.add(di)
                remain.remove(di)
                # Réduction Gaussienne : pour chaque autre élément ayant aussi un 1 sur le bit i, on l'XOR avec a[di]
                for j in range(n):
                    if j != di and (a[j] >> i) & 1 == 1:
                        a[j] ^= a[di]

    # Calcul du XOR des éléments sélectionnés pour "blu"
    bsum = 0
    for i in blu:
        bsum ^= a[i]

    # La somme maximale possible est la somme du XOR (bsum) de la base et le XOR du reste (sums ^ bsum)
    return bsum + (sums ^ bsum)

def main():
    """
    Point d'entrée du programme : lit les entrées, applique l'algorithme et affiche la réponse.
    """
    # Lecture du nombre d'éléments
    n = int(input())
    # Lecture de la liste d'entiers
    a = list(map(int, input().split()))
    # Application de l'algorithme et affichage du résultat
    print(calculate_special_sum(a))

# Appel du point d'entrée principal du programme
if __name__ == "__main__":
    main()