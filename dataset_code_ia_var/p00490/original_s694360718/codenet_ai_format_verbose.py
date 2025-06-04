number_of_pizzas, base_slices, additional_slices_per_topping, total_hungry_people, *topping_slices_list = map(int, open(0).read().split())

topping_slices_list.sort(reverse=True)

maximum_people_fed = total_hungry_people // base_slices

total_additional_slices = 0

for topping_index in range(number_of_pizzas):
    total_additional_slices += topping_slices_list[topping_index]
    current_people_fed = (total_hungry_people + total_additional_slices) // (base_slices + (topping_index + 1) * additional_slices_per_topping)
    maximum_people_fed = max(maximum_people_fed, current_people_fed)

print(maximum_people_fed)