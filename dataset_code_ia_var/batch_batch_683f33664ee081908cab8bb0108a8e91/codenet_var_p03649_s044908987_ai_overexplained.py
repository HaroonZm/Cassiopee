def main():
    # Demander à l'utilisateur d'entrer un entier N.
    # Cela représente la taille du tableau ou le nombre d'éléments à traiter.
    N = int(input())  # Conversion explicite en entier car input() retourne une chaîne de caractères.

    # Demander à l'utilisateur d'entrer N entiers, séparés par des espaces.
    # map() applique la fonction int à chaque élément obtenu via input().split(), donnant des entiers.
    # L'étoile *a dépaquette la séquence obtenue en une vraie liste 'a'.
    *a, = map(int, input().split())

    # Calculer la somme totale des éléments du tableau 'a'.
    # sum() prend en argument un itérable et retourne la somme de tous ses éléments.
    tot = sum(a)

    # Définir une fonction booléenne auxiliaire is_ok qui prend comme argument un entier k.
    def is_ok(k):
        # Pour chaque élément x dans le tableau a, créer une nouvelle séquence b où on ajoute k et on soustrait (N - 1) à x.
        # Il s'agit d'une compréhension générateur, ici utilisée pour le calcul intermédiaire sans stocker la liste entière en mémoire.
        b = (x + k - (N - 1) for x in a)

        # Initialiser un compteur 'cnt' à 0.
        cnt = 0

        # Pour chaque élément x dans la séquence b obtenue, effectuer un calcul.
        # Pour chaque x : ajouter N, puis faire une division entière vers le haut (en utilisant //) par (N + 1).
        # Ajoute le résultat à cnt.
        for x in b:
            cnt += (x + N) // (N + 1)

        # Retourner un booléen : True si cnt <= k, sinon False.
        return cnt <= k

    # Initialiser la variable ret, qui va contenir le résultat final. Mettre à zéro par défaut.
    ret = 0

    # Calculer une valeur de départ pour k.
    # On prend la valeur maximale entre 0 et tot - N * (N - 1).
    # Cette expression garantit que k ne prend jamais une valeur négative et commence à un minimum plausible pour une solution.
    k = max(0, tot - N * (N - 1))

    # Boucle tant que k est inférieur ou égal à tot.
    while k <= tot:
        # Appeler la fonction is_ok() avec le paramètre courant k.
        # Si elle retourne True, c'est que k est valide.
        if is_ok(k):
            # Stocker la solution dans ret.
            ret = k
            # Sortir immédiatement de la boucle, car on veut la première telle valeur valide de k.
            break
        # Sinon, augmenter k de 1 pour tester la valeur suivante.
        k += 1

    # Afficher le résultat final après la boucle.
    print(ret)

# Si ce fichier est exécuté directement (et non importé comme module),
# alors exécuter la fonction main().
if __name__ == '__main__':
    main()