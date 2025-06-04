def bubble_sort(cards_list, num_cards):
    for outer_idx in range(num_cards):
        for inner_idx in range(num_cards - 1, outer_idx, -1):
            if int(cards_list[inner_idx][1]) < int(cards_list[inner_idx - 1][1]):
                cards_list[inner_idx], cards_list[inner_idx - 1] = cards_list[inner_idx - 1], cards_list[inner_idx]

def selection_sort(cards_list, num_cards):
    for outer_idx in range(num_cards):
        min_idx = outer_idx
        for search_idx in range(outer_idx, num_cards):
            if int(cards_list[search_idx][1]) < int(cards_list[min_idx][1]):
                min_idx = search_idx
        cards_list[outer_idx], cards_list[min_idx] = cards_list[min_idx], cards_list[outer_idx]

num_cards = int(input())
input_cards = input().split()
original_cards = input_cards[:]
bubble_sorted_cards = input_cards[:]
bubble_sort(bubble_sorted_cards, num_cards)
print(' '.join(bubble_sorted_cards))
print('Stable')
selection_sorted_cards = original_cards[:]
selection_sort(selection_sorted_cards, num_cards)
print(' '.join(selection_sorted_cards))
if bubble_sorted_cards == selection_sorted_cards:
    print('Stable')
else:
    print('Not stable')