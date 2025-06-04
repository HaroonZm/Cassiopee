def transform_string(input_str):
    """
    Transforme la chaîne selon les règles suivantes :
    - Remplace tous les caractères '1' par des espaces temporaires,
    - Remplace tous les caractères '9' par des '1',
    - Remplace ensuite les espaces temporaires par des '9'.
    
    Args:
        input_str (str): La chaîne de caractères à transformer.
    
    Returns:
        str: La chaîne transformée selon les règles ci-dessus.
    """
    # Étape 1 : remplacer tous les '1' par des espaces. 
    # Les espaces servent de repère temporaire pour ne pas interférer avec le remplacement suivant.
    temp_str = input_str.replace('1', ' ')
    
    # Étape 2 : remplacer tous les '9' par des '1'.
    # À ce stade, les anciens '1' ont été mis de côté en tant qu'espaces,
    # cela permet de remplacer sans ambiguïté.
    temp_str = temp_str.replace('9', '1')
    
    # Étape 3 : remplacer tous les espaces (anciens '1') par des '9'.
    result_str = temp_str.replace(' ', '9')
    
    return result_str

def main():
    """
    Point d'entrée principal du programme.
    Lit une chaîne depuis l'entrée standard, applique la transformation, puis affiche le résultat.
    """
    # Lire la chaîne d'entrée de l'utilisateur.
    user_input = input()
    
    # Appliquer la transformation sur la chaîne saisie.
    transformed = transform_string(user_input)
    
    # Afficher la chaîne transformée.
    print(transformed)

# Exécute la fonction principale lorsque ce script est lancé
if __name__ == "__main__":
    main()