# Programme pour compter le nombre de chaînes palindromes dans des entrées multiples
# Chaque ligne contient une chaîne composée de caractères alphabétiques en demi-largeur
# Les chaînes peuvent contenir jusqu'à 100 caractères, et il y en a au plus 50
# Une chaîne de un seul caractère est considérée comme un palindrome

def is_palindrome(s):
    """
    Vérifie si une chaîne s est un palindrome.
    Un palindrome est identique lu de gauche à droite ou de droite à gauche.
    """
    return s == s[::-1]  # La chaîne inversée doit être identique à la chaîne originale

def main():
    count = 0  # Compteur pour le nombre de palindromes
    
    try:
        while True:
            line = input()
            if line == '':
                # Ligne vide, on arrête la lecture
                break
            
            # Vérification que la ligne est composée uniquement de demi-largeur alphabets
            # et que sa longueur est au plus 100
            if len(line) <= 100 and line.isascii() and line.isalpha():
                # Si la chaîne est palindrome, incrémenter le compteur
                if is_palindrome(line):
                    count += 1
            else:
                # Si la ligne ne respecte pas les contraintes, on peut choisir d'ignorer
                # ou sortir, ici on ignore simplement
                pass
    except EOFError:
        # Fin des entrées standard atteinte
        pass
    
    # Affichage du nombre de chaînes palindromes trouvées
    print(count)

if __name__ == "__main__":
    main()