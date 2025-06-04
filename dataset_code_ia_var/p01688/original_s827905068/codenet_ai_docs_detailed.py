def read_input():
    """
    Lit la valeur entière D puis les listes de paires d'entrées.  
    Les deux listes sont constituées d'une chaîne et d'un entier.

    Returns:
        tuple: (D, d1, d2) où
            - D (int) : Nombre d'éléments à traiter
            - d1 (list) : Liste des entrées (catégorie, valeur) du premier groupe
            - d2 (list) : Liste des entrées (catégorie, valeur) du second groupe
    """
    # Lecture de la valeur D
    D = int(input())
    # Lecture du nombre d'éléments pour le premier groupe
    n1 = int(input())
    d1 = []
    for _ in range(n1):
        # Lecture et séparation de la catégorie et de la valeur pour chaque entrée
        parts = input().split()
        d1.append((parts[0], int(parts[1])))
    # Lecture du nombre d'éléments pour le second groupe
    n2 = int(input())
    d2 = []
    for _ in range(n2):
        parts = input().split()
        d2.append((parts[0], int(parts[1])))
    return D, d1, d2

def extract_sorted_values(entries, category):
    """
    Extrait et trie dans l'ordre décroissant les valeurs des entrées appartenant à une catégorie donnée.

    Args:
        entries (list): Liste des tuples (catégorie, valeur).
        category (str): Catégorie à filtrer.

    Returns:
        list: Liste décroissante des valeurs pour la catégorie spécifiée.
    """
    # Filtrer par catégorie et prendre la valeur entière
    values = [value for cat, value in entries if cat == category]
    # Retourner la liste triée dans l'ordre décroissant
    return sorted(values, reverse=True)

def compute_max_sum(D, p1, p2):
    """
    Calcule la somme maximale obtenue en choisissant i éléments de p1 et (D-i)//2 éléments de p2.

    Args:
        D (int): Nombre total d'éléments à sélectionner.
        p1 (list): Liste d'entiers (valeurs du premier groupe, triées par ordre décroissant).
        p2 (list): Liste d'entiers (valeurs du second groupe, triées par ordre décroissant).

    Returns:
        int: La valeur maximale obtenue.
    """
    max_sum = 0
    # Parcourt toutes les répartitions possibles de sélection d'éléments
    for i in range(D + 1):
        try:
            # On prend i éléments du premier groupe et (D - i)//2 du deuxième
            sum1 = sum(p1[:i])
            sum2 = sum(p2[:(D - i) // 2])
            total = sum1 + sum2
            # Mise à jour du maximum
            if total > max_sum:
                max_sum = total
        except Exception:
            # Ignore les cas où l'affectation d'indices sort de la liste
            pass
    return max_sum

def main():
    """
    Fonction principale : lit les entrées, prépare les listes et calcule la somme maximale réalisable.
    """
    D, d1, d2 = read_input()
    # Extraction des valeurs après filtrage et tri pour chaque catégorie
    p1 = extract_sorted_values(d1, "D")
    p2 = extract_sorted_values(d2, "DD")
    # Calcul de la somme maximale
    ans = compute_max_sum(D, p1, p2)
    # Affichage du résultat
    print(ans)

# Appel du point d'entrée principal
if __name__ == "__main__":
    main()