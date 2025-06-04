def get_user_inputs(num_inputs):
    """
    Demande à l'utilisateur de saisir un nombre donné d'entiers.
    
    Args:
        num_inputs (int): Le nombre de valeurs à demander à l'utilisateur.
    
    Returns:
        list: Une liste des entiers saisis par l'utilisateur.
    """
    # Crée une liste vide pour stocker les entrées de l'utilisateur
    inputs = []
    for i in range(num_inputs):
        # Demande à l'utilisateur de saisir un entier et l'ajoute à la liste
        value = int(input(f"Entrez un entier ({i+1}/{num_inputs}) : "))
        inputs.append(value)
    return inputs

def find_unique_element(full_list, exclude_list):
    """
    Trouve l'élément unique dans full_list qui n'est pas présent dans exclude_list.
    
    Args:
        full_list (list): La liste complète des éléments possibles.
        exclude_list (list): La liste des éléments à exclure.
    
    Returns:
        L'élément unique restant dans full_list après exclusion.
        Si plusieurs éléments restent, retourne le premier.
    """
    # Convertit les listes en ensembles pour faciliter la différence d'ensemble
    remaining_elements = set(full_list) - set(exclude_list)
    # Transforme l'ensemble résultant en liste et retourne son premier élément
    return list(remaining_elements)[0]

def main():
    """
    Exécute le flux principal du programme :
    - Lit deux entiers en entrée,
    - Trouve et affiche l'unique valeur manquante dans [1,2,3].
    """
    # Liste complète de référence
    ans_list = [1, 2, 3]
    # Demande à l'utilisateur de saisir deux entiers
    ab = get_user_inputs(2)
    # Trouve la valeur manquante et l'affiche
    result = find_unique_element(ans_list, ab)
    print(result)

# Exécution du programme principal
if __name__ == "__main__":
    main()