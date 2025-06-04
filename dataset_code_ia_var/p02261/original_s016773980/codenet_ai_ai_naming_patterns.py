import sys

class CardObject:

    def __init__(self, card_string):
        self.card_string = card_string
        self.card_mark = card_string[0]
        self.card_value = int(card_string[1])

    def __str__(self):
        return self.card_string

def print_card_list(card_list):
    for card_index in range(len(card_list)):
        sys.stdout.write(str(card_list[card_index]))
        if card_index != len(card_list) - 1:
            sys.stdout.write(' ')
    print()

def swap_elements(element_list, index_a, index_b):
    temp_element = element_list[index_a]
    element_list[index_a] = element_list[index_b]
    element_list[index_b] = temp_element

def bubble_sort_cards(card_list, list_length):
    bubble_sort_swap_count = 0
    for bubble_sort_i in range(list_length):
        for bubble_sort_j in range(list_length - 1, bubble_sort_i, -1):
            if card_list[bubble_sort_j].card_value < card_list[bubble_sort_j - 1].card_value:
                swap_elements(card_list, bubble_sort_j, bubble_sort_j - 1)
                bubble_sort_swap_count += 1
    return bubble_sort_swap_count

def selection_sort_cards(card_list, list_length):
    selection_sort_stable = True
    for selection_sort_i in range(list_length):
        selection_sort_min_index = selection_sort_i
        for selection_sort_j in range(selection_sort_i, list_length):
            if card_list[selection_sort_j].card_value < card_list[selection_sort_min_index].card_value:
                selection_sort_min_index = selection_sort_j
        if selection_sort_min_index != selection_sort_i:
            for selection_sort_k in range(selection_sort_i + 1, selection_sort_min_index):
                if card_list[selection_sort_k].card_value == card_list[selection_sort_i].card_value:
                    selection_sort_stable = False
            swap_elements(card_list, selection_sort_i, selection_sort_min_index)
    return selection_sort_stable

input_card_count = int(input())
input_card_strings = list(map(str, input().split()))
bubble_sort_card_list = [None] * input_card_count
selection_sort_card_list = [None] * input_card_count
for input_index in range(input_card_count):
    bubble_sort_card_list[input_index] = CardObject(input_card_strings[input_index])
    selection_sort_card_list[input_index] = CardObject(input_card_strings[input_index])

bubble_sort_total_swaps = bubble_sort_cards(bubble_sort_card_list, input_card_count)
selection_sort_is_stable = selection_sort_cards(selection_sort_card_list, input_card_count)

print_card_list(bubble_sort_card_list)
print('Stable')
print_card_list(selection_sort_card_list)
if selection_sort_is_stable:
    print('Stable')
else:
    print('Not stable')