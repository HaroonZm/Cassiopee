def solve():
    """
    Lit plusieurs cas de test depuis l'entrée standard et pour chaque cas, trouve la somme maximale
    d'un sous-tableau contigu de taille k dans une liste de n entiers.

    Le programme s'arrête lorsque la valeur de n est égale à 0.

    Format des entrées pour chaque cas de test :
        - La première ligne contient deux entiers n et k.
        - Les n lignes suivantes contiennent chacune un entier de la liste A.

    Sortie :
        - Pour chaque cas de test, affiche un entier représentant la somme maximale possible d'un sous-tableau
          contigu de taille k dans la liste A.
    """
    while True:
        # Lecture des deux entiers n (taille de la liste) et k (taille du sous-tableau)
        n, k = [int(_) for _ in input().split()]
        # Condition d'arrêt : lorsque n vaut 0, on termine la fonction
        if n == 0:
            return

        # Lecture de la liste A contenant n entiers
        A = [int(input()) for _ in range(n)]

        # Création d'une liste s pour stocker les sommes préfixes de A
        # s[i] correspond à la somme des i premiers éléments de A (s[0] = 0)
        s = [0] * (len(A) + 1)
        for i in range(n):
            s[i + 1] = s[i] + A[i]

        # Initialisation de la variable ans pour conserver la somme maximale trouvée
        ans = -1
        # Parcours possible des indices gauche du sous-tableau contigu
        for l in range(n):
            r = l + k  # Indice droit exclusif du sous-tableau
            # Si l'indice droit dépasse la taille de la liste, on arrête la boucle
            if r > n:
                break
            # Calcul de la somme du sous-tableau de taille k grâce aux sommes préfixes
            current_sum = s[r] - s[l]
            # Mise à jour de la somme maximale si la somme actuelle est plus grande
            if current_sum > ans:
                ans = current_sum
        
        # Affichage du résultat pour ce cas de test
        print(ans)


if __name__ == '__main__':
    solve()