def main():
    """
    Lit quatre entiers depuis l'entrée standard, calcule leur somme,
    puis affiche la somme en minutes et secondes.
    
    Plus précisément :
    - Chaque entier représente un nombre de secondes.
    - La somme totale des secondes est convertie en minutes et secondes.
    - Le nombre de minutes est affiché en premier.
    - Le nombre de secondes restantes (modulo 60) est affiché ensuite.
    """
    # Lire quatre entiers depuis l'entrée utilisateur et calculer leur somme totale en secondes
    total_seconds = sum(int(input()) for _ in range(4))
    
    # Calculer le nombre entier de minutes en divisant la somme totale par 60
    minutes = total_seconds // 60
    
    # Calculer le reste des secondes après extraction des minutes complètes
    seconds = total_seconds % 60
    
    # Afficher d'abord le nombre de minutes
    print(minutes)
    
    # Afficher ensuite le nombre de secondes restantes
    print(seconds)

if __name__ == "__main__":
    main()