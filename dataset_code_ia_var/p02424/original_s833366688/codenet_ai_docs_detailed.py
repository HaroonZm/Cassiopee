def get_two_integers():
    """
    Demande à l'utilisateur de saisir deux entiers séparés par un espace,
    puis retourne ces deux entiers sous forme de tuple.
    
    Returns:
        tuple: Un tuple contenant deux entiers (a, b).
    """
    a, b = map(int, input("Entrez deux entiers séparés par un espace : ").split())
    return a, b

def apply_32bit_mask(value):
    """
    Applique un masque de 32 bits à la valeur entière fournie afin de ne garder
    que les 32 bits de poids faible. Ce masque force la valeur à rester dans les limites
    d'un entier non signé de 32 bits.
    
    Args:
        value (int): L'entier sur lequel appliquer le masque.
        
    Returns:
        int: L'entier tronqué à 32 bits.
    """
    mask_32 = 0b11111111111111111111111111111111  # Masque 32 bits (0xFFFFFFFF)
    return value & mask_32

def bitwise_operations_32bit(a, b):
    """
    Effectue des opérations bit à bit (ET, OU, XOR) sur deux entiers et applique un masque de 32 bits
    à chaque résultat pour garantir que seules les 32 positions de bits les plus basses sont conservées.
    
    Args:
        a (int): Premier entier.
        b (int): Deuxième entier.
        
    Returns:
        tuple: Un tuple contenant le résultat des opérations (AND, OR, XOR), chacun masqué à 32 bits.
    """
    c = apply_32bit_mask(a & b)      # ET bit à bit puis masque 32 bits
    d = apply_32bit_mask(a | b)      # OU bit à bit puis masque 32 bits
    e = apply_32bit_mask(a ^ b)      # XOR bit à bit puis masque 32 bits
    return c, d, e

def format_32bit_binary(value):
    """
    Formate un entier en une chaîne binaire de 32 bits (avec des zéros de tête si nécessaire).
    
    Args:
        value (int): L'entier à formater.
        
    Returns:
        str: Une chaîne représentant la valeur en binaire sur 32 bits.
    """
    return format(value, '032b')

def main():
    """
    Fonction principale qui orchestre la lecture de deux entiers, 
    effectue les opérations bit à bit, puis affiche chaque résultat au format binaire 32 bits.
    """
    # Lecture des entrées utilisateur
    a, b = get_two_integers()
    # Calcul des opérations bit à bit (ET, OU, XOR) avec masque de 32 bits
    and_result, or_result, xor_result = bitwise_operations_32bit(a, b)
    # Affichage des résultats formatés sur 32 bits en binaire
    print(format_32bit_binary(and_result))
    print(format_32bit_binary(or_result))
    print(format_32bit_binary(xor_result))

if __name__ == "__main__":
    main()