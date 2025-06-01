def compute_max_score():
    """
    Lit un entier n puis une liste de n entiers depuis l'entrée standard.
    Calcule ensuite, via une programmation dynamique sur des indices circulaires,
    une valeur maximale selon une règle particulière affectant un tableau dp.
    
    La logique considère à chaque étape un offset i, et met à jour le tableau dp en fonction
    des valeurs relatives des éléments de la liste a à des positions cycliques, ainsi que des 
    valeurs précedentes du dp. L'indice est traité modulo n pour simuler une structure circulaire.
    
    Enfin, la fonction affiche la valeur maximale obtenue de dp après n itérations.
    
    Entrée attendue (depuis input()) :
    - n : nombre entier correspondant à la taille de la liste a
    - a : n entiers, chacun sur une ligne
    
    Sortie :
    - un entier, la valeur maximale calculée selon la règle décrite.
    """
    # Lecture du nombre d'éléments
    n = int(input())
    
    # Lecture des éléments de la liste a
    a = [int(input()) for _ in range(n)]
    
    # Initialisation du tableau dp de taille n avec des zéros
    dp = [0 for _ in range(n)]
    
    # Boucle sur i qui représente un offset dans la structure circulaire
    for i in range(n):
        if i % 2 == n % 2:
            # Si la parité de i est égale à celle de n:
            # Pour chaque position l dans [0, n-1], on compare a[l] et a[(l+i)%n]
            # Si a[l] est plus grand, on met à jour dp[l] en prenant dp[(l+1)%n]
            # Sinon, on garde dp[l].
            # Cette mise à jour simule une rotation et des comparaisons circulaires.
            dp = [ dp[(l+1)%n] if a[l] > a[(l+i)%n] else dp[l] for l in range(n)]
        else:
            # Si la parité de i est différente de celle de n:
            # Mise à jour différente : pour chaque l,
            # on calcule le maximum entre a[l]+dp[(l+1)%n] et a[(l+i)%n]+dp[l].
            dp = [max(a[l] + dp[(l+1)%n], a[(l+i)%n] + dp[l]) for l in range(n)]
    
    # Affichage du maximum des valeurs finales de dp
    print(max(dp))


# Appel de la fonction principale pour exécution
compute_max_score()