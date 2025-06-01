def binary_search(qty, budget, price_aizu, price_chicken, limit_aizu):
    # si le budget est trop petit pour acheter au moins un lot
    if budget < (qty - 1) * price_chicken + price_aizu:
        return None

    # si on peut acheter uniquement du poulet d'Aizu
    if price_aizu * qty <= budget:
        count_aizu = budget // price_aizu
        if count_aizu > limit_aizu:
            count_aizu = limit_aizu   # j'aime bien respecter les limites

        rest_budget = budget - price_aizu * count_aizu
        count_chicken = rest_budget // price_chicken
        return count_aizu, count_chicken

    # cas où on achète tout le quota d'Aizu puis le reste en poulet normal
    if price_aizu * limit_aizu + price_chicken * (qty - limit_aizu) < budget:
        rest = budget - price_aizu * limit_aizu
        count_chicken = rest // price_chicken
        return limit_aizu, count_chicken

    # allez, on essaie une sorte de recherche binaire pour optimiser le nombre
    count_aizu = limit_aizu // 2
    count_chicken = qty - count_aizu
    step = count_aizu // 2 + 1

    max_combo = (0, qty)  # meilleur combo qu'on a trouvé

    while step > 0:
        cost = count_aizu * price_aizu + count_chicken * price_chicken

        if cost <= budget:
            max_combo = (count_aizu, count_chicken)
            count_aizu += step + 1   # je rajoute un peu plus pour avancer vite
            count_chicken -= step + 1
        else:
            count_aizu -= step + 1
            count_chicken += step + 1

        step //= 2   # réduction progressive du pas

    return max_combo


while True:
    user_input = input()
    if user_input == "0":
        break
    vals = [int(x) for x in user_input.split()]
    qty, budget, price_aizu, price_chicken, limit_aizu = vals

    res = binary_search(qty, budget, price_aizu, price_chicken, limit_aizu)
    if res is not None:
        print(res[0], res[1])
    else:
        print("NA")