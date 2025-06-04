def count_positive_sums():
    """
    Lit les entrées standard pour résoudre le problème suivant :
    Pour chaque ligne d'une matrice A (de taille n x m), calcule le produit scalaire avec le vecteur b,
    ajoute la constante c, puis compte le nombre de lignes pour lesquelles le résultat est strictement positif.
    
    Aucune valeur n'est retournée. Le résultat est affiché à la fin (le nombre calculé).
    """

    # Lecture et conversion des valeurs de n (lignes), m (colonnes) et c (constante) depuis l'entrée standard
    n, m, c = list(map(int, input().split()))

    # Lecture de la liste des coefficients b (taille m) depuis l'entrée standard
    b = list(map(int, input().split()))

    # Initialisation de la matrice a (liste de listes) pour stocker les lignes successives lues
    a = []
    for i in range(n):
        # Lecture de la i-ème ligne de la matrice et conversion en liste d'entiers
        a1 = list(map(int, input().split()))
        a.append(a1)

    # Compteur pour le nombre de lignes où la somme calculée est strictement positive
    count = 0

    # Pour chaque ligne de la matrice a
    for i in range(n):
        total = 0
        # Calcul du produit scalaire entre la ligne a[i] et le vecteur b
        for j in range(m):
            total += a[i][j] * b[j]
        # Ajout de la constante c au total
        total += c
        # Vérification si le résultat est strictement positif
        if total > 0:
            count += 1

    # Affichage du résultat total
    print(count)

# Appel de la fonction principale
count_positive_sums()