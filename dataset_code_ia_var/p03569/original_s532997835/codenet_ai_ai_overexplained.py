"""
@author: H_Hoshigi
"""

def main():
    # Lire une chaîne de caractères depuis l'entrée utilisateur.
    # input() lit une ligne de l'entrée standard et retourne une chaîne de caractères.
    S = input()

    # Initialiser un pointeur 'r' (pour right, à gauche du texte) à la position 0 (début de la chaîne).
    r = 0

    # Initialiser un pointeur 'l' (pour left, à droite du texte) à la position de l'avant-dernier caractère.
    # len(S) donne la longueur de la chaîne S (nombre de caractères dans S).
    # On retire 1 car l'indexation commence à 0, donc l'index maximal est len(S)-1.
    l = len(S) - 1

    # Initialiser un compteur à 0. Ce compteur servira à compter certaines opérations (ajouts de 'x').
    counter = 0

    # Tant que la différence entre les index 'l' et 'r' est supérieur ou égale à 1, poursuivre la boucle.
    # Cela signifie que nous n'avons pas encore traversé ou rencontré le centre du mot.
    while (l - r) >= 1:
        # Si le caractère au début (à la position 'r') et à la fin (à la position 'l') sont identiques.
        if S[r] == S[l]:
            # On "rapproche" les pointeurs, c'est-à-dire qu'on avance 'r' d'une position vers la droite,
            # et 'l' d'une position vers la gauche pour comparer les caractères suivants.
            r += 1    # Ajouter 1 à r (passer au caractère suivant depuis la gauche).
            l -= 1    # Soustraire 1 à l (passer au caractère précédent depuis la droite).
        # Sinon, si le caractère du côté gauche ('r') est un 'x' (caractère spécifique à traiter) :
        elif S[r] == "x":
            # Dans ce cas, nous considérons qu'il faut "compenser" par un ajout de 'x' du côté opposé pour former un palindrome.
            r += 1        # Avancer le pointeur gauche.
            counter += 1  # Compter une opération de modification.
        # Sinon, si le caractère côté droit ('l') est un 'x' :
        elif S[l] == "x":
            # On applique la même logique mais de l'autre côté.
            l -= 1        # Réduire le pointeur droit (vers la gauche).
            counter += 1  # Compter l'opération.
        # Enfin, si aucun des cas ci-dessus n'est applicable, cela veut dire que les caractères comparés sont différents et ne sont pas 'x'.
        else:
            # Il n'est pas possible de former un palindrome en n'ajoutant que des 'x'.
            counter = -1  # On utilise -1 comme valeur spécifique pour indiquer l'échec.
            break         # Sortir immédiatement de la boucle, car ce n'est plus possible.

    # Afficher le résultat final du compteur sur la sortie standard.
    # Si counter vaut -1, cela signifie qu'il était impossible de former le palindrome souhaité.
    # Sinon, on affiche le nombre minimal d'opérations (insertions de 'x') nécessaires.
    print(counter)

# Ce bloc conditionnel vérifie si le script est exécuté comme programme principal
# et non importé en tant que module dans un autre code Python.
if __name__ == "__main__":
    # Appeler la fonction main pour démarrer le programme.
    main()