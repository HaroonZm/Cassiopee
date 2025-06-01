# Programme Python pour résoudre le problème "おそろいの景品"
# L'objectif est de déterminer le nombre minimal de défis nécessaires
# pour obtenir au moins deux exemplaires identiques d'un même lot de prix,
# en fonction du stock disponible.

def main():
    while True:
        # Lecture du nombre de types de prix (N)
        line = input().strip()
        if line == '0':
            # Fin de la saisie des données
            break
        N = int(line)

        # Lecture des stocks pour les N types de prix
        # Les stocks sont sur une seule ligne, séparés par des espaces
        stocks = list(map(int, input().strip().split()))
        # Vérification du nombre correct de stocks en fonction de N
        if len(stocks) != N:
            # Si les données sont incorrectes, on arrête
            # (cette situation ne devrait pas arriver dans l'énoncé)
            print("NA")
            continue

        # Filtrage des prix dont la quantité est au moins 2 car 
        # sinon il est impossible d'obtenir 2 fois le même prix
        eligible_counts = [k for k in stocks if k >= 2]

        if not eligible_counts:
            # Aucun prix n'est disponible en quantité >= 2, donc impossible
            print("NA")
            continue

        # Pour déterminer le nombre minimal de défis nécessaires afin d'obtenir 
        # 2 exemplaires identiques quel que soit l'ordre d'apparition,
        # on applique le raisonnement de la pire situation.

        # Raisonnement :
        # Dans le pire cas, on peut obtenir 1 exemplaire de chaque prix 
        # (quel que soit leur stock) avant de retomber sur un doublon.
        # Donc, on regarde combien il y a de types de prix que l'on peut obtenir *au moins une fois*.
        # Or, dans la pire situation, on va obtenir toutes les sortes disponibles une fois.
        # Puis, le prochain tirage sera nécessairement un doublon, car on a épuisé les sortes simples.

        # Mais on doit aussi vérifier que pour chaque type qui a au moins 2 exemplaires,
        # on dispose suffisamment de stock.

        # Le nombre minimal de défis nécessaires est donc:
        # (nombre de prix avec stock >=1) + 1

        # Comptons tous les prix qui ont au moins 1 exemplaire, pour estimer le pire cas
        available_once_counts = [k for k in stocks if k >= 1]

        # Si on a N types de prix avec au moins 1 exemplaire, dans le pire
        # des cas on tire chacun une fois, donc N fois, et le prochain tirage (N+1)
        # donnera forcément un doublon vu tous les types sont épuisés d'un exemplaire.
        # Mais on doit vérifier si le stock est suffisant pour certains types.

        # Cependant, le problème mentionne spécifiquement que la quantité initiale est connue,
        # et qu'on veut le nombre minimal garanti de tirages pour obtenir au moins 2 exemplaires
        # identiques. Dans le pire des cas il faut prendre en compte le nombre maximum de 
        # prix distincts disponibles (au moins 1) plus un pour assurer un doublon.

        # Or, si le nombre total d'exemplaires disponibles est < 2,
        # c'est impossible.

        # On vérifie aussi si la quantité totale disponible est suffisante
        total_stock = sum(stocks)
        if total_stock < 2:
            print("NA")
            continue

        # La quantité de prix disponibles (au moins 1 exemplaire) est len(available_once_counts)
        # Donc le pire cas minimal est len(available_once_counts) + 1

        # En fait, si on a 1 seule sorte, minimal = 2 (deux tirages)
        # Sinon minimal = nombre de prix avec au moins 1 exemplaire + 1

        minimal = len(available_once_counts) + 1

        # Cependant, si un prix n'a qu'un seul exemplaire, dans le pire cas il est obtenu une fois,
        # mais on ne pourra pas avoir deux exemplaires de celui-ci, donc il ne compte pas pour garantir un doublon.
        # On doit considérer uniquement les prix avec au moins 2 exemplaires.

        # NB: En reprenant l'explication des exemples donnés:
        # Exemple 1: stocks = [3, 2], on a 2 types avec au moins 1 exemplaire: 2 + 1 = 3 => ok
        # Exemple 2: stocks = [0, 1, 1], aucun stock >= 2 donc NA
        # Exemple 3: stocks = [1000], un seul type => minimal = 2

        # Donc pour corriger le raisonnement:
        # minimal = nombre de prix avec stock >= 1 + 1, mais on ne compte pas les prix qui ne permettent pas un doublon 
        # (stock >= 2)

        # Calcul du nombre de types de prix avec stock >= 1 et avec au moins un doublon possible (stock >= 2)
        count_at_least_one = sum(1 for k in stocks if k >= 1)
        count_at_least_two = sum(1 for k in stocks if k >= 2)

        if count_at_least_two == 0:
            # Pas possible d'avoir doublon
            print("NA")
            continue

        # minimal = nombre de prix avec au moins 1 exemplaire + 1
        minimal = count_at_least_one + 1

        print(minimal)


if __name__ == '__main__':
    main()