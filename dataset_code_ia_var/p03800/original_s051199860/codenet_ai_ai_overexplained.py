import sys  # Importe le module sys afin d'accéder à des fonctionnalités système (ex: gestion des flux I/O)
from itertools import product  # Importe la fonction product du module itertools, qui sert à générer des produits cartésiens

def debug(x, table):
    # Cette fonction accepte deux arguments :
    #   x : une variable à comparer,
    #   table : un dictionnaire contenant des couples clé:valeur.
    # Elle affiche sur la sortie d'erreur standard (stderr) le nom de la variable et sa valeur si x correspond à une des valeurs du dictionnaire.
    for name, val in table.items():  # Pour chaque couple (clé, valeur) dans le dictionnaire table
        if x is val:  # Vérifie si x est exactement la même instance en mémoire que val (comparaison stricte "is")
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)  # Affiche le nom de la variable et sa valeur sur stderr
            return None  # Sort de la fonction immédiatement

def solve():
    # Cette fonction gère la résolution du problème principal.
    N = int(input())  # Lit une ligne de l'entrée standard, la convertit en entier et l'assigne à N. Correspond ici à la longueur du motif.
    S = [0 if i == 'o' else 1 for i in input()]  # Lit la chaîne d'entrée, puis pour chaque caractère :
    # Si c'est 'o', stocke un 0 ; si c'est autre chose (ici supposé 'x'), stocke un 1.
    # Résulte en une liste d'entiers (0 et 1) de longueur N.

    # La prochaine boucle tente toutes les combinaisons possibles (il y en a 4) pour les deux premiers éléments du motif.
    # product(range(2), repeat=2) génère [(0,0), (0,1), (1,0), (1,1)] c'est-à-dire toutes les combinaisons de deux bits.
    for i, j in product(range(2), repeat=2):
        # i et j représentent les deux premiers éléments du motif que l'on cherche à reconstituer
        
        # Crée la liste pat représentant le motif reconstitué en partant des deux premiers éléments i et j
        pat = [i, j] + [0]*(N - 2)  # Commence avec i et j ; complète la liste avec des zéros pour atteindre une taille N.

        # Remplit le reste du motif à partir de l'indice 2 jusqu'à N-1 (inclus)
        for k in range(2, N):
            # Calcule la valeur à la position k en se basant sur la formule spécifique du problème.
            # La formule utilise la valeur dans S en position k-1,
            # en soustrayant la somme des deux précédents éléments du motif, le tout modulo 2.
            pat[k] = (S[k - 1] - (pat[k - 1] + pat[k - 2])) % 2

        # Vérification de la cohérence du motif généré.
        # Condition 1 : vérifie que la dernière contrainte du problème est respectée.
        # test : la dernière valeur de S doit être égale à la somme (modulo 2)
        # de la première, de la dernière et de l'avant-dernière valeur du motif pat.
        if S[-1] != (pat[0] + pat[-1] + pat[-2]) % 2:
            continue  # Si ce n'est pas respecté, on passe à la combinaison suivante.

        # Condition 2 : la première contrainte.
        # test : la première valeur de S doit être égale à la somme (modulo 2)
        # de la deuxième, de la première et de la dernière valeur du motif pat.
        if S[0] != (pat[1] + pat[0] + pat[-1]) % 2:
            continue  # Si ce n'est pas respecté, essaie la prochaine combinaison.

        # Si on arrive ici, ça veut dire que les deux contraintes sont remplies.
        # Il faut maintenant transformer la liste pat (contenant des 0 et 1) en une chaîne de caractères selon la règle suivante :
        #   0 -> 'S', 1 -> 'W'
        ans = ['S' if pat[k] == 0 else 'W' for k in range(N)]  # Crée une nouvelle liste de caractères à partir de pat.

        print(''.join(ans))  # Affiche la réponse sur la sortie standard, c'est-à-dire la chaîne reconstruite.
        return None  # Sort immédiatement de la fonction car une solution a été trouvée.

    # Si aucune combinaison (parmi les 4 testées) ne fonctionne, on affiche -1 pour signaler l'absence de solution valide.
    print(-1)

# Ce test sert à s'assurer que la fonction solve() ne se lance que si le fichier est exécuté en tant que script principal (et pas lors d'un import)
if __name__ == '__main__':
    solve()  # Exécute la fonction principale qui gère tout le processus.