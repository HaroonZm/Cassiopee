def main():
    """
    Fonction principale qui lit deux chaînes de caractères de l'utilisateur,
    puis affiche leur concaténation dans l'ordre inversé (deuxième puis première).
    """
    # Lecture d'une ligne de l'entrée standard et séparation en deux chaînes distinctes
    S, T = input().split()
    
    # Concaténation des chaînes dans l'ordre T puis S et affichage du résultat
    print(T + S)

if __name__ == "__main__":
    main()