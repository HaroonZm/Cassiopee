def compute_sequence_sum(n):
    """
    Calcule une valeur en fonction de n en suivant une séquence définie :
    - Si n == 1, retourne 1.
    - Sinon, construit une liste A de taille n // 2 où :
        A[0] = 1
        A[i] = 1 + 2 * somme des A jusqu'à i-1 pour i >= 1
      La réponse finale est sum(A) * 2 (+ 1 + 2*sum(A) si n est impair).
      
    Args:
        n (int): Le nombre entier pour lequel calculer la somme.

    Returns:
        int: Le résultat du calcul défini par l'algorithme.
    """
    if n == 1:
        # Cas particulier où n vaut 1, la réponse est simplement 1
        return 1
    else:
        # Création d'une liste A initialisée à 0, de longueur n // 2
        A = [0 for _ in range(n // 2)]
        # Initialisation du premier élément à 1
        A[0] = 1
        # Remplissage de la liste A selon la formule spécifiée
        for i in range(1, n // 2):
            # A[i] dépend de la somme cumulative précédente, multipliée par 2, plus 1
            A[i] = 1 + sum(A[:i]) * 2

        # Calcul de la réponse principale : la somme de tous les éléments de A, multipliée par 2
        ans = sum(A) * 2

        # Si n est impair, on ajoute une valeur supplémentaire selon la formule
        if n % 2:
            ans += 1 + sum(A) * 2

        return ans

def main():
    """
    Boucle principale qui lit les valeurs de l'utilisateur depuis l'entrée standard.
    Continue jusqu'à ce qu'une exception surgisse (par exemple EOF).
    Pour chaque entrée, affiche le résultat du calcul en utilisant compute_sequence_sum.
    """
    while True:
        try:
            # Lecture et conversion de l'entrée utilisateur en entier
            n = int(raw_input())
            # Calcul du résultat et affichage
            print compute_sequence_sum(n)
        except:
            # Sort de la boucle en cas d'erreur (EOF ou entrée non valide)
            break

# Point d'entrée du programme
if __name__ == "__main__":
    main()