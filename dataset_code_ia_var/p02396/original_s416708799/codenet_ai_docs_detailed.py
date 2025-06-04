def main():
    """
    Exécute une boucle qui demande à l'utilisateur d'entrer des entiers jusqu'à ce que l'utilisateur saisisse 0
    ou que la limite de 10 000 entrées soit atteinte. Pour chaque entrée, le programme affiche l'index (Case)
    de la saisie et la valeur saisie. La boucle s'arrête immédiatement si 0 est saisi.
    """
    for i in range(10000):
        # Demander à l'utilisateur d'entrer un entier
        x = int(input())
        # Afficher le numéro de la case (1-indexé) et la valeur saisie
        print(f"Case {i+1}: {x}")
        # Si l'utilisateur saisit 0, arrêter la boucle immédiatement
        if x == 0:
            break

# Appelle la fonction principale si le script est exécuté directement
if __name__ == "__main__":
    main()