a, b, c = map(int, input().split())
calories = {'A': a, 'B': b, 'C': c}
# On veut éliminer le menu avec la plus grande calorie pour minimiser l'apport total
menu_to_skip = max(calories, key=calories.get)
print(menu_to_skip)