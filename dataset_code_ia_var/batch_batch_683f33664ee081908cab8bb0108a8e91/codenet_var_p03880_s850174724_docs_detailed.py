def get_input_numbers():
    """
    Lit un entier n depuis l'entrée standard, puis lit n entiers ligne par ligne.
    
    Returns:
        tuple: (n, a) où n est le nombre d'éléments, et a la liste d'entiers.
    """
    n = int(raw_input())  # Nombre d'entiers
    a = [int(raw_input()) for _ in xrange(n)]  # Liste des n entiers
    return n, a

def compute_max_binary_length(a):
    """
    Calcule la longueur maximale de la représentation binaire des éléments de la liste 'a'.
    
    Args:
        a (list of int): Liste des entiers.
    
    Returns:
        int: La longueur maximale rencontrée.
    """
    mxlba = 0
    for value in a:
        binary_length = len(bin(value)[2:])  # Exclure le préfixe '0b'
        mxlba = max(mxlba, binary_length)
    return mxlba

def build_bit_existence_array(a, mxlba):
    """
    Construit un tableau booléen indiquant pour chaque position de bit
    si un des éléments de la liste 'a' a son bit de poids fort à '1' à cette position.
    
    Args:
        a (list of int): Liste des entiers
        mxlba (int): Longueur binaire maximale des entiers de a.
    
    Returns:
        list of bool: Tableau où exist[i] est True si un entier de a a son premier '1' en position i.
    """
    exist = [False] * (mxlba + 1000)  # Taille généreuse pour éviter tout dépassement
    for value in a:
        bit_str = bin(value)[2:]
        length = len(bit_str)
        # Cherche le bit le plus significatif à '1'
        for j in xrange(length - 1, -1, -1):
            if bit_str[j] == "1":
                exist[length - 1 - j] = True  # Position du bit de poids fort rencontré
                break
    return exist

def compute_xor(a):
    """
    Calcule le OU exclusif (XOR) de tous les éléments de la liste 'a'.
    
    Args:
        a (list of int): Liste des entiers
    
    Returns:
        int: Le résultat du XOR.
    """
    axor = 0
    for value in a:
        axor ^= value
    return axor

def min_operations_to_reduce_xor(axor, exist):
    """
    Calcule le nombre minimal d'opérations nécessaires pour réduire un nombre XOR donné à zéro,
    en se basant sur la présence des bits de poids fort dans 'exist'.
    Si ce n'est pas possible, retourne -1.
    
    Args:
        axor (int): Le nombre à réduire.
        exist (list of bool): Présence des bits de poids fort dans les entiers initiaux.
    
    Returns:
        int: Le nombre minimal d'opérations, 0 si pas de XOR initial, -1 si impossible.
    """
    if axor == 0:
        # Rien à faire si XOR total nul, sortie immédiate
        return 0
    
    axor_bin = bin(axor)[2:]         # Représentation binaire du XOR
    la = len(axor_bin)               # Longueur de la chaîne binaire
    ans = 0                          # Compteur d'opérations
    i = 0
    while i < la:
        if axor_bin[i] == "1":
            bit_position = la - i - 1
            if not exist[bit_position]:
                # Impossible car il n'existe aucun nombre initial avec un '1' à cette position
                return -1
            else:
                # On peut éliminer ce bit : simuler une opération qui enlève tout les '1' jusqu'à cette position
                ans += 1
                if bit_position == 0:
                    break
                # Crée un masque de '1' de la taille bit_position
                tmp = int("1" * bit_position, 2)
                # Applique le XOR pour éliminer les bits
                axor = int(axor_bin, 2) ^ tmp
                axor_bin = bin(axor)[2:]
        i += 1
    return ans

def main():
    """
    Fonction principale : lit les entrées,
    puis calcule et affiche le nombre minimal d'opérations nécessaires,
    ou -1 si c'est impossible.
    """
    n, a = get_input_numbers()
    mxlba = compute_max_binary_length(a)
    exist = build_bit_existence_array(a, mxlba)
    axor = compute_xor(a)
    result = min_operations_to_reduce_xor(axor, exist)
    print(result)

if __name__ == "__main__":
    main()