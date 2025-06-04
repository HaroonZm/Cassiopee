from collections import Counter

def read_input():
    """
    Lit les valeurs d'entrée de l'utilisateur :
    - n : nombre de groupes d'items à traiter.
    - f : seuil de fréquence minimale pour filtrer les paires.
    Retourne n et f.
    """
    n, f = map(int, input().split())
    return n, f

def process_groups(n):
    """
    Traite chaque groupe d'items saisi par l'utilisateur.
    Pour chaque groupe, génère toutes les paires triées d'items possibles,
    et compte leur occurrence via un compteur Counter.
    
    Args:
        n (int): Nombre de groupes à lire.
    
    Returns:
        Counter: Un compteur du nombre d'occurrences de chaque paire d'items.
    """
    counter = Counter()
    for _ in range(n):
        # Lecture d'une ligne : le premier élément est le nombre d'items dans le groupe
        items = input().split()
        m = int(items[0])
        items = items[1:]  # Liste des items du groupe
        items.sort()       # Trie pour garantir l'ordre des paires
        # Pour chaque paire unique d'items (i, j) dans le groupe, on incrémente le compteur
        for i in range(m):
            for j in range(i + 1, m):
                counter[(items[i], items[j])] += 1
    return counter

def filter_and_sort_pairs(counter, f):
    """
    Filtre les paires d'items selon un seuil de fréquence,
    puis trie les résultats selon l'ordre alphabétique des paires.
    
    Args:
        counter (Counter): Compteur des paires d'items et leur fréquence.
        f (int): Fréquence minimale pour inclure une paire.
    
    Returns:
        list: Liste triée des paires d'items valides (filtrées par fréquence).
    """
    # Sélectionne les paires ayant une fréquence au moins égale à f, triées par fréquence descendante
    lst = [(k, v) for k, v in counter.most_common() if v >= f]
    lst.sort()  # Trie alphabétiquement par paire (tuple d'items)
    return lst

def main():
    """
    Fonction principale :
    - Lit l'entrée utilisateur (nombre de groupes et seuil de fréquence).
    - Compte les occurrences des paires d'items dans les groupes.
    - Filtre et trie les paires par fréquence et ordre alphabétique.
    - Affiche le nombre de paires valides et leur contenu.
    """
    n, f = read_input()
    counter = process_groups(n)
    lst = filter_and_sort_pairs(counter, f)
    print(len(lst))
    for k, v in lst:
        print(*k)

if __name__ == "__main__":
    main()