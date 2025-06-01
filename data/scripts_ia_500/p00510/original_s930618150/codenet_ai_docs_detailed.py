def main():
    """
    Lit des valeurs entières et calcule la valeur maximale atteinte par une variable lors d'une série d'ajustements.
    
    L'utilisateur saisit deux entiers n et m.
    Ensuite, pour chaque itération i allant de 0 à n-1, on lit deux entiers a et b.
    La variable m est mise à jour en ajoutant a et en soustrayant b.
    Si à un moment m devient négatif, le programme affiche 0 et s'arrête.
    Sinon, il affiche la valeur maximale atteinte par m durant le processus.
    """
    # Lire le nombre d'itérations
    n = int(input())
    # Lire la valeur initiale de m
    m = int(input())
    # Stocker la valeur maximale atteinte par m, initialement égale à m
    S_max = m

    # Boucle sur chaque paire d'entiers a, b pour mettre à jour m
    for i in range(n):
        a, b = map(int, input().split())
        # Mettre à jour m en ajoutant a et en soustrayant b
        m += a - b
        # Vérifier si m est devenu négatif
        if m < 0:
            # Si oui, afficher 0 et interrompre la boucle
            print(0)
            break
        # Mettre à jour la valeur maximale si le nouveau m est supérieur
        S_max = max(S_max, m)
    else:
        # Si la boucle s'est terminée sans interruption, afficher la valeur maximale atteinte
        print(S_max)

# Appel de la fonction principale pour exécuter le programme
main()