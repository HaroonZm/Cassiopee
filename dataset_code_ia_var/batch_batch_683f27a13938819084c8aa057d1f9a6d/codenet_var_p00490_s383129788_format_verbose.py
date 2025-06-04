total_number_of_additional_toppings = int(input())

price_of_dough, price_per_topping = map(int, input().split())

calories_of_dough = int(input())

max_calories_per_yen = calories_of_dough / price_of_dough
total_price = price_of_dough

calories_for_each_topping = [int(input()) for _ in range(total_number_of_additional_toppings)]
calories_for_each_topping.sort(reverse=True)

for index in range(total_number_of_additional_toppings):
    current_topping_calories = calories_for_each_topping[index]
    potential_total_calories = calories_of_dough + current_topping_calories
    potential_total_price = total_price + price_per_topping
    potential_calories_per_yen = potential_total_calories / potential_total_price

    if potential_calories_per_yen > max_calories_per_yen:
        max_calories_per_yen = potential_calories_per_yen
        calories_of_dough += current_topping_calories
        total_price += price_per_topping
    else:
        break

print(int(max_calories_per_yen))