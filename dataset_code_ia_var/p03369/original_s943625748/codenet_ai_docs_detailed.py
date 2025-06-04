def calculate_total_score(s):
    """
    Calcule le score total selon le nombre de caractères 'o' dans la chaîne d'entrée.
    
    Le calcul consiste à ajouter 100 points pour chaque 'o' présent dans la chaîne à une base de 700 points.
    
    Args:
        s (str): La chaîne de caractères à analyser.
    
    Returns:
        int: Le score total calculé.
    """
    # Compter le nombre d'occurrences du caractère 'o' dans la chaîne d'entrée
    number_of_o = s.count('o')
    # Calculer le score total selon la formule spécifiée
    total_score = 700 + number_of_o * 100
    return total_score

def main():
    """
    Fonction principale qui lit l'entrée utilisateur, calcule le score et l'affiche.
    """
    # Lire une ligne depuis l'entrée standard (utilisateur)
    user_input = input()
    # Calculer le score total en utilisant la fonction dédiée
    result = calculate_total_score(user_input)
    # Afficher le score résultant
    print(result)

if __name__ == "__main__":
    # Lancer la fonction principale uniquement si le script est exécuté directement
    main()