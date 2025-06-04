# Définition de la fonction "binary_search" qui calcule la combinaison optimale d'achat de poulets Aizu et de poulets normaux
def binary_search(quantity, budget, aizu_chicken_price, chicken_price, aizu_chicken_limit):
    # Vérifie si le budget permet d'acheter au moins 1 poulet Aizu et le reste en poulets normaux
    # (quantity - 1) * chicken_price + aizu_chicken_price calcule le coût minimum possible pour acheter "quantity" de poulets
    if budget < (quantity - 1) * chicken_price + aizu_chicken_price:
        # Si le budget est insuffisant pour cette configuration, retourne None
        return None

    # Vérifie si le budget suffit pour acheter uniquement des poulets Aizu
    # aizu_chicken_price * quantity calcule le coût pour acheter seulement des poulets Aizu
    if aizu_chicken_price * quantity <= budget:
        # Calcule combien de poulets Aizu on peut acheter avec le budget
        aizu_chicken_count = budget // aizu_chicken_price

        # Si la limite sur le nombre de poulets Aizu est dépassée, l'ajuste à la limite maximale permise
        if aizu_chicken_limit < aizu_chicken_count:
            aizu_chicken_count = aizu_chicken_limit

        # Calcule le budget restant après l'achat des poulets Aizu
        rest = budget - aizu_chicken_price * aizu_chicken_count
        # Calcule combien de poulets normaux peuvent être achetés avec le reste du budget
        chicken_count = rest // chicken_price
        # Retourne un tuple contenant le nombre de poulets Aizu et de poulets normaux achetés
        return aizu_chicken_count, chicken_count

    # Vérifie si on peut acheter le maximum de poulets Aizu autorisés par la limite et compléter le reste avec des poulets normaux
    # aizu_chicken_price * aizu_chicken_limit + chicken_price * (quantity - aizu_chicken_limit) calcule le cas où la limite de poulets Aizu est atteinte
    if aizu_chicken_price * aizu_chicken_limit + chicken_price * (quantity - aizu_chicken_limit) < budget:
        # Calcule le reste du budget après avoir acheté le maximum de poulets Aizu permis
        rest = budget - aizu_chicken_price * aizu_chicken_limit
        # Calcule combien de poulets normaux peuvent être achetés avec le reste du budget
        chicken_count = rest // chicken_price
        # Retourne la combinaison trouvée
        return aizu_chicken_limit, chicken_count

    # Si les cas précédents ne sont pas satisfaits, on lance une recherche binaire pour trouver la meilleure combinaison possible

    # Initialise le nombre de poulets Aizu à la moitié de la limite permise 
    aizu_chicken_count = aizu_chicken_limit // 2
    # Calcule le nombre de poulets normaux à acheter pour compléter le total requis
    chicken_count = quantity - aizu_chicken_count
    # Initialise la valeur de l'incrément/décrément pour ajuster aizu_chicken_count lors de la recherche binaire
    update_count = aizu_chicken_count // 2 + 1

    # Initialise le meilleur couple trouvé (nombre de poulets Aizu, nombre de poulets normaux)
    max_pair = (0, quantity)

    # Boucle de recherche binaire, continue tant que update_count est strictement positif
    while 0 < update_count:

        # Vérifie si le coût total actuel ne dépasse pas le budget
        if aizu_chicken_count * aizu_chicken_price + chicken_count * chicken_price <= budget:
            # Met à jour le meilleur couple trouvé
            max_pair = (aizu_chicken_count, chicken_count)
            # Augmente le nombre de poulets Aizu pour voir si on peut en acheter plus
            aizu_chicken_count += update_count + 1
            # Diminue d'autant le nombre de poulets normaux pour garder le total cohérent
            chicken_count -= (update_count + 1)

        else:
            # Diminue le nombre de poulets Aizu car le budget ne suffit pas
            aizu_chicken_count -= (update_count + 1)
            # Augmente d'autant le nombre de poulets normaux pour compenser
            chicken_count += update_count + 1

        # Réduit la valeur de update_count pour raffiner la recherche lors de la prochaine itération
        update_count //= 2

    # Retourne le couple optimal trouvé par la recherche binaire
    return max_pair

# Entrée principale du programme, boucle infinie pour traiter plusieurs jeux de données
while True:

    # Récupère une entrée utilisateur sous forme de chaîne de caractères
    input_data = input()

    # Vérifie si l'utilisateur a saisi "0", ce qui indique la fin de la saisie
    if input_data == "0":
        # Sort de la boucle, arrêt du programme principal
        break

    # Découpe la chaîne de caractères sur chaque espace pour obtenir les valeurs numériques
    # Convertit ensuite chaque élément texte en entier et stocke dans les variables correspondantes
    quantity, budget, aizu_chicken_price, chicken_price, aizu_chicken_limit = [int(item) for item in
                                                                               input_data.split(" ")]

    # Appelle la fonction binary_search pour calculer la meilleure configuration possible avec les paramètres saisis
    result = binary_search(quantity, budget, aizu_chicken_price, chicken_price, aizu_chicken_limit)

    # Si une solution existe (result n'est pas None), affiche les quantités de poulets Aizu et de poulets normaux achetées
    if result is not None:
        print(result[0], result[1])
    else:
        # Si aucune combinaison n'est possible, affiche "NA"
        print("NA")