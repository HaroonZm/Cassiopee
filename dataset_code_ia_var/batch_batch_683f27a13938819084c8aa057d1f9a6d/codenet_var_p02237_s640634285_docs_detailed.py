def process_input_line(n, input_line):
    """
    Traite une seule ligne d'entrée, en retournant une liste de longueur n indiquant
    la présence (1) ou l'absence (0) d'indices spécifiés dans la ligne.

    Args:
        n (int): La taille de la liste à générer.
        input_line (str): Une chaîne contenant des entiers séparés par des espaces. 
                          La ligne commence par deux entiers (u, k) ignorés dans la logique,
                          suivis par des entiers représentant des indices à marquer comme 1 dans la liste.

    Returns:
        list: Une liste de longueur n composée de 0 et 1, où chaque 1 indique la présence d'un indice donné.
    """
    # Conversion de la ligne d'entrée en liste d'entiers
    values = list(map(int, input_line.split()))
    # Les deux premiers champs sont 'u' et 'k', qui ne sont pas utilisés pour la logique suivante
    u = values[0]
    k = values[1]
    v = values[2:]  # Les indices à considérer

    # Création de la liste de sortie initialisée à 0
    a = [0] * n
    # Pour chaque indice reçu dans v, on met la valeur correspondante de 'a' à 1
    for i_v in v:
        index_v = i_v - 1  # Passage en indexation Python (début à 0)
        if 0 <= index_v < n:
            a[index_v] = 1
    return a

def main():
    """
    Fonction principale du programme :
    - Lit le nombre de lignes à traiter depuis l'entrée standard.
    - Pour chaque ligne, lit les données, les traite, et affiche le résultat.
    """
    # Lecture du nombre de lignes/instances à traiter
    n = int(input())
    # Pour chaque ligne à traiter
    for _ in range(n):
        # Lecture d'une ligne de données
        input_line = input()
        # Traitement de la ligne pour obtenir le tableau binaire correspondant
        a = process_input_line(n, input_line)
        # Affichage du résultat, avec un espace entre chaque valeur
        print(*a)

if __name__ == '__main__':
    main()