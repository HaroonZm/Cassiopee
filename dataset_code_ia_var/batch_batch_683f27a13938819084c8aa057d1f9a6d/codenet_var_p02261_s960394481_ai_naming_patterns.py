def bubble_sort_coherent(input_list, sort_key_index=0):
    swap_count = 0
    sortable_list = [item if isinstance(item, list) else [item] for item in input_list[:]]
    last_index = len(sortable_list) - 1
    for outer_idx in range(0, last_index):
        for inner_idx in range(last_index, outer_idx, -1):
            if sortable_list[inner_idx][sort_key_index] < sortable_list[inner_idx - 1][sort_key_index]:
                sortable_list[inner_idx], sortable_list[inner_idx - 1] = sortable_list[inner_idx - 1], sortable_list[inner_idx]
                swap_count += 1
    formatted_list = [item[0] if len(item) == 1 else item for item in sortable_list]
    return {'sorted_list': formatted_list, 'swap_count': swap_count}

def selection_sort_coherent(input_list, sort_key_index=0):
    swap_count = 0
    sortable_list = [item if isinstance(item, list) else [item] for item in input_list[:]]
    list_length = len(sortable_list)
    for outer_idx in range(0, list_length):
        min_index = outer_idx
        for inner_idx in range(outer_idx, list_length):
            if sortable_list[inner_idx][sort_key_index] < sortable_list[min_index][sort_key_index]:
                min_index = inner_idx
        if min_index != outer_idx:
            sortable_list[outer_idx], sortable_list[min_index] = sortable_list[min_index], sortable_list[outer_idx]
            swap_count += 1
    formatted_list = [item[0] if len(item) == 1 else item for item in sortable_list]
    return {'sorted_list': formatted_list, 'swap_count': swap_count}

def format_card_list(card_list):
    return ' '.join([str(card[0]) + str(card[1]) for card in card_list])

if __name__ == '__main__':
    cards_input_count = int(input())
    cards_input_raw = list(map(list, input().split(' ')))
    cards_input = [[item[0], int(item[1])] for item in cards_input_raw]
    bubble_sorted_result = bubble_sort_coherent(cards_input, 1)
    selection_sorted_result = selection_sort_coherent(cards_input, 1)
    bubble_sorted_str = format_card_list(bubble_sorted_result['sorted_list'])
    selection_sorted_str = format_card_list(selection_sorted_result['sorted_list'])
    print(bubble_sorted_str)
    print('Stable')
    print(selection_sorted_str)
    print('Stable' if bubble_sorted_str == selection_sorted_str else 'Not stable')