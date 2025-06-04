def main():
    # Définition du modulo pour éviter les dépassements d'entiers dans les grandes sommes
    mod = 10 ** 9 + 7  # 10^9 + 7 est un nombre premier souvent utilisé pour les calculs modulaires

    # Lecture de deux entiers n et m depuis une entrée utilisateur
    n, m = map(int, input().split())  # n : taille du tableau, m : paramètre dépendant du problème

    # Lecture du tableau d'entiers a à partir de l'entrée utilisateur
    a = [int(x) for x in input().split()]  # Création d'une liste d'entiers à partir de l'entrée utilisateur

    # Si m vaut 0, il n'y a rien à calculer, donc afficher 0 et terminer la fonction
    if not m:  # Equivalent à "if m == 0"
        print(0)  # Afficher 0
        return  # Sortie de la fonction main

    # Initialisation d'un tableau mx de taille n+1 pour stocker les maximums progressifs
    mx = [0] * (n + 1)  # mx[i] contiendra la valeur maximale parmi les a[0] à a[i-1]
    # Initialisation d'un tableau mn de taille n+1 pour stocker les minimums progressifs, initialisé à mod
    mn = [mod] * (n + 1)  # mn[i] contiendra la valeur minimale parmi les a[i] à a[n-1]

    # Boucle pour remplir le tableau mx avec les valeurs maximales trouvées jusqu'à chaque index
    for i in range(n):  # Parcourt les indices de 0 à n-1
        if mx[i] > a[i]:  # Si le maximum actuel est supérieur à l'élément courant
            mx[i + 1] = mx[i]  # On conserve le maximum précédent
        else:
            mx[i + 1] = a[i]  # Sinon, le nouvel élément devient le nouveau maximum

    # Boucle pour remplir le tableau mn avec les valeurs minimales trouvées en partant de la droite
    for i in range(n - 1, -1, -1):  # Parcourt les indices de n-1 à 0 (ordre décroissant)
        if mn[i + 1] < a[i]:  # Si le minimum à droite est inférieur à l'élément courant
            mn[i] = mn[i + 1]  # On conserve le minimum suivant
        else:
            mn[i] = a[i]  # Sinon, le nouvel élément devient le nouveau minimum

    # Initialisation d'un tableau dp de taille n+1 pour stocker les valeurs intermédiaires de la programmation dynamique
    dp = [0] * (n + 1)  # Tous les éléments sont initialement à 0

    # Mise à jour de la valeur de dp[1], c'est souvent la base pour la programmation dynamique
    dp[1] = 2  # Cas de base : il y a deux façons au début selon la logique du problème

    # Boucle principale sur les éléments du tableau a (hors du premier déjà traité)
    for i in range(1, n):  # Boucle de 1 à n-1 inclus
        # Création d'un nouveau tableau ndp pour stocker les résultats provisoires de cette itération
        ndp = [0] * (n + 1)  # Initialisé à 0 à chaque itération

        # Les trois conditions de contrôle pour décider comment mettre à jour ndp suivant l'état courant
        check0 = mx[i + 1] == a[i]  # Vérifie si la valeur maximale jusque-là est effectivement a[i]
        check1 = mn[i + 1] >= mx[i]  # Vérifie si le minimum du segment droit est au moins le maximum du segment gauche
        check2 = mn[i] == a[i]  # Vérifie si la valeur minimale à partir d'ici est justement a[i]

        # Si la valeur maximale jusque-là est l'élément courant
        if check0:
            # Et si le minimum du segment droit est assez grand par rapport au maximum du segment gauche
            if check1:
                # Mise à jour de ndp selon deux transitions différentes
                for j in range(i + 1):  # Pour chaque possible état j
                    ndp[j + 1] += dp[j]  # Transition directe
                    ndp[i - j + 1] += dp[j]  # Transition basée sur le complément à l'indice actuel
            else:
                # Sinon, effectuer uniquement la transition directe
                for j in range(i + 1):  # Pour chaque possible état j
                    ndp[j + 1] += dp[j]  # Transition directe
        else:
            # Si ce n'est pas le maximum, mais si c'est le minimum du segment
            if check2:
                # Mise à jour neutre : recopier simplement dp
                for j in range(i + 1):  # Pour chaque possible état j
                    ndp[j] += dp[j]

        # Appliquer le modulo à chaque case de ndp pour éviter les dépassements et revenir dans l'intervalle du modulo
        dp = [x % mod for x in ndp]  # On effectue le modulo pour chaque valeur de ndp

    # Calcul du résultat final : somme des façons valides pour des indices de n-m à m inclus
    ans = 0  # Initialisation de la variable de réponse finale
    for i in range(n - m, m + 1):  # Pour chaque index dans cet intervalle
        ans += dp[i]  # Ajouter la valeur correspondante de dp
        ans %= mod  # Appliquer le modulo pour rester dans les bornes

    # Affichage du résultat final après l'itération
    print(ans)

# Exécution principale : ce bloc vérifie que le script est lancé directement et pas importé
if __name__ == "__main__":
    main()  # Appel de la fonction main pour lancer l'exécution du programme