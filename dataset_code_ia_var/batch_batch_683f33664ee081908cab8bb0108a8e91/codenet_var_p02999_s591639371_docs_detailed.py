def compare_values():
    """
    Demande à l'utilisateur d'entrer deux entiers séparés par un espace,
    puis compare ces deux valeurs. Si le premier entier 'x' est inférieur
    au second entier 'a', affiche '0'. Sinon, affiche '10'.
    """
    # Demande une entrée à l'utilisateur et la convertit en deux entiers
    x, a = map(int, input("Entrez deux entiers séparés par un espace : ").split())

    # Si 'x' est strictement inférieur à 'a', affiche '0'
    if x < a:
        print("0")
    # Si 'x' est supérieur ou égal à 'a', affiche '10'
    elif x >= a:
        print("10")

# Appelle la fonction principale pour exécuter le programme
compare_values()