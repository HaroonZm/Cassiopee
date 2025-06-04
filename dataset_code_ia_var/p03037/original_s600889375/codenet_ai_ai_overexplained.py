def main():
    # Demande à l'utilisateur de saisir une seule ligne contenant deux entiers séparés par un espace
    # La fonction input() lit cette ligne depuis l'entrée standard (le clavier)
    # split() sépare la ligne en morceaux à chaque espace et retourne une liste de chaînes de caractères
    # map(int, ...) applique la fonction int à chaque élément de la liste ce qui convertit chaque chaîne de caractères en un nombre entier
    # Enfin, l'expression affecte ces deux entiers aux variables n et m
    n, m = map(int, input().split())

    # Initialise la variable left à 1
    # Cette variable représentera la borne gauche actuelle de l'intervalle d'intérêt, initialement le plus petit possible (1)
    left = 1

    # Initialise la variable right à n
    # Cette variable représentera la borne droite actuelle de l'intervalle d'intérêt, initialement le plus grand possible (n)
    right = n

    # Démarre une boucle qui s'exécutera exactement m fois
    # L'underscore '_' est une convention pour indiquer que nous n'utilisons pas la variable de boucle
    for _ in range(m):
        # À chaque itération, demande à l'utilisateur de saisir une ligne avec deux entiers séparés par un espace
        # Ces deux entiers sont left_i et right_i, représentant une contrainte sur la plage possible
        left_i, right_i = map(int, input().split())

        # Met à jour la valeur de left pour qu'elle soit la plus à droite possible entre sa valeur actuelle et left_i
        # max() retourne le plus grand des deux arguments
        # Ceci garantit que left représente la limite la plus restrictive à gauche imposée jusqu'à présent
        left = max(left, left_i)

        # Met à jour la valeur de right pour qu'elle soit la plus à gauche possible entre sa valeur actuelle et right_i
        # min() retourne le plus petit des deux arguments
        # Ceci garantit que right représente la limite la plus restrictive à droite imposée jusqu'à présent
        right = min(right, right_i)
    
    # Calcule la longueur de la plage valide résultante en soustrayant left à right puis en ajoutant 1
    # Cela correspond au nombre d'entiers sur l'intervalle fermé [left, right]
    # Si right < left, alors il n'y a aucun entier valide, donc on utilise max(0, ...) pour éviter une valeur négative
    result = max(0, right - left + 1)

    # Affiche le résultat à l'utilisateur
    print(result)

# Appelle la fonction principale main() pour démarrer l'exécution du programme
main()