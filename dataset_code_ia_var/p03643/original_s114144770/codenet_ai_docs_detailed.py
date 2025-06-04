def main():
    """
    Fonction principale qui lit une entrée utilisateur et affiche le préfixe 'ABC' suivi de l'entrée.
    """
    # Lecture de la saisie utilisateur (une chaîne de caractères, généralement un nombre).
    N = input()
    # Affichage du résultat en concaténant le préfixe 'ABC' avec la saisie utilisateur.
    print("ABC" + N)

# Appelle la fonction principale si ce fichier est exécuté directement.
if __name__ == "__main__":
    main()