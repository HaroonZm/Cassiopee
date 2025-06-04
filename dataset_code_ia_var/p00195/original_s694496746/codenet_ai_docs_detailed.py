import sys
import operator

def read_input(file_handle):
    """
    Lit une ligne depuis le flux donné et retourne une liste d'entiers.
    
    Args:
        file_handle: Objet représentant le flux d'entrée à lire (ex: sys.stdin).
        
    Returns:
        list: Liste d'entiers extraits de la ligne lue.
    """
    return list(map(int, file_handle.readline().split()))

def main():
    """
    Fonction principale qui lit les scores de cinq groupes, puis affiche
    la lettre représentant le groupe ayant le score total le plus élevé
    ainsi que son score. Le programme s'arrête lorsque la première ligne lue
    contient uniquement des zéros.
    
    La correspondance entre les lettres et les groupes est la suivante:
    'A', 'B', 'C', 'D', 'E'
    """
    f = sys.stdin  # Utilisation du flux d'entrée standard
    while True:
        # Lecture et sommation de la première ligne de scores
        a = sum(read_input(f))
        # Condition d'arrêt (si la somme est nulle)
        if a == 0:
            break
        # Lecture et sommation des scores pour les quatre autres groupes
        abcde = [a] + [sum(read_input(f)) for _ in range(4)]
        # Création de couples (lettre, score) pour chaque groupe
        groups = list(zip('ABCDE', abcde))
        # Recherche du groupe avec le score maximal
        winner = max(groups, key=operator.itemgetter(1))
        # Affichage du résultat
        print(*winner)

if __name__ == "__main__":
    main()