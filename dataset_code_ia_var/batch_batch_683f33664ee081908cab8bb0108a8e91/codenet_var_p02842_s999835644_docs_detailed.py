def find_original_price_with_tax(n):
    """
    Cherche le nombre entier x tel que l'arrondi inférieur de x * 1.08 soit égal à n.
    
    Plus précisément, pour une taxe de 8% (équivalent à multiplier par 108 puis division entière par 100),
    cette fonction trouve le prix d'origine x si possible, sinon indique l'absence d'une telle valeur.
    
    Args:
        n (int): Le prix final après taxe (entier).
    
    Returns:
        int or str: Le prix initial x si trouvé, sinon ':('.
    """
    # Boucle sur toutes les valeurs possibles de x de 0 jusqu'à n inclus.
    for x in range(n + 1):
        # Vérifie si la partie entière de x multiplié par 108/100 donne n
        # Cela simule l'application de la taxe de 8% et son arrondi vers le bas.
        if x * 108 // 100 == n:
            # Si c'est le cas, retourne x comme prix initial.
            return x
    # Si aucune valeur de x ne satisfait la condition, retourne ':('.
    return ':('

def main():
    """
    Point d'entrée principal du programme.
    Lit une entrée utilisateur, cherche le prix initial avant taxe, puis affiche le résultat.
    """
    # Lecture de l'entrée utilisateur représentant le prix après taxe
    n = int(input())
    # Calcul du prix initial à partir du prix après taxe
    result = find_original_price_with_tax(n)
    # Affichage du résultat (prix initial ou ':(' si introuvable)
    print(result)

if __name__ == "__main__":
    main()