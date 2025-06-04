from copy import deepcopy

def sort_bubble(cards_list, num_cards):
    sorted_cards = deepcopy(cards_list)
    for outer_idx in range(num_cards):
        for inner_idx in reversed(range(outer_idx + 1, num_cards)):
            if int(sorted_cards[inner_idx][1]) < int(sorted_cards[inner_idx - 1][1]):
                sorted_cards[inner_idx], sorted_cards[inner_idx - 1] = sorted_cards[inner_idx - 1], sorted_cards[inner_idx]
    return sorted_cards

def sort_selection(cards_list, num_cards):
    sorted_cards = deepcopy(cards_list)
    for outer_idx in range(num_cards):
        min_index = outer_idx
        for inner_idx in range(outer_idx, num_cards):
            if int(sorted_cards[inner_idx][1]) < int(sorted_cards[min_index][1]):
                min_index = inner_idx
        sorted_cards[outer_idx], sorted_cards[min_index] = sorted_cards[min_index], sorted_cards[outer_idx]
    return sorted_cards

def run_sorting_process():
    num_cards = int(input())
    cards_list = list(input().split())
    bubble_sorted = sort_bubble(cards_list, num_cards)
    print(*bubble_sorted)
    print("Stable")
    selection_sorted = sort_selection(cards_list, num_cards)
    print(*selection_sorted)
    if bubble_sorted == selection_sorted:
        print("Stable")
    else:
        print("Not stable")

if __name__ == "__main__":
    run_sorting_process()