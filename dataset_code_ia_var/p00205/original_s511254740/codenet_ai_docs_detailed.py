def get_inputs(num_inputs=5):
    """
    Demande à l'utilisateur d'entrer un certain nombre de valeurs.

    Args:
        num_inputs (int): Le nombre d'entrées à collecter auprès de l'utilisateur.

    Returns:
        list: Une liste contenant les valeurs saisies par l'utilisateur sous forme d'entiers.
    """
    return [int(input("Entrez un nombre: ")) for _ in range(num_inputs)]

def determine_w(input_set):
    """
    Détermine la valeur de 'w' selon la logique spécifiée :
    - Si 1 et 2 sont dans l'ensemble, retourne 1.
    - Sinon, si 1 et 3 sont dans l'ensemble, retourne 3.
    - Sinon, retourne 2.

    Args:
        input_set (set): Un ensemble d'entiers représentant les valeurs saisies.

    Returns:
        int: La valeur calculée pour 'w' selon la logique du problème.
    """
    if 1 in input_set and 2 in input_set:
        return 1
    elif 1 in input_set and 3 in input_set:
        return 3
    else:
        return 2

def process_inputs(inputs):
    """
    Traite la liste d'entrées selon la logique :
    - Si le nombre de valeurs distinctes n'est pas 2, imprime 3 pour chaque entrée.
    - Sinon, imprime 1 si la valeur correspond à 'w', sinon 2, pour chaque entrée.

    Args:
        inputs (list): Liste d'entiers saisis par l'utilisateur.
    """
    unique_values = set(inputs)
    w = determine_w(unique_values)
    if len(unique_values) != 2:
        for value in inputs:
            print(3)
    else:
        for value in inputs:
            print(1 if value == w else 2)

def main_loop():
    """
    Boucle principale du programme :
    - Continue de demander des entrées jusqu'à interception d'une exception (fin de flux ou erreur).
    - Pour chaque lot de 5 entrées, traite et affiche le résultat selon la logique décrite.
    """
    while True:
        try:
            # Récupère 5 entrées utilisateur
            user_inputs = get_inputs(5)
            # Traite et affiche le résultat pour ces entrées
            process_inputs(user_inputs)
        except Exception:
            # Termine la boucle en cas d'erreur (EOFError, interruption, etc.)
            break

if __name__ == "__main__":
    # Démarre la boucle principale seulement si ce fichier est exécuté comme programme principal
    main_loop()