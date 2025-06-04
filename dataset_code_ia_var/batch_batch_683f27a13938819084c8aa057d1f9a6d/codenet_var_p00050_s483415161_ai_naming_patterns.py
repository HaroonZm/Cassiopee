user_input = input()
swapped_fruits = user_input.replace('peach', 'TEMP_FRUIT').replace('apple', 'peach').replace('TEMP_FRUIT', 'apple')
print(swapped_fruits)