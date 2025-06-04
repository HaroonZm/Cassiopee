def main():
    """
    Fonction principale qui lit des paires de nombres entiers depuis l'entrée standard,
    puis pour chaque paire (a, b) où a != 0 ou b != 0, calcule la différence c = b - a.
    La fonction décompose ensuite c en billets de 1000, 500, et 100 selon un système glouton.
    Le programme s'arrête lorsque la paire (0, 0) est saisie.
    """
    while True:
        # Lecture de deux entiers séparés par un espace depuis l'entrée standard
        a, b = map(int, raw_input().split())
        
        # Condition d'arrêt : si les deux valeurs saisies sont 0, on sort de la boucle
        if a == 0 and b == 0:
            break
        
        # Calcul de la différence entre b et a
        c = b - a
        
        # Initialisation des compteurs pour les billets de 1000, 500 et 100
        ans_1000 = 0  # Compte de billets de 1000
        ans_500 = 0   # Compte de billets de 500
        ans_100 = 0   # Compte de billets de 100
        
        # Comptage des billets de 1000 nécessaires
        while c >= 1000:
            c -= 1000
            ans_1000 += 1
        
        # Comptage des billets de 500 nécessaires
        while c >= 500:
            c -= 500
            ans_500 += 1
        
        # Comptage des billets de 100 nécessaires
        while c >= 100:
            c -= 100
            ans_100 += 1
        
        # Affichage du résultat : nombre de billets de 100, 500, puis 1000
        print ans_100, ans_500, ans_1000

# Appel de la fonction principale lorsque le script est exécuté
if __name__ == "__main__":
    main()