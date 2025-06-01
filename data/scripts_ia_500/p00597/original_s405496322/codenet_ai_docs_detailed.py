def calculate_value(n):
    """
    Calcule une valeur spécifique basée sur un entier n donné selon une règle définie.
    
    Pour n == 1, retourne directement 1.
    Sinon, crée une liste A de longueur n//2 où chaque élément A[i] est calculé
    comme 1 plus deux fois la somme des éléments précédents.
    La réponse finale est deux fois la somme de tous les éléments de A.
    Si n est impair, ajoute un terme supplémentaire : 1 plus deux fois la somme de A.
    
    Args:
        n (int): L'entier d'entrée pour lequel calculer la valeur.
        
    Returns:
        int: Le résultat calculé suivant la règle décrite.
    """
    if n == 1:
        return 1
    else:
        half = n // 2  # Division entière pour déterminer la moitié de n
        A = [0 for _ in range(half)]  # Initialisation de la liste A avec des zéros
        A[0] = 1  # Premier élément fixé à 1
        
        # Calcul des autres éléments en fonction de la somme des précédents multiplicée par 2, plus 1
        for i in range(1, half):
            A[i] = 1 + sum(A[:i]) * 2
        
        ans = sum(A) * 2  # Calcul partiel de la réponse finale
        
        # Si n est impair, on ajoute une correction supplémentaire
        if n % 2:
            ans += 1 + sum(A) * 2
        
        return ans


def main_loop():
    """
    Boucle principale de lecture continue des entrées utilisateur.
    
    Tente de lire un entier depuis l'entrée standard. Pour chaque entier,
    calcule la valeur correspondante à l'aide de la fonction calculate_value() et l'affiche.
    Arrête la boucle si une exception survient (par exemple, EOFError lors de la fin d'entrée).
    """
    while True:
        try:
            # Lecture de l'entrée utilisateur en utilisant raw_input() pour compatibilité Python 2
            n = int(raw_input())
            result = calculate_value(n)
            print(result)
        except:
            # Quitte la boucle en cas d'exception (fin de fichier ou entrée invalide)
            break


# Exécution de la boucle principale si ce script est lancé directement
if __name__ == "__main__":
    main_loop()