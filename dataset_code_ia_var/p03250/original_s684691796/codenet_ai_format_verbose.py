card_values_from_input = [int(card_value_string) for card_value_string in input().split()]

card_values_from_input.sort(reverse=True)

highest_card_value = card_values_from_input[0]
second_highest_card_value = card_values_from_input[1]
third_highest_card_value = card_values_from_input[2]

score_calculated = (highest_card_value * 10) + second_highest_card_value + third_highest_card_value

print(score_calculated)