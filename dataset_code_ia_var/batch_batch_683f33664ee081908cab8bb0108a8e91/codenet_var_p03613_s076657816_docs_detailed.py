def prepare_counter(size):
    """
    Crée et retourne une liste initialisée à 0 de longueur spécifiée.

    Args:
        size (int): La taille de la liste à créer.

    Returns:
        list: Une liste de zéros de longueur 'size'.
    """
    return [0] * size

def lire_entier():
    """
    Lit un entier depuis l'entrée standard.

    Returns:
        int: L'entier lu.
    """
    return int(input())

def lire_liste_entiers():
    """
    Lit une ligne d'entiers séparés par des espaces depuis l'entrée standard.

    Returns:
        list: Une liste d'entiers.
    """
    return [int(v) for v in input().split()]

def compter_occurrences_et_voisins(a, cnt):
    """
    Pour chaque valeur de la liste 'a', incrémente son compteur ainsi que celui
    de ses voisins (x-1 et x+1) dans la liste 'cnt'.

    Args:
        a (list): La liste des entiers à traiter.
        cnt (list): La liste des compteurs à mettre à jour.
    """
    for x in a:
        cnt[x] += 1                    # Incrémente le compteur de l'élément lui-même
        if x > 0:                      # Vérifie que x-1 reste dans la liste
            cnt[x-1] += 1              # Incrémente le compteur du voisin inférieur
        cnt[x+1] += 1                  # Incrémente le compteur du voisin supérieur

def trouver_valeur_max(cnt):
    """
    Trouve et retourne la valeur maximale dans la liste 'cnt'.

    Args:
        cnt (list): Liste de compteurs.

    Returns:
        int: La valeur maximale trouvée dans 'cnt'.
    """
    answer = 0
    for n in cnt:
        answer = max(answer, n)
    return answer

def main():
    """
    Point d'entrée du programme : lit les entrées, traite les données pour compter
    les occurrences et les voisins, puis affiche la réponse maximale trouvée.
    """
    # Taille suffisante pour couvrir tous les entiers possibles plus leurs voisins
    COUNTER_SIZE = 10**5 + 2

    # Initialisation du compteur de fréquences et voisins
    cnt = prepare_counter(COUNTER_SIZE)

    # Lecture des entrées
    n = lire_entier()                # Nombre d'éléments (non utilisé directement)
    a = lire_liste_entiers()         # Liste des entiers

    # Comptage des occurrences et de leurs voisins immédiats
    compter_occurrences_et_voisins(a, cnt)

    # Recherche de la fréquence maximale
    answer = trouver_valeur_max(cnt)

    # Affichage de la réponse
    print(answer)

if __name__ == "__main__":
    main()