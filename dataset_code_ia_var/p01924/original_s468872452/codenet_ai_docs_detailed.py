def process_test_cases():
    """
    Lit et traite une série de jeux de données selon des règles spécifiques.
    Pour chaque jeu de données, calcule un résultat basé sur la logique suivante :
      - Pour chaque valeur lue, si elle est au moins égale à L, on initialise une 'fenêtre' ou période à D.
      - Tant que cette période n'est pas épuisée (rem > 0), chaque valeur suivante (quelle qu'elle soit) est comptée et la période décrémentée.
      - À la fin du batch, si au moins une valeur a été comptée (ans > 0), on retire 1 au total.
    Affiche le résultat pour chaque batch.
    """
    while True:
        # Lecture des paramètres du jeu de données : T (nombre d'éléments), D (durée), L (seuil)
        T, D, L = map(int, input().split())
        # Condition de terminaison : toutes les valeurs sont nulles
        if T == 0 and D == 0 and L == 0:
            break

        rem = 0  # Nombre de traitements restants dans la 'fenêtre' active
        ans = 0  # Compteur du nombre d'éléments traités dans la fenêtre

        # Pour chaque élément à traiter dans ce jeu de données
        for _ in range(T):
            x = int(input())  # Lecture de l'élément

            if x >= L:
                # Une nouvelle fenêtre est ouverte : on initialise/remet à D
                rem = D

            if rem:
                # Si une fenêtre est active, on compte cet élément et décrémente la fenêtre
                ans += 1
                rem -= 1

        if ans:
            # Si au moins un élément a été compté, on retire le premier de la fenêtre comme décrit dans la logique
            ans -= 1

        print(ans)

if __name__ == "__main__":
    process_test_cases()