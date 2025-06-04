def get_prices(n):
    """
    Demande à l'utilisateur d'entrer n prix, un par un, puis retourne la liste de ces prix.
    
    Args:
        n (int): Le nombre total de prix à saisir.
        
    Returns:
        list: Une liste d'entiers représentant les prix saisis.
    """
    prices = []  # Liste vide pour stocker les prix entrés par l'utilisateur
    for _ in range(n):
        price = int(input())  # Lit un prix depuis l'entrée standard et le convertit en entier
        prices.append(price)  # Ajoute le prix à la liste
    return prices

def compute_integer_average(prices):
    """
    Calcule la moyenne entière d'une liste de prix.
    
    Args:
        prices (list): Liste d'entiers représentant les prix.
        
    Returns:
        int: La moyenne arithmétique entière des prix.
    """
    # On utilise la division entière pour obtenir la partie entière de la moyenne
    return int(sum(prices) / len(prices))

def main():
    """
    Fonction principale : lit le nombre de prix à saisir, demande les prix, puis affiche la moyenne entière.
    """
    n = int(input())  # Demande à l'utilisateur le nombre de prix à saisir
    prices = get_prices(n)  # Récupère les prix saisis côté utilisateur
    ans = compute_integer_average(prices)  # Calcule la moyenne entière des prix
    print(ans)  # Affiche la moyenne calculée

if __name__ == "__main__":
    main()