def count_below_or_equal_average(n, values):
    """
    Compte le nombre d'éléments dans la liste 'values' qui sont inférieurs ou égaux à la moyenne arithmétique.

    Paramètres :
        n (int) : Nombre d'éléments dans la liste.
        values (list of int) : Liste contenant les valeurs à traiter.

    Retourne :
        int : Le nombre d'éléments inférieurs ou égaux à la moyenne.
    """
    # Calcul de la somme totale des valeurs
    total = 0
    for value in values:
        total += int(value)
    # Calcul de la moyenne (attention à la division, n doit être non nul)
    average = total / n
    # Compte le nombre d'éléments inférieurs ou égaux à la moyenne
    count = 0
    for value in values:
        if int(value) <= average:
            count += 1
    return count

def main():
    """
    Fonction principale qui lit les entrées utilisateur et affiche le résultat pour chaque série d'entiers.
    Le programme s'arrête lorsque l'utilisateur saisit 0.
    """
    while True:
        # Lecture du nombre d'éléments (arrêt si n == 0)
        n = int(input())
        if n == 0:
            break
        # Lecture des valeurs, séparées par des espaces
        a = input().split()
        # Calcul et affichage du résultat
        result = count_below_or_equal_average(n, a)
        print(result)

# Lancement du programme principal
if __name__ == "__main__":
    main()