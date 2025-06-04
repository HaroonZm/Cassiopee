def calculate1():
    """
    Calcule la différence entre B et A, puis décompose ce montant en billets de 1000, 500 et 100.
    Appelle les fonctions appropriées pour continuer la décomposition selon le reste après chaque étape.
    """
    change = B - A  # Calcule la différence à rendre
    if change % 1000 == 0:
        # Si la différence est multiple de 1000, on utilise uniquement des billets de 1000
        one_thousand_count = change // 1000
        print_result(one_thousand_count)
    else:
        # Sinon, on calcule le nombre de billets de 1000 et le reste
        one_thousand_count = change // 1000
        remainder = change - one_thousand_count * 1000
        calculate2(remainder, one_thousand_count)

def calculate2(remainder, one_thousand_count):
    """
    Décompose le reste en utilisant des billets de 500 si possible.
    Si le reste n'est pas un multiple de 500, passe à la décomposition en billets de 100.
    
    Args:
        remainder (int): le montant restant après extraction des billets de 1000.
        one_thousand_count (int): nombre de billets de 1000 utilisés.
    """
    if remainder % 500 == 0:
        # Si le reste est multiple de 500, on utilise uniquement des billets de 500 pour ce qui reste
        five_hundred_count = remainder // 500
        print_result(one_thousand_count, five_hundred_count)
    else:
        # Sinon, on calcule le nombre de billets de 500 et le reste
        five_hundred_count = remainder // 500
        remainder = remainder - five_hundred_count * 500
        calculate3(remainder, one_thousand_count, five_hundred_count)

def calculate3(remainder, one_thousand_count, five_hundred_count):
    """
    Décompose le reste en billets de 100 uniquement.
    
    Args:
        remainder (int): le montant restant après extraction des billets de 1000 et 500.
        one_thousand_count (int): nombre de billets de 1000 utilisés.
        five_hundred_count (int): nombre de billets de 500 utilisés.
    """
    one_hundred_count = remainder // 100  # Compte le nombre de billets de 100 à utiliser
    print_result(one_thousand_count, five_hundred_count, one_hundred_count)

def print_result(one_thousand_count=0, five_hundred_count=0, one_hundred_count=0):
    """
    Affiche le nombre de billets de 100, 500 et 1000 utilisés dans l'ordre spécifié.
    
    Args:
        one_thousand_count (int, optional): nombre de billets de 1000. Défaut à 0.
        five_hundred_count (int, optional): nombre de billets de 500. Défaut à 0.
        one_hundred_count (int, optional): nombre de billets de 100. Défaut à 0.
    """
    print('%d %d %d' % (one_hundred_count, five_hundred_count, one_thousand_count))

# Boucle principale pour traiter les entrées utilisateur
while True:
    # Lit deux entiers A et B. Arrête la boucle si les deux sont zéro.
    try:
        A, B = map(int, input().split())
    except EOFError:
        break  # Arrête proprement à la fin de l'entrée (utile lorsque les entrées ne sont pas interactives)
    if A == 0 and B == 0:
        break
    calculate1()