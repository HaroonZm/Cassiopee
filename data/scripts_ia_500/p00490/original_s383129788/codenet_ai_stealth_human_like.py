n = int(input())
x, y = map(int, input().split())
initial_pizza = int(input())

best_ratio = initial_pizza / x
total_people = x
toppings = [int(input()) for _ in range(n)]
toppings.sort(reverse=True)  # Try biggest toppings first

for topping in toppings:
    new_ratio = (initial_pizza + topping) / (total_people + y)
    if new_ratio > best_ratio:
        best_ratio = new_ratio
        initial_pizza += topping
        total_people += y
    else:
        # no improvement, better to stop adding toppings
        break

print(int(best_ratio))