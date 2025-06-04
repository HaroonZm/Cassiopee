def calc_prize(input_str):
    """
    Calcule le montant du prix basé sur les caractères 'o' dans la chaîne donnée.
    
    Chaque 'o' ajoute 100 au montant de base de 700.
    
    Args:
        input_str (str): Chaîne de caractères à évaluer.
        
    Returns:
        int: Montant total calculé.
    """
    # Compte le nombre de fois que 'o' apparaît dans la chaîne
    num_o = input_str.count('o')
    
    # Calcule le prix total en ajoutant 100 pour chaque 'o' au montant de base de 700
    total = 700 + 100 * num_o
    return total

if __name__ == "__main__":
    # Lecture de la chaîne d'entrée de l'utilisateur
    S = input()
    # Calcul du montant du prix en fonction de l'entrée
    ans = calc_prize(S)
    # Affichage du montant calculé
    print(ans)