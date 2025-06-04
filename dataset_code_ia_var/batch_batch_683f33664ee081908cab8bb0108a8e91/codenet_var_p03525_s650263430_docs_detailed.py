def min_time_difference(N, D):
    """
    Calcule la différence minimale de temps entre des individus ayant des décalages horaires,
    en appliquant les contraintes suivantes :
    - Les personnes ayant un même décalage horaire apparaissant trois fois ou plus rendent la différence minimale 0.
    - Une fois pour chaque décalage, on peut placer ce décalage ou son complément (24-D) pour minimiser les écarts.

    Args:
        N (int): Nombre d'individus
        D (List[int]): Liste des décalages horaires de chaque individu (0 <= D[i] < 24)

    Returns:
        int: Différence minimale de temps possible parmi les horaires choisis
    """
    from collections import Counter, defaultdict

    # Compter le nombre d'apparition de chaque décalage horaire dans la liste
    c = Counter(D)
    # Ajouter une unité supplémentaire pour le décalage 0 afin d'éviter des erreurs de corner-case
    c[0] += 1

    # Vérifier les conditions qui rendent la différence minimale 0 :
    for i in range(13):  # On ne parcourt que la moitié (0 à 12 inclusive) car 24-D recouvre l'autre moitié
        if i == 0 or i == 12:
            # Si il y a deux personnes ou plus avec un décalage horaire de 0 ou 12, la différence sera forcément 0
            if c[i] >= 2:
                return 0
        else:
            # Si il y a au moins trois personnes avec le même décalage, la différence minimale est 0
            if c[i] >= 3:
                return 0

    # On trie les décalages horaires pour les traiter dans l'ordre
    D.sort()

    # On va utiliser un dictionnaire pour compter le nombre d’individus à chaque horaire choisi
    # Initialement, 24h est déjà présent avec un compteur à 1 pour permettre un cycle horaire complet
    d = defaultdict(int)
    d[24] += 1

    # Indicateur pour alterner entre placer t et 24-t pour chaque individu
    is_am = True

    for t in D:
        if is_am:
            # On ajoute l'horaire tel quel
            d[t] += 1
            is_am = False
        else:
            # On ajoute le complément à 24 pour l’alternance
            d[24 - t] += 1
            is_am = True

    # Initialisation de la réponse avec la plus petite valeur de décalage
    ans = min(D)
    # Extraire la liste triée des horaires utilisés
    times = list(d.keys())
    times.sort()

    # Calculer la différence minimale entre deux horaires consécutifs
    for a, b in zip(times, times[1:]):
        ans = min(ans, b - a)

    return ans

def main():
    """
    Fonction principale pour lire les entrées, calculer la différence minimale de temps et afficher la réponse.
    """
    N = int(input())
    D = list(map(int, input().split()))
    result = min_time_difference(N, D)
    print(result)

if __name__ == "__main__":
    main()