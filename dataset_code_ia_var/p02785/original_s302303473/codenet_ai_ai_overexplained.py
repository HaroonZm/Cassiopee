# Début de la définition de la fonction principale appelée 'main'
def main():
    # On lit une ligne de texte depuis l'entrée standard (par défaut le clavier),
    # puis on applique la méthode split() qui sépare la chaîne en une liste de sous-chaînes
    # à chaque espace rencontré. Par exemple, si l'utilisateur tape "3 2", cela retourne ["3", "2"].
    # Ensuite, on utilise map() pour appliquer la fonction int à chaque élément de la liste,
    # ce qui convertit chaque sous-chaîne (qui représente un chiffre) en un nombre entier.
    # Enfin, les deux entiers récupérés sont assignés respectivement à N et K.
    N, K = map(int, input().split())

    # On lit de nouveau une ligne de texte de l'utilisateur. L'utilisateur devrait saisir N entiers séparés par des espaces.
    # On utilise input(), puis split() afin de récupérer une liste de chaînes de caractères.
    # On applique map(int, ...) pour convertir chaque chaîne en entier.
    # On convertit finalement l'objet obtenu grâce à map() en une vraie liste d'entiers, que l’on assigne à la variable H.
    H = list(map(int, input().split()))

    # On trie la liste H en ordre décroissant. La fonction sorted() retourne une nouvelle liste triée.
    # L'argument reverse=True indique que l'on veut un tri par ordre décroissant (du plus grand au plus petit).
    # Ainsi, le ou les plus grands éléments de la liste seront placés au début de la liste.
    H = sorted(H, reverse=True)

    # On teste si le nombre d'éléments N est inférieur ou égal à K.
    # Cela signifie qu'il y a autant (ou plus) d'éléments que la valeur de K.
    if N <= K:
        # Dans ce cas, on affiche simplement '0' grâce à la fonction print().
        # Cela signifie probablement (dans le contexte original) qu'aucun coût n'est requis, 
        # ou qu'aucune opération n'est nécessaire.
        print(0)
    else:
        # Sinon (c'est-à-dire si N > K), on considère les éléments de l'indice K (inclus)
        # jusqu'à la fin de la liste H, grâce au découpage H[K:].
        # En Python, H[K:] crée une nouvelle liste à partir du (K+1)-ième élément jusqu'au dernier.
        # On applique la fonction sum() sur cette sous-liste afin de calculer la somme de tous ses éléments.
        # Enfin, on affiche le résultat avec print().
        print(sum(H[K:]))

# Ce bloc est une convention en Python pour s'assurer que le code suivant s'exécute seulement
# si ce fichier est exécuté directement (et pas supposé être importé dans un autre module).
if __name__ == '__main__':
    # On appelle la fonction main pour démarrer le programme.
    main()