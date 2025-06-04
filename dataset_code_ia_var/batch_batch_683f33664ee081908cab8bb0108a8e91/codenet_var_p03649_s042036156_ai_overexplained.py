def check(N, A, n):
    # Cette fonction vérifie si pour une valeur donnée 'n', une certaine condition basée sur le tableau A et le nombre N est satisfaite.
    # Arguments :
    # N : un entier donné (limite supérieure).
    # A : une liste d'entiers.
    # n : un entier représentant une quantité de ressources ou d'opérations utilisables.
    # But : Parcourir toutes les valeurs possibles d'une variable 'i' (de 0 à min(n,N) inclus),
    #       calculer 'x' pour chaque 'i', puis compter certains éléments selon un critère,
    #       et vérifier si le total de ces éléments n'excède pas 'x' pour une solution faisable.
    for i in range(min(n, N) + 1):
        # 'i' : itère de 0 jusqu'à min(n, N) inclus. Cela signifie qu'on considère jusqu'à N valeur de 'i', mais pas au-delà de 'n'.
        x = n - i  # On calcule 'x', qui est la différence entre 'n' et 'i'. Cela peut représenter le nombre d'opérations restantes après avoir utilisé 'i' opérations sur une partie.
        cnt = 0    # On initialise un compteur 'cnt' à 0. Ce compteur va calculer combien d'éléments du tableau A dépassent un certain seuil et combien d'opérations seraient alors nécessaires pour les 'ajuster'.
        for a in A:
            # Pour chaque élément 'a' dans la liste A, on teste la condition suivante :
            if a + x >= N:
                # Si 'a' augmenté de 'x' atteint ou dépasse N, alors il faut évaluer combien d'opérations additionnelles seraient nécessaires pour que 'a' ne dépasse pas N après l'ajout de 'x'.
                # L'expression suivante ajoute : 
                #   a + x - N + 1    : nombre d'unités à traiter au-delà de N, auquel on ajoute 1 pour rendre la division suivante "inclusive".
                #   (N+1)            : on divise par N+1, ce qui semble être une sorte de regroupement ou transformation par paquets de taille N+1.
                #   -(-//)           : l'opérateur 'divison entière négative', équivalent à 'ceil(a/b)', c'est-à-dire le plafond de la division.
                cnt += -(-(a + x - N + 1) // (N + 1))
                # Chaque fois qu'une telle condition est satisfaite, 'cnt' est incrémenté par le nombre de "paquets" excédents nécessaires pour ajuster l'élément à la limite N.
        # À la sortie de la boucle interne, 'cnt' contient le total d'opérations nécessaires pour ajuster tous les éléments de A dans ce cas-là.
        if cnt <= x:
            # Si le nombre total d'opérations requises (cnt) pour cette valeur de 'x' reste inférieur ou égal à 'x', cela signifie que cette solution est faisable avec 'x' opérations.
            return True
    # Si aucune des valeurs testées pour 'i' n'a permis de valider la condition, la fonction retourne False.
    return False

def main():
    # Cette fonction sert de point d'entrée principal pour exécuter le programme.
    # On commence par lire les entrées :
    N = int(input())   # On lit la première ligne en entrée, qui représente un entier N. L'utilisateur doit saisir un entier.
    A = list(map(int, input().split()))  # On lit la deuxième ligne, qui contient une liste d'entiers (séparés par des espaces). On convertit chaque élément en entier, puis on crée une liste A.
    lo = 0             # On initialise la borne inférieure 'lo' à 0. Cela représentera le plus petit nombre possible pour la recherche (dichotomique) de la solution optimale.
    hi = int(1e18)     # On initialise la borne supérieure 'hi' à 10^18 (un nombre très élevé). Cela représente la limite supérieure de la recherche.
    while lo < hi:     # Tant que la borne inférieure est strictement inférieure à la borne supérieure, on continue la recherche binaire.
        mid = (lo + hi) // 2   # On calcule la borne médiane 'mid' en faisant la moyenne entière de 'lo' et 'hi'. Cela permet de diviser la recherche en deux à chaque itération.
        if check(N, A, mid):   # On appelle la fonction 'check' avec les paramètres N, A, et la valeur 'mid' actuelle pour voir si la condition cible peut être satisfaite avec 'mid' opérations.
            hi = mid           # Si la fonction retourne True, c'est que la solution est possible avec au plus 'mid', donc on limite maintenant 'hi' à 'mid'.
        else:
            lo = mid + 1       # Sinon, cela veut dire que 'mid' est trop petit, donc toute solution valable nécessitera plus de ressources ; on élargit donc la recherche à la partie supérieure en mettant 'lo' à 'mid+1'.
    print(lo)         # À la fin de la boucle, 'lo' contiendra la plus petite solution entière qui satisfait la condition imposée par la fonction 'check'. On affiche alors cette solution.

if __name__ == "__main__":
    # Ce bloc permet de s'assurer que le code contenu dans ce fichier ne s'exécutera que si le fichier est lancé directement,
    # et non s'il est importé en tant que module depuis un autre script Python.
    main()           # On appelle la fonction principale pour démarrer le programme.