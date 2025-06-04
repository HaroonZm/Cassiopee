number_of_toppings = int(raw_input())

base_price, topping_price = map(float, raw_input().split(" "))

base_calories = float(raw_input())

toppings_calories_list = []
for topping_index in range(number_of_toppings):
    individual_topping_calories = float(raw_input())
    toppings_calories_list.append(individual_topping_calories)

# Sort toppings by calories in descending order for optimal selection
toppings_calories_list.sort(cmp=lambda first, second: cmp(second, first))

total_calories = base_calories
total_price = base_price

for topping_calories in toppings_calories_list:
    current_ratio = total_calories / total_price
    new_ratio = (total_calories + topping_calories) / (total_price + topping_price)

    if current_ratio < new_ratio:
        total_calories += topping_calories
        total_price += topping_price
    else:
        break

print int(total_calories / total_price)