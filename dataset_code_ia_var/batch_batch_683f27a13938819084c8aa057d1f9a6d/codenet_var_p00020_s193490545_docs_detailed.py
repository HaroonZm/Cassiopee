import sys

def to_uppercase(input_str):
    """
    Convertit toutes les lettres minuscules de l'alphabet latin dans la chaîne d'entrée en lettres majuscules.
    Les autres caractères ne sont pas modifiés.
    
    Paramètres:
        input_str (str): La chaîne de caractères à transformer.
    
    Retourne:
        str: Une nouvelle chaîne avec les lettres minuscules converties en majuscules.
    """
    # Définir les chaînes pour les minuscules et majuscules latin standard
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Créer la table de traduction pour str.translate : chaque minuscule mappe sur la majuscule correspondante
    translation_table = str.maketrans(lowercase, uppercase)
    
    # Transformer la chaîne d'entrée à l'aide de la table de traduction
    return input_str.translate(translation_table)

def main():
    """
    Lit les lignes de l'entrée standard, convertit les lettres minuscules en majuscules et affiche le résultat.
    Supprime le caractère de saut de ligne à la fin de chaque ligne lue.
    """
    for line in sys.stdin:
        # Enlever le caractère de saut de ligne final (s'il existe)
        stripped_line = line.rstrip('\n')
        
        # Convertir la ligne en majuscules selon le mapping a-z -> A-Z
        result = to_uppercase(stripped_line)
        
        # Afficher la ligne convertie
        print(result)

if __name__ == "__main__":
    main()