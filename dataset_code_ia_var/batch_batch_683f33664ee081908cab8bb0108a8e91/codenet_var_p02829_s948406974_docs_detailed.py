def main():
    """
    Lit deux entiers depuis l'entrée utilisateur, puis imprime l'entier manquant 
    parmi 1, 2 et 3 sachant que les deux entiers saisis sont distincts dans l'intervalle [1, 3].

    Si les valeurs sont (a=1, b=2), la sortie est 3.
    Si les valeurs sont (a=1, b=3), la sortie est 2.
    Si les valeurs sont (a=2, b=3), la sortie est 1.
    Et inversement selon l'ordre des entrées.
    """
    # Lire le premier entier depuis l'entrée utilisateur
    a = int(input("Entrez le premier entier (1, 2 ou 3) : "))
    # Lire le second entier depuis l'entrée utilisateur
    b = int(input("Entrez le second entier (1, 2 ou 3, et différent du premier) : "))

    # Vérifier le couple d'entrées et afficher la valeur manquante parmi {1, 2, 3}
    if a == 1 and b == 2:
        print('3')
    elif a == 1 and b == 3:
        print('2')
    elif a == 2 and b == 3:
        print('1')
    elif a == 2 and b == 1:
        print('3')
    elif a == 3 and b == 1:
        print('2')
    elif a == 3 and b == 2:
        print('1')

# Exécuter la fonction principale si ce fichier est exécuté comme script principal
if __name__ == "__main__":
    main()