def is_increasing_consecutive(s: str) -> bool:
    """
    Vérifie si la chaîne s représente une suite de chiffres strictement croissante
    et consécutive (chaque chiffre est exactement 1 plus que le précédent).
    Par exemple, "12345" -> True, "234" -> True, "34567" -> True
    mais "21" -> False, "334" -> False, "135" -> False, "89012" -> False.
    """
    if not s:
        return False
    # Vérifier pour chaque position si les chiffres sont consécutifs
    for i in range(len(s) - 1):
        current_digit = int(s[i])
        next_digit = int(s[i + 1])
        if next_digit != current_digit + 1:
            return False
    return True

def largest_matched_product(numbers):
    """
    Calcule le produit maximum de deux nombres distincts dans la liste numbers
    tel que le produit écrit en chaîne de caractères soit une séquence
    de chiffres consécutifs croissants.
    """
    max_product = -1
    n = len(numbers)
    # On teste toutes les paires possibles
    for i in range(n):
        for j in range(i + 1, n):
            a = numbers[i]
            b = numbers[j]
            product = a * b
            product_str = str(product)
            if is_increasing_consecutive(product_str):
                if product > max_product:
                    max_product = product
    return max_product

# Lecture de l'entrée
N = int(input())
numbers = list(map(int, input().split()))

# Calcul et affichage du résultat
result = largest_matched_product(numbers)
print(result)