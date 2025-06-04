# --*-coding:utf-8-*--

def main():
    """
    Résout le problème selon la logique suivante :
    1. Lit les entrées : taille du tableau N, et deux tableaux d'entiers A et B.
    2. Teste si, pour les tableaux triés, tous les éléments de A sont inférieurs ou égaux à ceux de B.
    3. Si la condition précédente passe, teste s'il existe un décalage permettant à tous les A d'être plus petits ou égaux à B (décalé d'une position).
    4. Si aucune condition précédente ne passe, effectue une vérification cyclique sur un réarrangement complexe pour déterminer si une permutation particulière permet d'établir la contrainte imposée.
    Renvoie 'Yes' ou 'No' selon la solution trouvée.
    """
    # Lecture de la taille du tableau
    N = int(input())
    # Lecture et conversion du tableau A en entiers
    A = list(map(int, input().split()))
    # Lecture et conversion du tableau B en entiers
    B = list(map(int, input().split()))

    # Tri croissant des deux tableaux pour simplifier les comparaisons
    A2 = sorted(A)
    B2 = sorted(B)
    
    # Première condition :
    # Pour chaque indice, vérifie si l'élément correspondant de A2 est supérieur à B2
    # Si oui, il n'est pas possible de satisfaire la condition demandée
    for i in range(N):
        if A2[i] > B2[i]:
            print('No')
            return

    # Deuxième condition :
    # Vérifie si pour un décalage, chaque élément de A2 est inférieur ou égal au précédent élément de B2
    # Ceci pourrait permettre un permutation ou une rotation avantageuse
    for i in range(1, N):
        if A2[i] <= B2[i-1]:
            print('Yes')
            return

    # Si les deux vérifications précédentes n'ont rien donné,
    # on effectue une analyse plus approfondie basée sur les indices des éléments des tableaux triés
    # On crée une liste B3 où on génère des couples (indice initial, valeur de B trié, indice trié)
    B3 = sorted(
        map(
            lambda x: (x[1][1], x[0]),
            enumerate(
                sorted(
                    map(lambda x: (x[1], x[0]), enumerate(B))
                )
            )
        )
    )

    # On crée une nouvelle liste C qui va servir pour la vérification cyclique suivante
    # Elle contient l'indice trié du tableau B pour chaque élément de A
    # On utilise zip pour associer chaque valeur de A avec l'élément correspondant dans B3
    # On trie ces couples selon les valeurs de A, puis on extrait le second indice de B
    C = list(map(lambda x: x[1][1], sorted(zip(A, B3))))

    # Vérification cyclique pour détecter une éventuelle permutation circulaire satisfaisante
    p = 0
    for i in range(N-1):
        p = C[p]
        if p == 0:
            print('Yes')
            return

    # Si aucune des conditions n'est remplie, on affiche 'No'
    print('No')


if __name__ == '__main__':
    main()