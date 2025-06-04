def recurrence_sequence(r, D, x_initial):
    """
    Calcule et affiche les 10 premières valeurs d'une suite définie par récurrence.
    
    La suite est définie comme suit :
        x_{n+1} = r * x_n - D
    où :
        - r (int) : le coefficient multiplicateur
        - D (int) : la valeur à soustraire à chaque itération
        - x_initial (int) : la valeur initiale x_0
        
    Les 10 premières valeurs calculées (x_1 à x_10) sont affichées à l'écran.
    
    Paramètres
    ----------
    r : int
        Le coefficient multiplicatif de la récurrence.
    D : int
        La constante soustraite à chaque itération.
    x_initial : int
        La valeur initiale de la suite (x_0).
    """
    # Initialisation de la variable x avec la valeur initiale x_0
    x = x_initial

    # Calcul et affichage des 10 premières valeurs de la suite
    for i in range(10):
        # Application de la relation de récurrence pour obtenir la nouvelle valeur de x
        x = r * x - D
        # Affichage de la valeur courante de x
        print(x)

def main():
    """
    Demande à l'utilisateur de saisir trois entiers séparés par des espaces (r, D, x_0),
    puis génère et affiche les 10 premières valeurs de la suite définie par la fonction recurrence_sequence().
    """
    # Demande à l'utilisateur de saisir les valeurs pour r, D et x_initial
    r, D, x_initial = map(int, input("Entrez r, D et x_0 séparés par des espaces : ").split())
    # Appelle la fonction qui traite la suite et affiche les résultats
    recurrence_sequence(r, D, x_initial)

# Appel du point d'entrée si le script est exécuté directement
if __name__ == "__main__":
    main()