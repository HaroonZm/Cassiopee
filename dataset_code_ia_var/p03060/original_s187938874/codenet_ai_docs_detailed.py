def read_integer_list(prompt):
    """
    Lit une ligne d'entrées séparées par des espaces et retourne une liste d'entiers.
    
    Args:
        prompt (str): Le message à afficher pour demander l'entrée utilisateur.
        
    Returns:
        list of int: Une liste d'entiers extraite de l'entrée utilisateur.
    """
    return list(map(int, input(prompt).split()))

def calculate_max_profit(values, costs):
    """
    Calcule le profit maximal pouvant être obtenu, en choisissant les éléments 
    ayant un profit positif (profit = value - cost).
    
    Args:
        values (list of int): La liste des valeurs pour chaque article.
        costs (list of int): La liste des coûts pour chaque article.
        
    Returns:
        int: La somme maximale des profits positifs triés par ordre décroissant.
    """
    # Calculer le profit pour chaque élément
    profit_list = []
    for i in range(len(values)):
        profit = values[i] - costs[i]
        profit_list.append(profit)
    
    # Trier la liste des profits en ordre décroissant pour d'abord traiter les plus grands profits
    profit_list.sort(reverse=True)
    
    # Cumuler les profits tant qu'ils sont strictement positifs
    max_profit = 0
    for profit in profit_list:
        if profit <= 0:
            # Arrêter le cumul si on atteint un profit nul ou négatif
            break
        max_profit += profit
    
    return max_profit

def main():
    """
    Point d'entrée principal du script.
    Lit les entrées utilisateur, calcule et affiche le profit maximal possible.
    """
    # Lire le nombre d'éléments à traiter
    N = int(input())
    
    # Lire la liste des valeurs associées aux éléments
    value_lst = read_integer_list('')
    
    # Lire la liste des coûts associés aux éléments
    cost_lst = read_integer_list('')
    
    # Calculer et afficher le profit maximal possible
    plofit_max = calculate_max_profit(value_lst, cost_lst)
    print(plofit_max)

# Exécuter le script principal si ce fichier est exécuté directement
if __name__ == "__main__":
    main()