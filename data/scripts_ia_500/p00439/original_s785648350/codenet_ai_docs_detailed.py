a, s = [0]*100003, [0]*100003  # Initialisation des deux listes pour stocker les valeurs et les sommes glissantes

while True:
    # Lecture des deux entiers n (nombre d'éléments) et k (taille de la sous-séquence)
    n, k = map(int, input().split())

    if n == 0:
        # Condition d'arrêt du programme : si n est égal à 0, on sort de la boucle
        break

    # Lecture du premier élément de la séquence
    s[0] = a[0] = int(input())

    # Calcul des sommes glissantes pour les indices de 1 à n-1
    for i in range(1, n):
        a[i] = int(input())  # Lecture de l'élément à l'indice i
        s[i] = s[i-1] + a[i]  # Addition de l'élément courant à la somme précédente

        # Ajustement de la somme glissante pour conserver uniquement la somme des derniers k éléments
        if i >= k:
            s[i] -= a[i-k]

    # Initialisation de la variable 'ans' avec la première somme de taille k
    ans = s[k-1]

    # Parcours des sommes glissantes restantes pour trouver la valeur maximale
    for i in range(k, n):
        if s[i] > ans:
            ans = s[i]

    # Affichage du résultat : la somme maximale d'une sous-séquence contiguë de taille k
    print(ans)


def max_sliding_sum():
    """
    Fonction principale pour trouver la somme maximale d'une sous-séquence contiguë de taille k
    sur plusieurs jeux de données jusqu'à ce que n = 0 soit rencontré.

    Lecture des entrées:
    - n : nombre d'éléments de la séquence (entier)
    - k : taille de la sous-séquence pour laquelle on veut la somme maximale (entier)
    - a[i] : i-ème élément de la séquence (entier)

    Sortie:
    - La somme maximale d'une sous-séquence contiguë de taille k pour chaque jeu de données.

    La fonction lit en boucle les entrées, traite les données avec une somme glissante,
    et affiche le résultat jusqu'à ce que n soit égal à 0.
    """
    a, s = [0]*100003, [0]*100003  # listes pour stocker les valeurs et les sommes glissantes
    while True:
        n, k = map(int, input().split())
        if n == 0:
            break
        s[0] = a[0] = int(input())
        for i in range(1, n):
            a[i] = int(input())
            s[i] = s[i-1] + a[i]
            if i >= k:
                s[i] -= a[i-k]
        ans = s[k-1]
        for i in range(k, n):
            if s[i] > ans:
                ans = s[i]
        print(ans)

# Appel de la fonction principale si besoin
# max_sliding_sum()