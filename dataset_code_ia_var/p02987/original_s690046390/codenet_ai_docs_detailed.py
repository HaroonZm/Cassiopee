import sys

def check_each_char_appears_twice(s):
    """
    Vérifie si chaque caractère de la chaîne donnée apparaît exactement deux fois.
    
    Arguments :
        s (str) : La chaîne de caractères à analyser.
        
    Retourne :
        bool : True si chaque caractère apparaît exactement deux fois, False sinon.
    """
    for char in s:
        # Compte le nombre d'occurrences du caractère courant dans la chaîne
        if s.count(char) != 2:
            # Si un caractère n'apparaît pas exactement deux fois, retourne False
            return False
    # Tous les caractères apparaissent exactement deux fois
    return True

def main():
    """
    Point d'entrée principal du programme.
    Lit une chaîne de caractères depuis l'entrée utilisateur et affiche "Yes"
    si chaque caractère apparaît exactement deux fois, "No" sinon.
    """
    # Lit la chaîne de caractères depuis l'entrée standard
    input_str = input()
    
    # Vérifie si chaque caractère apparaît exactement deux fois
    if check_each_char_appears_twice(input_str):
        print("Yes")
    else:
        print("No")
        # Termine le programme immédiatement avec un code de sortie différent de zéro
        sys.exit()

if __name__ == "__main__":
    main()