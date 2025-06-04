def format_binary_string(number, length=11):
    """
    Retourne la représentation binaire d'un entier 'number' sur 'length' caractères, 
    complétée avec des zéros à gauche si nécessaire.

    Args:
        number (int): L'entier à convertir en binaire.
        length (int, optional): La longueur désirée de la chaîne binaire. Par défaut à 11.

    Returns:
        str: Chaîne binaire du nombre, sous forme de 'length' caractères.
    """
    binary_str = bin(number)[2:]           # Enlever le préfixe '0b'
    padded_binary_str = '0' * (length - len(binary_str)) + binary_str
    return padded_binary_str

def compute_differences(n):
    """
    Pour chaque nombre i de 0 à n-1, calcule les positions de la première différence binaire
    (sur les 9 bits de poids fort) entre i et tous les j > i jusqu'à n-1, et affiche 
    les résultats.

    Args:
        n (int): Nombre d'itérations et borne supérieure pour i et j (exclue).
    """
    for i in range(n):
        differences = []  # Liste pour stocker les positions trouvées pour cet i
        I = format_binary_string(i)  # Binaire sur 11 bits de i
        for j in range(i + 1, n):    # Pour chaque j > i
            J = format_binary_string(j)  # Binaire sur 11 bits de j
            # On cherche la première position (des 9 premiers bits) où les chaînes diffèrent
            for k in range(9):
                if I[k] != J[k]:
                    differences.append(9 - k)  # On note la position en partant du 9 (de poids fort)
                    break                      # On arrête dès la première différence trouvée
        # On affiche les positions séparées par des espaces (chaîne vide si aucune)
        print(' '.join(map(str, differences)))

def main():
    """
    Fonction principale. Lit un entier depuis l'entrée standard, puis
    affiche les résultats des positions de premières différences binaires pour chaque i.
    """
    n = int(input())
    compute_differences(n)

# Appel du point d'entrée du script
if __name__ == "__main__":
    main()