def main():
    """
    Fonction principale exécutant la lecture de deux chaînes à partir de l'entrée utilisateur,
    puis affichant leur concaténation dans l'ordre inverse par rapport à l'entrée.
    """
    # Lecture de deux chaînes de caractères à l'aide de l'entrée standard, séparées par des espaces.
    T, S = map(str, input().split())
    
    # Concaténation de S suivi de T, puis affichage du résultat.
    print(S + T)

if __name__ == "__main__":
    main()